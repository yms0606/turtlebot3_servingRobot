import rclpy
from rclpy.node import Node
from serving_interface.srv import Order

class OrderServiceeServer(Node):
    def __init__(self):
        super().__init__('ros2_order_client')
        self.srv = self.create_service(Order, 'process_order', self.process_order_callback)

    def process_order_callback(self, request, response):
        self.get_logger().info(f"Received order: Table {request.table_num}, Menu: {request.menu}, Total: {request.total_price}")
        response.is_accept = True
        return response
    
def main(args=None):
    rclpy.init(args=args)
    node = OrderServiceeServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()