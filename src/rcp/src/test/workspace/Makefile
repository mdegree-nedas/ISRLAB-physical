.SILENT: run
.PHONY: run
.ONESHELL:
run:
	pip3 install redis
	colcon build --symlink-install
	. install/setup.sh
	ros2 run ros_usage_example main

