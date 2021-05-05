import yaml


# yaml file -> yaml string
def _file_reader(file_name):
    """
    Reads a file and returns the yaml string

    :param file_name: The file's name
    :return: Yaml string
    """
    with open(file_name, 'r') as yaml_file:
        return yaml_file.read()

# yaml string -> dict
def _yaml_converter(yaml_str):
    """
    Converts a yaml string to dict

    :param yaml_str: The yaml string
    :return: dict representation of yaml_str
    """
    return yaml.load(yaml_str, Loader=yaml.FullLoader)

# dict fields follow the rules?
def _rule_checker(robot):
    """
    Checks the structure of the given robot dict object

    :param : robot dict structure
    :return: True if structure follows the rules, False instead
    """
    # TODO: what are the rules?
    return True


def parse_robot_structure(file_name):
    """
    Reads the yaml file containing the structure of a robot and, if it follows the rules, returns a dict representation of it

    :param : filename that contains a yaml robot structure
    :return: dict representation of the robot structure
    """
    yaml_str = _file_reader(file_name)
    obj = _yaml_converter(yaml_str)

    if not _rule_checker(obj):
        raise Exception("The yaml robot structure doesn't follow the rules")
    
    return obj
