rosdep install -i --from-path src --rosdistro kilted -y

colcon build --packages-select py_pubsub

in 1st terminal
    source install/setup.bash
    source /opt/ros/kilted/setup.bash
    cd ros2_tutorial_py_ws
    ros2 run py_pubsub talker

in 2nd terminal
    source install/setup.bash
    source /opt/ros/kilted/setup.bash
    cd ros2_tutorial_py_ws
    ros2 run py_pubsub listener