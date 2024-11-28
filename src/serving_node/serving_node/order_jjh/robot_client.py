import rclpy
from rclpy.node import Node
from serving_interface.srv import ServingStatus

class TurtleBotClient(Node):
    def __init__(self):
        super().__init__('turtlebot_client')
        self.client = self.create_client(ServingStatus, 'serving_status')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for ServingStatus service...')
        self.get_logger().info('Connected to ServingStatus service!')

    def send_status(self, is_arrived):
        request = ServingStatus.Request()
        request.is_arrived = is_arrived

        self.get_logger().info(f'Sending is_arrived: {is_arrived}')
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result():
            response = future.result()
            self.get_logger().info(f'Received get_back: {response.get_back}')
            return response.get_back
        else:
            self.get_logger().error('Service call failed')
            return False


def main(args=None):
    rclpy.init(args=args)
    turtlebot_client = TurtleBotClient()

    try:
        # 예제: 도착 -> 복귀 요청
        arrived = True
        get_back = turtlebot_client.send_status(arrived)
        if get_back:
            turtlebot_client.get_logger().info('Returning to initial position...')
        else:
            turtlebot_client.get_logger().info('No return requested.')
    finally:
        turtlebot_client.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
