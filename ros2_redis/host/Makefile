include config.mk

DEFAULT := all

all: clean build

build: $(REQFILE)
	$(VENV) $(ENVNAME) 
	. $(ENV) && $(PIPINSTALL) -r $(REQFILE)

clean:
	rm -rf $(ENVNAME)


.PHONY: build clean
