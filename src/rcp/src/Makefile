.POSIX:

PREFIX ?= .

DESTDIR_C ?= config
DESTDIR_T ?= test
DESTDIR_G ?= out

CONFIG_O ?= $(PREFIX)/$(DESTDIR_C)/freenove.yml

ACTUATORS_NOROS_EXAMPLE ?= $(PREFIX)/$(DESTDIR_T)/examples/actuators/noros_usage_example.py
SENSORS_NOROS_EXAMPLE ?= $(PREFIX)/$(DESTDIR_T)/examples/sensors/noros_usage_example.py

ACTUATORS_ROS_EXAMPLE ?= $(PREFIX)/$(DESTDIR_T)/examples/actuators/ros_usage_example.py

NOROS_EXAMPLE_PKG_PATH ?= host
ROS_EXAMPLE_PKG_PATH ?= workspace/src/ros_usage_example/ros_usage_example

PYTHON_X ?= python
RCP_X ?= rcp.py

.SILENT: help
.PHONY: help # print this help text
help:
	@grep '^.PHONY: .* #' $(firstword $(MAKEFILE_LIST)) |\
		sed 's/\.PHONY: \(.*\) # \(.*\)/\1 # \2/' |\
		awk 'BEGIN {FS = "#"}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' 

.SILENT: actuators
.PHONY: actuators # --- (combo) build and exec (actuators)
actuators: actuators_build actuators_exec

.SILENT: sensors
.PHONY: sensors # --- (combo) build and exec (sensors)
sensors: sensors_build sensors_exec


.PHONY: build # generate libraries code
build:
	@$(PYTHON_X) $(RCP_X) $(CONFIG_O)

.PHONY: sensors_build # parse, generate, and update examples (sensors)
sensors_build: build
	# chown
	sudo chown -R ${USER}:${USER} $(PREFIX)/$(DESTDIR_T)/workspace
	rm -rf $(PREFIX)/$(DESTDIR_T)/workspace/build
	rm -rf $(PREFIX)/$(DESTDIR_T)/workspace/install
	rm -rf $(PREFIX)/$(DESTDIR_T)/workspace/log
	# copy ros example and library
	# copy noros example and library
	cp -rf $(SENSORS_NOROS_EXAMPLE) $(PREFIX)/$(DESTDIR_T)/$(NOROS_EXAMPLE_PKG_PATH)
	cp -rf $(PREFIX)/$(DESTDIR_G)/freenove_4WD_smart_car/noros $(PREFIX)/$(DESTDIR_T)/$(NOROS_EXAMPLE_PKG_PATH)
	rm -rf $(PREFIX)/$(DESTDIR_T)/$(NOROS_EXAMPLE_PKG_PATH)/noros/__pycache__


.PHONY: actuators_build # parse, generate, and update examples (actuators)
actuators_build: build
	# chown
	sudo chown -R ${USER}:${USER} $(PREFIX)/$(DESTDIR_T)/workspace
	rm -rf $(PREFIX)/$(DESTDIR_T)/workspace/build
	rm -rf $(PREFIX)/$(DESTDIR_T)/workspace/install
	rm -rf $(PREFIX)/$(DESTDIR_T)/workspace/log
	# copy ros example and library
	cp -rf $(ACTUATORS_ROS_EXAMPLE) $(PREFIX)/$(DESTDIR_T)/$(ROS_EXAMPLE_PKG_PATH)/main.py
	cp -rf $(PREFIX)/$(DESTDIR_G)/freenove_4WD_smart_car/ros $(PREFIX)/$(DESTDIR_T)/$(ROS_EXAMPLE_PKG_PATH)
	rm -rf $(PREFIX)/$(DESTDIR_T)/$(ROS_EXAMPLE_PKG_PATH)/__pycache__
	# copy noros example and library
	cp -rf $(ACTUATORS_NOROS_EXAMPLE) $(PREFIX)/$(DESTDIR_T)/$(NOROS_EXAMPLE_PKG_PATH)
	cp -rf $(PREFIX)/$(DESTDIR_G)/freenove_4WD_smart_car/noros $(PREFIX)/$(DESTDIR_T)/$(NOROS_EXAMPLE_PKG_PATH)
	rm -rf $(PREFIX)/$(DESTDIR_T)/$(NOROS_EXAMPLE_PKG_PATH)/noros/__pycache__

.SILENT: sensors_exec
.PHONY: sensors_exec # exec ros/noros examples
sensors_exec:
	# docker-compose -f ./test/docker-compose.yml up -d
	$(PYTHON_X) $(PREFIX)/$(DESTDIR_T)/$(NOROS_EXAMPLE_PKG_PATH)/noros_usage_example.py

.SILENT: actuators_exec
.PHONY: actuators_exec # exec ros/noros examples
actuators_exec:
	docker-compose -f ./test/docker-compose.yml up -d
	$(PYTHON_X) $(PREFIX)/$(DESTDIR_T)/$(NOROS_EXAMPLE_PKG_PATH)/noros_usage_example.py

.SILENT: rm
.PHONY: rm # clean env
rm:
	docker-compose -f ./test/docker-compose.yml down
	docker system prune -f
	docker volume prune -f
	docker network prune -f
