.POSIX:

include config.mk

.DEFAULT_GOAL := help

h_build: h_init h_install
r_build: r_init r_install
v_build: v_rm v_init
v_rm: v_down v_clean

.PHONY: all # ----- (combo)[host,ros,rcp] build all
.PHONY: rm # ----- (combo)[host,ros,rcp] rm all
.PHONY: host # ----- (combo)[host] build
.PHONY: ros # ----- (combo)[ros] build
.PHONY: rcp # ----- (combo)[rcp] build

all: h_build v_build
rm: h_clean v_rm
host: h_build
ros: v_build
rcp: r_build

# --------------------------------------------------
# HELP

.SILENT:
.PHONY: help # [make] print this help text
help:
	@grep '^.PHONY: .* #' $(firstword $(MAKEFILE_LIST)) |\
		sed 's/\.PHONY: \(.*\) # \(.*\)/\1 # \2/' |\
		awk 'BEGIN {FS = "#"}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' 

# --------------------------------------------------
# ROS RULES

.SILENT:
.PHONY: v_check # [ros] check if 'docker' and 'docker-compose' commands exist
v_check:
	command -V $(DOCKER_COMPOSE_X) >/dev/null || exit 1
	command -V $(DOCKER_X) >/dev/null || exit 1 

.SILENT:
.PHONY: v_init # [ros] docker-compose up
v_init: v_check
	sudo $(DOCKER_COMPOSE_X) up

.SILENT:
.PHONY: v_down # [ros] docker-compose env clean and system prune
v_down: v_check
	echo "PRUNE all docker env objects"
	sudo docker system prune -f
	echo "RM $(PUBLISHER_IMG):latest docker image"
	sudo docker image ls | grep -i "$(PUBLISHER_IMG)" && \
		sudo docker rmi $(PUBLISHER_IMG):latest || \
		echo "image $(PUBLISHER_IMG):latest not found"

.SILENT:
.PHONY: v_clean # [ros] ros packages env clean
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
	
# --------------------------------------------------
# HOST RULES

.PHONY: h_init # [host] initialize python venv
h_init:
	$(PYTHON_X) -m venv $(HOST_REDIS_MIRROR_PATH)

.ONESHELL:
.PHONY: h_install # [host] source python venv and install dependencies
h_install:
	. $(HOST_REDIS_MIRROR_PATH)/bin/activate
	$(PYTHON_X) -m $(PIP_X) install --upgrade $(PIP_X)
	$(PIP_X) install -r $(HOST_REDIS_MIRROR_PATH)/requirements.txt

.ONESHELL:
.PHONY: h_resolve # [host] source python venv and update requirements.txt
h_resolve:
	. $(HOST_REDIS_MIRROR_PATH)/bin/activate
	$(PIP_X) freeze > $(HOST_REDIS_MIRROR_PATH)/requirements.txt

.PHONY: h_clean # [host] clean python venv
h_clean:
	-rm -rf $(HOST_REDIS_MIRROR_PATH)/bin
	-rm -rf $(HOST_REDIS_MIRROR_PATH)/include
	-rm -rf $(HOST_REDIS_MIRROR_PATH)/lib
	-rm -rf $(HOST_REDIS_MIRROR_PATH)/lib64
	-rm -f $(HOST_REDIS_MIRROR_PATH)/pyvenv.cfg
	-rm -rf $(HOST_REDIS_MIRROR_PATH)/__pycache__
	-rm -rf $(HOST_REDIS_MIRROR_PATH)/share

# --------------------------------------------------
# RCP RULES

.PHONY: r_init # [rcp] initialize python venv
r_init:
	$(PYTHON_X) -m venv $(RCP_PATH)

.ONESHELL:
.PHONY: r_install # [rcp] source python venv and install dependencies
r_install:
	. $(RCP_PATH)/bin/activate
	$(PYTHON_X) -m $(PIP_X) install --upgrade $(PIP_X)
	$(PIP_X) install -r $(RCP_PATH)/requirements.txt

.ONESHELL:
.PHONY: r_resolve # [rcp] source python venv and update requirements.txt
r_resolve:
	. $(RCP_PATH)/bin/activate
	$(PIP_X) freeze > $(RCP_PATH)/requirements.txt

.PHONY: r_clean # [rcp] clean python venv
r_clean:
	-rm -rf $(RCP_PATH)/bin
	-rm -rf $(RCP_PATH)/include
	-rm -rf $(RCP_PATH)/lib
	-rm -rf $(RCP_PATH)/lib64
	-rm -f $(RCP_PATH)/pyvenv.cfg
	-rm -rf $(RCP_PATH)/__pycache__
	-rm -rf $(RCP_PATH)/share
