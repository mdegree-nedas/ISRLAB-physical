def parseArgs():
    return sys.argv[1:]


def main():
    yml_args = parseArgs()
    rcp = Rcp()
    for yml_arg in yml_args:
        yml_src = rcp.parser.syntax.yaml_parse_file(yml_arg)
        cfg_dict = rcp.parser.syntax.yaml_to_dict(yml_src)
        cfg_parse = rcp.parser.structure.cfg_validate(cfg_dict)
        rcp.generator.core.generate(cfg_dict, cfg_parse)
        rcp.generator.template.generate(cfg_dict, cfg_parse)
        rcp.generator.interface.generate(cfg_dict, cfg_parse)


if __name__ == "__main__":
    from librcp.core.rcp import Rcp
    import sys

    main()
