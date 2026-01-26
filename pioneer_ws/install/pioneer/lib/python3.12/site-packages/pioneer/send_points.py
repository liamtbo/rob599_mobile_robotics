
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from goal_target.action import GoalTarget

# TODO need to transfrom world coords to robot coords somehow

class SendPoints(Node):

    def __init__(self, points):
        super().__init__('send_points_action_client')

        self.action_client = ActionClient(self, 
                                        action_type=GoalTarget,
                                        action_name='goal_target')
        self.points = points
        self.curr_points_idx = 0

        # start point sending process every 1 second until driver responds ready
        self.start_timer = self.create_timer(1.0, self._start_action_client)

    
    def _start_action_client(self):
        
        self.start_timer.cancel()

        if self.curr_points_idx == 0:
            self.get_logger().info("Waiting for driver to start")
            self.action_client.wait_for_server()
            self.get_logger().info(f'Driver has started')

        if self.curr_points_idx >= len(self.points):
            self.get_logger().info("Finished sending points")
            return

        curr_point = self.points[self.curr_points_idx]
        self.curr_points_idx += 1

        goal = GoalTarget.Goal()
        goal.goal.header.frame_id = 'odom'
        goal.goal.header.stamp = self.get_clock().now().to_msg()
        goal.goal.point.x = float(curr_point[0])
        goal.goal.point.y = float(curr_point[1])
        goal.goal.point.z = 0.0

        self.get_logger().info(f'Sending point {self.curr_points_idx-1}/{len(self.points) - 1}: {curr_point}')

        # sends a goal non-blocking (async) to the action server and give it a function to call as the action server executes the goal
        self._send_goal_future = self.action_client.send_goal_async(goal=goal, feedback_callback=self._feedback_callback)
        # when driver finishes goal, call this function
        self._send_goal_future.add_done_callback(self._goal_sent_callback)
    
    # as robots working to complete goal, this function triggers periodically with distance to go
    def _feedback_callback(self, feedback):
        self.last_distance = feedback.feedback.distance.data
        self.get_logger().info(f'Feedback: Distance to goal is {feedback.feedback.distance.data}')

    # reacts once goal is accepted by service and sets up results callback
    def _goal_sent_callback(self, future):
        self._goal_handle = future.result()
        if not self._goal_handle.accepted:
            self.get_logger().warn('Driver did not accept point')
        else:
            self.get_logger().info(f'Driver accepted point')
            self._result_future = self._goal_handle.get_result_async()
            # when point is reached, trigger function below
            self._result_future.add_done_callback(self._goal_done_callback)

    def _goal_done_callback(self, future):
        result = future.result().result
        if result:
            self.get_logger().info(f'Reached Point')
            self.start_timer.reset() # next point
        else:
            self.get_logger().info(f'Robot said it reached goal, but actually didnt')
    
def main():
    try:
        with rclpy.init():
            goals = [(4,4)]
            action_client = SendPoints(goals)
            rclpy.spin(action_client)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass

if __name__ == '__main__':
    main()