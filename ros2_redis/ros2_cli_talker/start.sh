#!/bin/bash

echo "Sourcing ROS2..."
source /opt/ros/dashing/setup.bash

echo "sleep 90..."
sleep 90

echo "Publishing..."
ros2 topic pub /from_ros2 std_msgs/msg/String "{data: 'Hello from ROS2'}"
