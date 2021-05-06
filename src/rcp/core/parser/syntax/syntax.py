import yaml


class Syntax:
    def parse_yaml_file(self, file_name):
        """
        Reads a yaml file and returns the dict representation of it

        :param file_name: The file's name
        :return: dict representation of yaml in yaml file
        """
        yaml_str = self.__file_reader(file_name)
        return self.__yaml_converter(yaml_str)
        
    def __yaml_converter(self, yaml_str):
        """
        Converts a yaml string to dict

        :param yaml_str: The yaml string
        :return: dict representation of yaml_str
        """
        return yaml.load(yaml_str, Loader=yaml.FullLoader)

    def __file_reader(self, file_name):
        """
        Reads a file and returns the yaml string

        :param file_name: The file's name
        :return: Yaml string
        """
        with open(file_name, "r") as yaml_file:
            return yaml_file.read()
