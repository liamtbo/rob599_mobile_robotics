from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pioneer',      
            executable='driver',    
            name='driver',
            emulate_tty=True 
        )
    ])
