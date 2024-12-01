from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

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
         ),
    ])