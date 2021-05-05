.DEFAULT_GOAL := all

all: rm build

rm:
	-rm -rf bin
	-rm -rf include
	-rm -rf lib
	-rm -rf lib64
	-rm -f pyvenv.cfg
	-rm -rf __pycache__
	-rm -rf mod/__pycache__


build: requirements.txt
	python3 -m venv .
	. bin/activate && pip install --upgrade pip && pip install -r requirements.txt

.PHONY: all rm build
