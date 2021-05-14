from librcp.generator.noros.generator_core import NoRosCoreGenerator
from librcp.generator.noros.generator_template import NoRosTemplateGenerator
from librcp.generator.noros.generator_interface import NoRosInterfaceGenerator


class Generator:
    def __init__(self):
        self.noros_core = NoRosCoreGenerator()
        self.noros_template = NoRosTemplateGenerator()
        self.noros_interface = NoRosInterfaceGenerator()
