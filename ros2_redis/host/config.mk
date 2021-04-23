PYTHON = python3
VENV = $(PYTHON) -m venv
PIP = $(PYTHON) -m pip
PIPINSTALL = $(PIP) install

REQFILE = requirements.txt
ENVNAME = venv
ENV = $(ENVNAME)/bin/activate
