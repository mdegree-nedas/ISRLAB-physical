import collections


class Structure:
    def cfg_validate(self, cfg_src):
        robot_name = list(cfg_src.keys())[0]
        robot_configuration = cfg_src[robot_name]

        return self.__validate_robot_fields(robot_configuration) and self.__validate_sensors_fields(robot_configuration) and self.__validate_actuators_fields(robot_configuration) and self.__validate_commands_fields(robot_configuration)


    def __validate_robot_fields(self, configuration):
        configuration_names = list(configuration.keys())
        
        if  not ("sensors" in configuration_names and "actuators" in configuration_names and "commands" in configuration_names):
            return False

        return True
    

    def __validate_sensors_fields(self, configuration):
        sensors = configuration["sensors"]
        sensors_names = list(sensors.keys())

        if not ("ultrasound" in sensors_names and "lightsensor" in sensors_names and "linetracker" in sensors_names):
            return False

        for sensors_values in sensors.values():
            sensors_values_names = list(sensors_values.keys())

            if not ("id" in sensors_values_names and "type" in sensors_values_names and "address" in sensors_values_names and "data" in sensors_values_names):
                return False

        return True


    def __validate_actuators_fields(self, configuration):
        actuators = configuration["actuators"]
        actuators_names = list(actuators.keys())

        if not ("motion" in actuators_names and "led" in actuators_names):
            return False

        for actuators_values in actuators.values():
            actuators_values_names = list(actuators_values.keys())

            if not("id" in actuators_values_names and "address" in actuators_values_names and "commands" in actuators_values_names):
                return False

            if not isinstance(actuators_values["commands"], list):
                return False

        return True


    def __validate_commands_fields(self, configuration):
        commands = configuration["commands"]
        commands_command_list = list(commands.keys())
        total_commands = []
        
        for commands_values in commands.values():
            if not("data" in commands_values and "time" in commands_values):
                return False

        for command_list in configuration["actuators"].values():
            total_commands += command_list["commands"]

        if collections.Counter(commands_command_list) != collections.Counter(total_commands):
            return False

        return True
        
