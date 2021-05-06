from core.parser.parser import Parser


def main():
    robot_parser = Parser()

    # this will be passed by command line args
    files = []
    files.append("./test/rcp_cfg_test.yml")

    for robot_file in files:
        robot = robot_parser.syntax.parse_yaml_file(robot_file)
        if robot_parser.structure.check(robot):
            # print structure only if it is valid
            print(robot)


if __name__ == "__main__":
    main()
