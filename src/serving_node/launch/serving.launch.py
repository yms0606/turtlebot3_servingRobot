from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription(
        [Node(
            package="serving_node",
            executable="order"
        ),
         Node(
             package="serving_node",
             executable="display"
         ),
         Node(
             package="serving_node",
             executable="robot"
         )
    ])