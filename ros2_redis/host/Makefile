include config.mk

DEFAULT := all

all: clean build

build:
	$(VENV) $(ENVNAME) 
	. $(ENV) && $(PIPINSTALL) -r requirements.txt

clean:
	rm -rf $(ENVNAME)


.PHONY: build clean
