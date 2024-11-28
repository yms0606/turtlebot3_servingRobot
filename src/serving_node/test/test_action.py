import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import PoseStamped
import time

class NavigateToPoseClient(Node):
    def __init__(self):
        super().__init__('action_test')
        self.action_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')
        self.last_feedback_time = 0

    def send_goal(self, pose):
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = pose

        self.action_client.wait_for_server()
        self.get_logger().info('Sending goal...')

        self.goal_handle = self.action_client.send_goal_async(goal_msg, feedback_callback = self.feedback_callback)
        self.goal_handle.add_done_callback(self.goal_response_callback)

    def feedback_callback(self, feedback_msg):
        current_time = time.time()
        if current_time - self.last_feedback_time >= 0.5:
            feedback = feedback_msg.feedback

            distance_remaining = feedback.distance_remaining
            current_x = round(feedback.current_pose.pose.position.x, 2)
            current_y = round(feedback.current_pose.pose.position.y, 2)

            if distance_remaining > 1.0:
                status = "가는중..."
            else:
                status = "거의 도착"

            self.get_logger().info(f"Current position: x: {current_x}, y: {current_y}, 로봇이 {status}")
            self.last_feedback_time = current_time

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return
        
        self.get_logger().info('Goal accepted')
        goal_handle.get_result_async().add_done_callback(self.result_callback)
            
    def result_callback(self, future):
        self.get_logger().info(f'Goal result: 배달 완료')

def main(args=None):
    rclpy.init(args=args)
    node = NavigateToPoseClient()

    target_pose = PoseStamped()
    target_pose.header.frame_id = 'map'
    target_pose.pose.position.x = 0.0
    target_pose.pose.position.y = 1.0
    target_pose.pose.orientation.w = 0.0

    node.send_goal(target_pose)

    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()