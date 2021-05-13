from librcp.generator.generator_core import CoreGenerator
from librcp.generator.generator_template import TemplateGenerator
from librcp.generator.generator_interface import InterfaceGenerator


class Generator:
    def __init__(self):
        self.core = CoreGenerator()
        self.template = TemplateGenerator()
        self.interface = InterfaceGenerator()
