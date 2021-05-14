from pathlib import Path
import os


class RosCoreGenerator:
    def __init__(self):
        self._cfg_dict = None

        self._gen_name_k = None
        self._gen_sensors_k = None
        self._gen_vector_sensors = []
        self._gen_actuators_k = None
        self._gen_vector_actuators = []
        self._gen_commands_k = None
        self._gen_vector_commands = []

    def _initialize(self, cfg_dict, cfg_parse):
        self._cfg_dict = cfg_dict

        (
            self._gen_name_k,
            self._gen_sensors_k,
            self._gen_vector_sensors,
            self._gen_actuators_k,
            self._gen_vector_actuators,
            self._gen_commands_k,
            self._gen_vector_commands,
        ) = cfg_parse[:]

        self._sep = "/"
        self._ext = ".py"

        self._tab = "    "
        self._2tab = self._tab * 2
        self._3tab = self._tab * 3
        self._4tab = self._tab * 4
        self._nl = "\n"

    def _initialize_core(self):
        self._prefix = "."
        self._destdir = "out" + self._sep + self._gen_name_k + self._sep + "ros"
        Path(self._prefix + self._sep + self._destdir).mkdir(
            parents=True, exist_ok=True
        )

        self._filename = (
            self._prefix + self._sep + self._destdir + self._sep + "core" + self._ext
        )

        payload = [
            "# rcp: CORE MODULE" + self._nl,
            "# rcp: auto-generated ros foreign broker file" + self._nl,
            "# rcp: do not edit this file" + self._nl,
            self._nl,
        ]

        f = open(self._filename, "w")
        f.writelines(payload)
        f.close()

    def generate(self, cfg_dict, cfg_parse):
        self._initialize(cfg_dict, cfg_parse)

        self._initialize_core()

        self._gen_core_imports()

        self._gen_core_main_class()
        self._gen_core_main_class__init__()
        self._gen_core_main_class__initialize_topics()
        self._gen_core_main_class__initialize_commands()
        self._gen_core_main_class__initialize_msg_types()

        self._finalize()

    # ##################################################
    # GEN EXTRA

    def _gen_core_imports(self):
        payload = [
            "from broker import RedisMiddleware",
            self._nl,
        ]

        f = open(self._filename, "a")
        f.writelines(payload)
        f.close()

    def _finalize(self):
        print("finalize >   ros > " + self._filename)
        os.system("black -q " + self._filename)

    # ##################################################
    # GEN CORE MAIN CLASS

    def _gen_core_main_class(self):
        payload = [
            "class " + self._gen_name_k.capitalize() + ":" + self._nl,
        ]

        f = open(self._filename, "a")
        f.writelines(payload)
        f.close()

    def _gen_core_main_class__init__(self):
        payload = [
            self._tab + "def __init__(self):" + self._nl,
            self._2tab + "self.broker = RedisMiddleware()" + self._nl,
            self._2tab + "self.topics = self.__Topics()" + self._nl,
            self._2tab + "self.commands = self.__Commands()" + self._nl,
            self._2tab + "self.types = self.__Types()" + self._nl,
            self._nl,
        ]

        f = open(self._filename, "a")
        f.writelines(payload)
        f.close()

    def _gen_core_main_class__initialize_topics(self):
        payload = [
            self._tab + "class __Topics:" + self._nl,
            self._2tab + "def __init__(self):" + self._nl,
        ]
        for sensor in self._gen_vector_sensors:
            payload.append(
                self._3tab
                + "self."
                + sensor
                + ' = "'
                + self._cfg_dict[self._gen_name_k][self._gen_sensors_k][sensor]["topic"]
                + '"'
                + self._nl
            )
        for actuator in self._gen_vector_actuators:
            payload.append(
                self._3tab
                + "self."
                + actuator
                + ' = "'
                + self._cfg_dict[self._gen_name_k][self._gen_actuators_k][actuator][
                    "topic"
                ]
                + '"'
                + self._nl
            )
        payload.append(self._nl)

        f = open(self._filename, "a")
        f.writelines(payload)
        f.close()

    def _gen_core_main_class__initialize_commands(self):
        payload = [
            self._tab + "class __Commands:" + self._nl,
            self._2tab + "def __init__(self):" + self._nl,
        ]
        for actuator in self._gen_vector_actuators:
            payload.append(
                self._3tab
                + "self."
                + actuator
                + " = self.__"
                + actuator.capitalize()
                + "Commands()"
                + self._nl
            )
            for command in self._cfg_dict[self._gen_name_k][self._gen_actuators_k][
                actuator
            ]["commands"]:
                payload.append(
                    self._2tab
                    + "class __"
                    + actuator.capitalize()
                    + "Commands:"
                    + self._nl
                    + self._3tab
                    + "def __init__(self):"
                    + self._nl
                    + self._4tab
                    + "self."
                    + command
                    + ' = "'
                    + command
                    + '"'
                    + self._nl,
                )

        f = open(self._filename, "a")
        f.writelines(payload)
        f.close()

    def _gen_core_main_class__initialize_msg_types(self):
        payload = [
            self._tab + "class __Types:" + self._nl,
            self._2tab + "def __init__(self):" + self._nl,
            self._3tab + 'self.twist = "twist"' + self._nl,
        ]

        f = open(self._filename, "a")
        f.writelines(payload)
        f.close()
