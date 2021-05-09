def parseArgs():
    return sys.argv[1:]


def main():
    yml_args = parseArgs()
    rcp = Rcp()
    for yml_arg in yml_args:
        yml_src = rcp.parser.syntax.yaml_parse_file(yml_arg)
        cfg_dict = rcp.parser.syntax.yaml_to_dict(yml_src)
        rcp.parser.structure.cfg_validate(cfg_dict)


if __name__ == "__main__":
    from librcp.core.rcp import Rcp
    import sys

    main()
