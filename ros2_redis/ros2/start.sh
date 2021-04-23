#!/bin/bash

echo "Installing deps..."
apt update && apt install -y python3-pip && pip3 install redis

echo "Sourcing ROS2 and building..."
source /opt/ros/dashing/setup.bash && cd /root/workspace && colcon build --symlink-install && source install/setup.bash && echo "starting ros2..." && ros2 run ros2_redis main
