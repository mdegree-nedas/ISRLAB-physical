.POSIX:

include config.mk

.DEFAULT_GOAL := help

all: h_build
clean: h_clean

h_build: h_init h_install

.PHONY: h_init
h_init:
	python -m venv $(HOST_REDIS_MIRROR_PATH)

.ONESHELL:
.PHONY: h_install
h_install:
	. $(HOST_REDIS_MIRROR_PATH)/bin/activate
	python -m pip install --upgrade pip
	pip install -r $(HOST_REDIS_MIRROR_PATH)/requirements.txt

.ONESHELL:
.PHONY: h_resolve
h_resolve:
	. $(HOST_REDIS_MIRROR_PATH)/bin/activate
	pip freeze > $(HOST_REDIS_MIRROR_PATH)/requirements.txt

.PHONY: h_clean
h_clean:
	-rm -rf $(HOST_REDIS_MIRROR_PATH)/bin
	-rm -rf $(HOST_REDIS_MIRROR_PATH)/include
	-rm -rf $(HOST_REDIS_MIRROR_PATH)/lib
	-rm -rf $(HOST_REDIS_MIRROR_PATH)/lib64
	-rm -f $(HOST_REDIS_MIRROR_PATH)/pyvenv.cfg

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
