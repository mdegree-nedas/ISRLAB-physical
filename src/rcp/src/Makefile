.POSIX:

PREFIX ?= .

DESTDIR_C ?= config
DESTDIR_T ?= test
DESTDIR_G ?= out

CONFIG_O ?= $(PREFIX)/$(DESTDIR_C)/freenove.yml

NOROS_EXAMPLE ?= $(PREFIX)/$(DESTDIR_T)/noros_usage_example.py
ROS_EXAMPLE_PKG_PATH ?= workspace/src/ros_usage_example/ros_usage_example

PYTHON_X ?= python
RCP_X ?= rcp.py

.SILENT: help
.PHONY: help # print this help text
help:
	@grep '^.PHONY: .* #' $(firstword $(MAKEFILE_LIST)) |\
		sed 's/\.PHONY: \(.*\) # \(.*\)/\1 # \2/' |\
		awk 'BEGIN {FS = "#"}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' 

.PHONY: build # parse, generate, and update examples
build:
	@$(PYTHON_X) $(RCP_X) $(CONFIG_O)
	cp -rf $(PREFIX)/$(DESTDIR_T)/ros_usage_example.py $(PREFIX)/$(DESTDIR_T)/$(ROS_EXAMPLE_PKG_PATH)/main.py
	cp -rf $(PREFIX)/$(DESTDIR_G)/freenove_4WD_smart_car/ros $(PREFIX)/$(DESTDIR_T)/$(ROS_EXAMPLE_PKG_PATH)
	sudo chown -R ${USER}:${USER} $(PREFIX)/$(DESTDIR_T)/workspace

.SILENT: exec
.PHONY: exec # exec ros/noros examples
exec:
	docker-compose -f ./test/docker-compose.yml up -d
	$(PYTHON_X) $(NOROS_EXAMPLE)

.SILENT: rm
.PHONY: rm # clean env
rm:
	docker-compose -f ./test/docker-compose.yml down
	docker system prune -f
	docker volume prune -f
	docker network prune -f
