from parser import parse_robot_structure


def main():
    file_name = "./test/rcp_cfg_test.yml"
    obj = parse_robot_structure(file_name)
    print(obj)


if __name__ == "__main__":
    main()
