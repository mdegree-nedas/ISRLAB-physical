.POSIX:

include config.mk

.DEFAULT_GOAL := help

all: h_build v_build
rm: h_clean v_rm

h_build: h_init h_install
v_build: v_rm v_init
v_rm: v_down v_clean

.SILENT:
.PHONY: v_check
v_check:
	command -V $(DOCKER_COMPOSE_X) >/dev/null || exit 1
	command -V $(DOCKER_X) >/dev/null || exit 1 

.SILENT:
.PHONY: v_init
v_init: v_check
	sudo $(DOCKER_COMPOSE_X) up

.SILENT:
.PHONY: v_down
v_down: v_check
	echo "PRUNE all docker env objects"
	sudo docker system prune -f
	echo "RM $(PUBLISHER_IMG):latest docker image"
	sudo docker image ls | grep -i "$(PUBLISHER_IMG)" && \
		sudo docker rmi $(PUBLISHER_IMG):latest || \
		echo "image $(PUBLISHER_IMG):latest not found"

.SILENT:
.PHONY: v_clean
v_clean:
	if [ -d "$(PUBLISHER_SRC)/log" ]; then \
		sudo rm -rf "$(PUBLISHER_SRC)/log"; \
	fi
	echo "DIR $(PUBLISHER_SRC)/log removed"
	if [ -d "$(PUBLISHER_SRC)/install" ]; then \
		sudo rm -rf "$(PUBLISHER_SRC)/install"; \
	fi
	echo "DIR $(PUBLISHER_SRC)/install removed"
	if [ -d "$(PUBLISHER_SRC)/build" ]; then \
		sudo rm -rf "$(PUBLISHER_SRC)/build"; \
	fi
	echo "DIR $(PUBLISHER_SRC)/build removed"
	
.PHONY: h_init
h_init:
	$(PYTHON_X) -m venv $(HOST_REDIS_MIRROR_PATH)

.ONESHELL:
.PHONY: h_install
h_install:
	. $(HOST_REDIS_MIRROR_PATH)/bin/activate
	$(PYTHON_X) -m $(PIP_X) install --upgrade $(PIP_X)
	$(PIP_X) install -r $(HOST_REDIS_MIRROR_PATH)/requirements.txt

.ONESHELL:
.PHONY: h_resolve
h_resolve:
	. $(HOST_REDIS_MIRROR_PATH)/bin/activate
	$(PIP_X) freeze > $(HOST_REDIS_MIRROR_PATH)/requirements.txt

.PHONY: h_clean
h_clean:
	-rm -rf $(HOST_REDIS_MIRROR_PATH)/bin
	-rm -rf $(HOST_REDIS_MIRROR_PATH)/include
	-rm -rf $(HOST_REDIS_MIRROR_PATH)/lib
	-rm -rf $(HOST_REDIS_MIRROR_PATH)/lib64
	-rm -f $(HOST_REDIS_MIRROR_PATH)/pyvenv.cfg
	-rm -rf $(HOST_REDIS_MIRROR_PATH)/__pycache__
	-rm -rf $(HOST_REDIS_MIRROR_PATH)/share

.SILENT:
.PHONY: help
help:
	echo "MACROS: "
	echo " * {DEFAULT} : help"
	echo
	echo " * {all}     : h_build"
	echo " * {clean}   : h_clean"
	echo
	echo " * {h_build} : h_init h_install"
	echo
	echo "RULES: "
	echo " - h_init    : create host_redis_mirror venv package"
	echo " - h_install : install host_redis_mirror venv deps"
	echo " - h_resolve : refresh host_redis_mirror venv requirements.txt file"
	echo " - h_clean   : clean host_redis_mirror venv package"
	echo " - help      : print this help message"
