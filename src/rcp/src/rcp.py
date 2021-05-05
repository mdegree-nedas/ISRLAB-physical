from mod.parser import parse_robot_structure


def main():
    file_name = "../yml/rcp_cfg.yml"
    obj = parse_robot_structure(file_name)
    print(obj)


if __name__ == '__main__':
    main()
