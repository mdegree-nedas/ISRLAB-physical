OS = $(shell uname -s)

PYTHON_X ?= python3
PIP_X ?= pip
DOCKER_X ?= docker
DOCKER_COMPOSE_X ?= docker-compose

PUBLISHER_SRC ?= src/publisher
WORKSPACE_DIR ?= intelligent_systems_and_robotics_lab-physical-proj_
PUBLISHER_IMG ?= $(WORKSPACE_DIR)publisher

HOST_REDIS_MIRROR_PATH ?= src/raspberry/host_redis_mirror
RCP_PATH ?= src/rcp
