
import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from rclpy.action import ActionServer, CancelResponse, GoalResponse

from goal_target.action import GoalTarget
from rclpy.callback_groups import ReentrantCallbackGroup
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist, PointStamped

from tf2_ros.transform_listener import TransformListener
from tf2_ros.buffer import Buffer
from tf2_geometry_msgs import do_transform_point

import numpy



import numpy as np
"""
I noticed this project was very similar to intro 1's so I built based off intro 1's code.
I didn't copy and paste anything in. I slowly developed it incrementally so that I could learn
intuitively how the code is built.
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

        self.sub = self.create_subscription(LaserScan, '/base_scan', self.scan_callback, 10)
        self.last_scan_time = self.get_clock().now()


        # listens for tf2 transformations and stores them in buffer for up to 10 seconds
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.close_enough = False

        # goal in world
        # self.goal = None

        self.goal = PointStamped()
        self.goal.header.frame_id = 'robot/odom'
        self.goal.header.stamp = self.get_clock().now().to_msg()
        self.goal.point.x = 4.0
        self.goal.point.y = 4.0
        self.goal.point.z = 0.0
        
        # self.goal = (4,4)
        self.curr_goal_idx = 0

        # goal in robot coordinates
        self.target = PointStamped()
        self.target.point.x = 0.0
        self.target.point.y = 0.0

    def goal_accept_callback(self, goal_request):
        self.get_logger().info("Goal request received")
        return GoalResponse.ACCEPT
    
    def cancel_callback(self, goal_handle):
        self.get_logger().info("Received cancel request from client")
        return CancelResponse.ACCEPT

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

            self.get_logger().info(f'worlds point: ({self.goal.point.x, self.goal.point.y})')
            self.get_logger().info(f'robots point: ({self.target.point.x}, {self.target.point.y})')

            self.get_logger().info(f'goal with respect to robot: ({self.target.point.x:.2f}, {self.target.point.y:.2f}), orig ({self.goal.point.x, self.goal.point.y})')
            
        else:
            self.get_logger().info(f'There is no target to set')
            self.target = None		

    def action_callback(self, goal_handle):
        self.get_logger().info(f"Executing goal: {goal_handle.request.goal.point}")

        self.goal = PointStamped()
        self.goal.header = goal_handle.request.goal.header
        self.goal.point = goal_handle.request.goal.point

        result = GoalTarget.Result()
        result.success = False

        self.set_target()
        
        rate = self.create_rate(20)   # 20 Hz (20 times per second)

        while not self.close_enough:
            feedback = GoalTarget.Feedback()
            # feedback.distance.data = self.distance_to_target() TODO
            feedback.distance.data = 4.0
            goal_handle.publish_feedback(feedback)
            # self.get_logger().info(f'in action loop')
            rate.sleep()

        self.goal = None
        # self.cmd_pub.publish(self.zero_twist())

        self.get_logger().info(f'Completed goal')

        goal_handle.succeed()

        result.success = True
        return result

    def scan_callback(self, scan):

        # slow it down a bit
        now = self.get_clock().now()
        if (now - self.last_scan_time).nanoseconds < 2e8:  # 0.2 sec = 5 Hz
            return
        self.last_scan_time = now

        self.get_logger().info('in scan callback')
        if self.goal:
            self.set_target()
            
            t = self.get_twist(scan)
        else:
            t = Twist()
            self.get_logger().info(f'No goal to move towards')
        
        self.cmd_pub.publish(t)

    def get_twist(self, scan):

        t = Twist()
        target_x = self.target.point.x
        target_y = self.target.point.y
        angle = np.arctan2(target_y, target_x)
        self.get_logger().info(f'target_x: {target_x}')
        self.get_logger().info(f'target_y: {target_y}')
        self.get_logger().info(f'angle: {angle}')
        self.get_logger().info(f'distance error: {self.distance_error()}')
        t.angular.z = angle * 0.1
        t.linear.x = self.distance_error() * 0.05
        return t

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