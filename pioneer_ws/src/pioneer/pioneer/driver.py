
import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from rclpy.action import ActionServer, CancelResponse, GoalResponse

# from goal_target.action import GoalTarget
from rclpy.callback_groups import ReentrantCallbackGroup
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist, PointStamped

from tf2_ros.transform_listener import TransformListener
from tf2_ros.buffer import Buffer
from tf2_geometry_msgs import do_transform_point

import numpy
import copy

# For publishing markers to rviz
from visualization_msgs.msg import Marker

import numpy as np

"""
CITATION:
This projects code is inspired from ROB intro 1's project. 
That code was developed by Professor Bill Smart.
"""

class Driver(Node):

    def __init__(self):

        super().__init__('driver')

        # self.action_server = ActionServer(node=self,
        #                         action_type=GoalTarget,
        #                         action_name="goal_target",
        #                         callback_group=ReentrantCallbackGroup(), # allow multiple callbacks to run concurrently
        #                         goal_callback=self.goal_accept_callback, # called when action client sends a goal
        #                         cancel_callback=self.cancel_callback, # called when the client asks to cancel a running goal
        #                         execute_callback=self.action_callback) # work function, runs to execute goal

        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 1)
        # self.timer = self.create_timer(0.5, self.publish_cmd)

        # listens for tf2 transformations and stores them in buffer for up to 10 seconds
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.close_enough = False

        # goal in world
        # self.goal = None

        # For some reason, tf buffer lookup transform always fails on first pass, skipping the first point
        # thus, i added this arbitrary first point to be skipped.
        self.goal0 = PointStamped()
        self.goal0.header.frame_id = 'robot/odom'
        self.goal0.header.stamp = self.get_clock().now().to_msg()
        self.goal0.point.x = 0.0
        self.goal0.point.y = 0.0
        self.goal0.point.z = 0.0

        self.goal1 = PointStamped()
        self.goal1.header.frame_id = 'robot/odom'
        self.goal1.header.stamp = self.get_clock().now().to_msg()
        self.goal1.point.x = 7.0
        self.goal1.point.y = 7.0
        self.goal1.point.z = 0.0

        self.goal2 = PointStamped()
        self.goal2.header.frame_id = 'robot/odom'
        self.goal2.header.stamp = self.get_clock().now().to_msg()
        self.goal2.point.x = -5.0
        self.goal2.point.y = -5.0
        self.goal2.point.z = 0.0

        self.goal3 = PointStamped()
        self.goal3.header.frame_id = 'robot/odom'
        self.goal3.header.stamp = self.get_clock().now().to_msg()
        self.goal3.point.x = -3.0
        self.goal3.point.y = -5.0
        self.goal3.point.z = 0.0

        self.goal_list = [self.goal0, self.goal1, self.goal2, self.goal3]
        self.goal_idx = 0
        self.goal = self.goal_list[self.goal_idx]
        self.get_logger().info(f'goal tuple: {(self.goal.point.x, self.goal.point.y, self.goal.point.z)}')

        # goal in robot coordinates
        self.target = PointStamped()
        self.target.point.x = 0.0
        self.target.point.y = 0.0
        self.set_target()

        self.get_logger().info(f'target x: {self.target.point.x}, target y: {self.target.point.y}')

        self.done = False

        self.sub = self.create_subscription(LaserScan, '/base_scan', self.scan_callback, 10)
        self.last_scan_time = self.get_clock().now()


    def goal_accept_callback(self, goal_request):
        self.get_logger().info("Goal request received")
        return GoalResponse.ACCEPT
    
    def cancel_callback(self, goal_handle):
        self.get_logger().info("Received cancel request from client")
        return CancelResponse.ACCEPT

    # can't get this to work well
    # def action_callback(self, goal_handle):
    #     self.get_logger().info(f"Executing goal: {goal_handle.request.goal.point}")

    #     self.goal = PointStamped()
    #     self.goal.header = goal_handle.request.goal.header
    #     self.goal.point = goal_handle.request.goal.point

    #     result = GoalTarget.Result()
    #     result.success = False

    #     self.set_target()
        
    #     rate = self.create_rate(20)   # 20 Hz (20 times per second)

    #     while not self.close_enough:
    #         feedback = GoalTarget.Feedback()
    #         # feedback.distance.data = self.distance_to_target() TODO
    #         feedback.distance.data = 4.0
    #         goal_handle.publish_feedback(feedback)
    #         # self.get_logger().info(f'in action loop')
    #         rate.sleep()

    #     self.goal = None
    #     # self.cmd_pub.publish(self.zero_twist())

    #     self.get_logger().info(f'Completed goal')

    #     goal_handle.succeed()

    #     result.success = True
    #     return result

    def scan_callback(self, scan):

        # slow it down a bit
        now = self.get_clock().now()
        if (now - self.last_scan_time).nanoseconds < 2e8:  # 0.2 sec = 5 Hz
            return
        self.last_scan_time = now

        if self.done:
            self.cmd_pub.publish(Twist())  # stop robot
            return

        if self.distance_error() < 0.2:
            # self.get_logger().info(f'distance_error: {self.distance_error()}')
            # self.get_logger().info("Reached goal!")
            self.get_logger().info(f'goal_idx: {self.goal_idx}')
            if self.goal_idx + 1 <= len(self.goal_list) - 1:
                self.goal_idx += 1
            else:
                self.get_logger().info('All Goals Completed')
                self.done = True
                return

        self.goal = self.goal_list[self.goal_idx]

        # self.get_logger().info('in scan callback')
        if self.goal:
            self.set_target()
            
            t = self.get_twist(scan)
        else:
            t = Twist()
            self.get_logger().info(f'No goal to move towards')
        
        self.cmd_pub.publish(t)

    def set_target(self):
        if self.goal:
            try:
                # query the listener for a specific transformation
                # arguments: target frame, source frame, the time at which we want to transfofrm
                # transform = self.tf_buffer.lookup_transform('robot/base_link', 'robot/odom', rclpy.time.Time(), timeout=rclpy.duration.Duration(seconds=4.0))
                transform = self.tf_buffer.lookup_transform(
                    'robot/odom',
                    'robot/base_link',
                    rclpy.time.Time(),
                    timeout=rclpy.duration.Duration(seconds=1.0)
                )
                
            except Exception as e:
                self.get_logger().warn(f'TF target lookup timed-out: {e}')
                return
            
            # this applies transform to point but doesn't work right now TODO
            # self.target = do_transform_point(self.goal, transform)

			# This does the transform manually, by calculating the theta rotation from the quaternion
            euler_ang = -np.arctan2(2 * transform.transform.rotation.z * transform.transform.rotation.w,
                                1.0 - 2 * transform.transform.rotation.z * transform.transform.rotation.z)

            # Translate to the base link's origin
            x = self.goal.point.x - transform.transform.translation.x
            y = self.goal.point.y - transform.transform.translation.y

            # Do the rotation
            rot_x = x * np.cos(euler_ang) - y * np.sin(euler_ang)
            rot_y = x * np.sin(euler_ang) + y * np.cos(euler_ang)

            self.target.point.x = rot_x
            self.target.point.y = rot_y

            # self.get_logger().info(f'worlds point: ({self.goal.point.x, self.goal.point.y})')
            # self.get_logger().info(f'robots point: ({self.target.point.x}, {self.target.point.y})')

            # self.get_logger().info(f'goal with respect to robot: ({self.target.point.x:.2f}, {self.target.point.y:.2f}), orig ({self.goal.point.x, self.goal.point.y})')
            
        else:
            # self.get_logger().info(f'There is no target to set')
            self.target = None		


    def get_twist(self, scan):

        t = Twist()
        target_x = self.target.point.x
        target_y = self.target.point.y
        target_angle = np.arctan2(target_y, target_x)
        # self.get_logger().info(f'target_x: {target_x}')
        # self.get_logger().info(f'target_y: {target_y}')
        # self.get_logger().info(f'angle: {target_angle}')
        # self.get_logger().info(f'distance error: {self.distance_error()}')
        vfh_angle = self.vector_field_histogram(scan, target_angle, threshold=2)
        # self.get_logger().info(f'vfh angle: {vfh_angle}')
        t.angular.z = vfh_angle
        # t.angular.z = target_angle * 0.4
        t.linear.x = self.distance_error() * 0.5
        return t

    def vector_field_histogram(self, scan, target_angle, threshold=2, bin_size=10,):

        # create polar histogram and associated angles parallel array
        scan_dist = np.array(scan.ranges) # len(scan_values) = 180
        scan_angle = np.linspace(scan.angle_min, scan.angle_max, len(scan.ranges))

        dist_bins = []
        angle_bins = []
        bin_size = 10
        
        # discretize the angles and distance
        for i in range(0, len(scan_dist), bin_size - 1):
            start = i
            end = min(i + (bin_size - 1) + 1, len(scan_dist)) # -1 bc that how bins overlap and +1 bc we want the end integer when slicing
            dist_bin = scan_dist[start:end].min()
            dist_bins.append(float(dist_bin))
            angle_bins.append(scan_angle[start:end])

        # testing TODO remove
        # for i in range(len(dist_bins)):
        #     self.get_logger().info(f'i: {i}')
        #     self.get_logger().info(f'\tdist_bins: {dist_bins[i]}')
        #     self.get_logger().info(f'\tangle_bins: {angle_bins[i]}')

        # find bins that don't have an object near
        # self.get_logger().info(f'Num of bins: {len(dist_bins)}')
        free_bins = []
        free_angles = []
        for i, dist in enumerate(dist_bins):
            if dist >= threshold:
                free_bins.append(dist)
                free_angles.append(angle_bins[i])
        # self.get_logger().info(f'free_bins: {free_bins}')
        # self.get_logger().info(f'Num of free bins: {len(free_bins)}')

        # combine adjacent angle bins
        if len(free_angles) == 0:
            return target_angle

        grouped_angles = [] 
        local_group = copy.copy(free_angles[0])
        for i in range(1, len(free_angles)):
            # print(f'free_angle: {free_angles[i]}')
            if free_angles[i][0] == free_angles[i - 1][-1]:
                # print('if path\n')
                if len(free_angles) > 1:
                    local_group = np.concatenate((local_group, free_angles[i][1:])) # don't add a duplicate angle
                if i == len(free_angles) - 1:
                    grouped_angles.append(local_group)
            else:
                # print(f'else path\n')
                grouped_angles.append(local_group)
                local_group = copy.copy(free_angles[i])
                if i == len(free_angles) - 1:
                    grouped_angles.append(local_group)

        # for i in range(len(grouped_angles)):
        #     self.get_logger().info(f'Grouped Angle {i}: {grouped_angles[i]}')

        # out of the free bins, which is closest to target angle
        closest_angle = None
        target_angle_bin = np.array([])
        for angle_bin in grouped_angles:
            if target_angle > angle_bin[-1]:
                continue
            target_angle_bin = angle_bin
            min_error = float('inf')
            for i, candidate in enumerate(angle_bin):
                err = abs(target_angle - candidate)
                if err < min_error:
                    min_error = err
                    closest_angle = candidate
                    target_angle_bin = angle_bin
            break
        # self.get_logger().info(f'closest_angle: {closest_angle}')
        # self.get_logger().info(f'target_angle_bin: {target_angle_bin}')
        
        # add padding to angle
        # self.get_logger().info(f'target_angle_bin min: {target_angle_bin[0]}')
        # self.get_logger().info(f'target_angle_bin max: {target_angle_bin[-1]}')

        if not target_angle_bin.any():
            return target_angle

        padding = 20 # padding off the extremes of target_angle_bin
        padded_angle = target_angle
        padded_angle_i = None
        if closest_angle == target_angle_bin[0]:
            padded_angle_i = min(0 + padding, len(target_angle_bin) - 1)
            padded_angle = target_angle_bin[padded_angle_i]
        elif closest_angle == target_angle_bin[-1]:
            padded_angle_i = max(len(target_angle_bin) - 1 - padding, 0)
            padded_angle = target_angle_bin[padded_angle_i]
        # self.get_logger().info(f'padding_idx: {padded_angle_i}')
        
        return padded_angle
    

    def distance_error(self):
        target_x = self.target.point.x
        target_y = self.target.point.y
        return np.sqrt(target_x**2 + target_y**2)


    def publish_cmd(self):
        t = Twist()
        t.linear.x = 0.3
        t.linear.y = 0.0
        t.angular.z = 0.0
        self.cmd_pub.publish(t)
        self.get_logger().info('Publishing cmd_vel')
        

def main(args=None):
    try:
        with rclpy.init(args=args):
            driver = Driver()
            rclpy.spin(driver)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass

if __name__ == '__main__':
    main()