import configparser
import os

def get_config(key, section=None):
    config = configparser.ConfigParser()
    config_file = os.path.join(os.path.dirname(__file__), "config.ini")

    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Config file not found at {config_file}")

    config.read(config_file)

    if section:
        if section in config:
            if key in config[section]:
                return config[section][key]
            else:
                raise KeyError(f"Key '{key}' not found in section '{section}'")
        else:
            raise KeyError(f"Section '{section}' not found in config.ini")
    else:
        # Search all sections
        for sec in config.sections():
            if key in config[sec]:
                return config[sec][key]
        raise KeyError(f"Key '{key}' not found in any section of config.ini")
