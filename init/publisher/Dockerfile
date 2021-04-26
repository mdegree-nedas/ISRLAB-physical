FROM isrlab/ros2_dashing_rpi:redis

MAINTAINER Valentino Di Giosaffatte valentino.digiosaffatte@student.univaq.it
MAINTAINER Riccardo Armando Di Prinzio riccardoarmando.diprinzio@student.univaq.it

# client
# publisher
# talker

SHELL ["/bin/bash", "-l", "-i", "-c"]

CMD cd /root/workspace && \
    colcon build --symlink-install && \
    . /root/workspace/install/setup.bash && \
	sleep 10 && \
        ros2 run virt_redis_mirror main
	# ros2 run publisher main

	# rosdep update && \
	# rosdep install -i --from-path src --rosdistro dashing -y && \
	# colcon build && \
