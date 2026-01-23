
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



import numpy as np
"""
I noticed this project was very similar to intro 1's so I built based off intro 1's code.
I didn't copy and paste anything in. I slowly developed it incrementally so that I could learn
intuitively how the code is built.
"""

class Driver(Node):

    def __init__(self):

        super().__init__('driver')

        self.action_server = ActionServer(node=self,
                                action_type=GoalTarget,
                                action_name="goal_target",
                                callback_group=ReentrantCallbackGroup(), # allow multiple callbacks to run concurrently
                                goal_callback=self.goal_accept_callback, # called when action client sends a goal
                                cancel_callback=self.cancel_callback, # called when the client asks to cancel a running goal
                                execute_callback=self.action_callback) # work function, runs to execute goal


        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 1)
        self.timer = self.create_timer(0.5, self.publish_cmd)


        # self.laser_scan = self.create_subscription(LaserScan, 'base_scan', self.scan_callback, 10)

        # self.goal = None
        # self.goals = [(5,5),]
        curr_goal = None
        self.curr_goal_idx = 0

        # self.timer = self.create_timer(1, self.action)

        self.target = PointStamped()
        self.target.point.x = 0.0
        self.target.point.y = 0.0

        # listens for tf2 transformations and stores them in buffer for up to 10 seconds
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.close_enough = False


    def goal_accept_callback(self, goal_request):
        self.get_logger().info("Goal request received")
        return GoalResponse.ACCEPT
    
    def cancel_callback(self, goal_handle):
        self.get_logger().info("Received cancel request from client")
        return CancelResponse.ACCEPT

    # TODO skip transofrmatin problem for now and just focus on obstacle avoidance. 
    def set_target(self):

        if self.goal:
            # odom is world frame, base_link is robot frame
            # duration gives it amount of time to keep checking before timeout
            # TODO come back and fix
            
            try:
                # query the listener for a specific transformation
                # arguments: target frame, source frame, the time at which we want to transfofrm
                transform = self.tf_buffer.lookup_transform('robot/base_link', 'robot/odom', rclpy.time.Time(), timeout=rclpy.duration.Duration(seconds=4.0))
                print(transform)
            except Exception as e:
                self.get_logger().warn(f'TF target lookup timed-out: {e}')
                return
            
            # this applies transform to point but doesn't work right now TODO
            self.target = do_transform_point(self.goal, transform)

            self.get_logger().info(f'worlds point: {self.goal}')
            self.get_logger().info(f'robots point: ({self.target.point.x}, {self.target.point.y})')
    
            self.get_logger().info(f'goal with respec to robot: ({self.target.point.x:.2f}, {self.target.point.y:.2f}), orig ({self.goal.point.x, self.goal.point.y})')
            
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
            # feedback.distance.data = self.distance_to_target()
            feedback.distance.data = 4.0
            goal_handle.publish_feedback(feedback)
            rate.sleep()

        self.goal = None
        # self.cmd_pub.publish(self.zero_twist())

        self.get_logger().info(f'Completed goal')

        goal_handle.succeed()

        result.success = True
        return result

    def publish_cmd(self):
        t = Twist()
        t.linear.x = 0.3
        t.linear.y = 0.0
        t.angular.z = 0.0
        self.cmd_pub.publish(t)
        self.get_logger().info('Publishing cmd_vel')

    def scan_callback(self):
        pass

    # def create_twist(self, scan):

    #     angle = self.get_angle(scan)

    # def get_angle(self, scan):

    #     # print(scan)
    #     self.i += 1
    #     print(f'scan: {self.i}')
        

def main(args=None):
    try:
        with rclpy.init(args=args):
            driver = Driver()
            rclpy.spin(driver)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass

if __name__ == '__main__':
    main()