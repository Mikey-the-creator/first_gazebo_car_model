import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, OpaqueFunction, RegisterEventHandler
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    pkg_name = 'minicar'
    robotXacroname = "differential_drive_robot"

    pkg_share = get_package_share_directory(pkg_name)
    model_path = os.path.join(pkg_share, 'model', 'robot.xacro')
    world_path = os.path.join(pkg_share, 'model', 'empty_world.world')

    robot_description = xacro.process_file(model_path).toxml()

    gazebo_launch =PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
    )
    
    nodeRobotStatePublisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description, 'use_sim_time': True}]
    )

    spawnModelNode = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', robotXacroname],
        output='screen'
    )

    LaunchDescriptionObject = LaunchDescription()
    
    LaunchDescriptionObject.add_action(IncludeLaunchDescription(gazebo_launch))
    
    LaunchDescriptionObject.add_action(spawnModelNode)
    LaunchDescriptionObject.add_action(nodeRobotStatePublisher)
    
    return LaunchDescriptionObject