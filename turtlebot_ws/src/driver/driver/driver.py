# Every Python node in ROS2 should include these lines.  rclpy is the basic Python
# ROS2 stuff, and Node is the class we're going to use to set up the node.
import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException

# from geometry_msgs.msg import TwistStamped
from geometry_msgs.msg import Twist


class Driver(Node):

    def __init__(self):

        super().__init__('driver')

        self.cmd_pub = self.create_publisher(Twist, 'cmd_vel', 1)

        self.timer = self.create_timer(0.1, self.publish_cmd)

    def publish_cmd(self):
        t = Twist()
        t.linear.x = 1.0
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