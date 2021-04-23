include config.mk

DEFAULT := all

all: clean build

build: $(REQFILE)
	$(VENV) $(ENVNAME) 
	. $(ENV) && $(PIPINSTALL) -r $(REQFILE)

clean:
	rm -rf $(ENVNAME)
	rm -rf __pycache__

start: $(ENV) $(MAIN)
	. $(ENV) && $(PYTHON) $(MAIN)


.PHONY: build clean start
