import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from serving_interface.srv import ServingStatus
import math


class TurtleBotClient(Node):
    def __init__(self):
        super().__init__('turtlebot_client')
        # Create service client
        self.client = self.create_client(ServingStatus, 'serving_status')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for Table Order Server...')
        self.get_logger().info('Connected to Table Order Server!')

        # Subscribe to /odom to get the robot's current position
        self.subscription = self.create_subscription(
            Odometry, '/odom', self.odom_callback, 10
        )
        self.current_position = None  # To store the current position of the robot

        # Table positions (x, y) for each table (from the provided data)
        self.table_positions = {
            1: (1.277221791349055, 1.6058266331783906),
            2: (1.2993672267175878, 0.4889310444008698),
            3: (1.3120198653499835, -0.4876605614055664),
            4: (2.4809115369173242, 1.6540902169757656),
            5: (2.4564183301035545, 0.5146326969974298),
            6: (2.4100204518975747, -0.623137814815407),
            7: (3.6524732694758115, 1.614374148835083),
            8: (3.9135246611118406, 0.5120813128241669),
            9: (3.755207311676657, -0.6681678861865618)
        }

        # Offset to convert RViz coordinates to TurtleBot's coordinates
        self.destination_offset = (-2.0, -1.0)  # Example offset, adjust based on your setup

        # Example: Set the destination to table 3 (you can change the table number)
        self.destination_table = 3
        self.update_destination()

    def update_destination(self):
        """Update the destination by applying the offset."""
        original_pos = self.table_positions[self.destination_table]
        self.destination_rviz = (
            original_pos[0] + self.destination_offset[0],
            original_pos[1] + self.destination_offset[1]
        )

    def odom_callback(self, msg):
        """Callback to update the current position of the robot."""
        self.current_position = (
            msg.pose.pose.position.x,
            msg.pose.pose.position.y
        )

    def is_at_destination(self):
        """Check if the robot is at the destination."""
        if self.current_position is None:
            return False
        dest_x, dest_y = self.destination_rviz
        current_x, current_y = self.current_position
        distance = math.sqrt((current_x - dest_x)**2 + (current_y - dest_y)**2)
        self.get_logger().info(f'Distance to destination: {distance}')
        return distance < 0.7  # Threshold for arrival (in meters)

    def send_request(self):
        """Send the arrival status to the server."""
        request = ServingStatus.Request()
        request.is_arrived = self.is_at_destination()
        self.get_logger().info(f'Sending is_arrived={request.is_arrived} to server...')
        self.future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()





def main(args=None):
    rclpy.init(args=args)
    client = TurtleBotClient()

    while rclpy.ok():
        rclpy.spin_once(client)
        if client.is_at_destination():
            # Send request to server when at destination
            response = client.send_request()
            if response.get_back:
                client.get_logger().info('Server requested return to start position.')
            else:
                client.get_logger().info('No return requested.')
            break

    rclpy.shutdown()


if __name__ == '__main__':
    main()
