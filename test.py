import rclpy
from rclpy.node import Node
from serving_interface.srv import *
import threading

class TestNode(Node):

    def __init__(self):
        super().__init__("test_node")
        self.cli = self.create_client(ServingStatus,"test")

        while not self.cli.wait_for_service(timeout_sec=5.0):
            self.get_logger().info("waiting")

        self.req = ServingStatus.Request()
        self.req.is_arrived = False

        threading.Thread(target=self.send_request,daemon=True).start()

    
    def send_request(self):
        while True:
            input("input enter\n")
            future = self.cli.call_async(self.req)
            self.get_logger().info('success')
            future.add_done_callback(self.callback_req)
    
    def callback_req(self, res):
        response = res.result()
        self.get_logger().info(f"res: {response.get_back}")


if __name__ == "__main__":

    rclpy.init()
    testnode = TestNode()
    rclpy.spin(testnode)
    
    testnode.destroy_node()
    rclpy.shutdown()