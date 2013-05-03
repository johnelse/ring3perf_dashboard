import getpass
import imp
import os
import sys

config_file = ".ring3perf/config.py"

expected_keys = [
    "jira_url",
    "jira_username",
    "jira_password",
    "server_ip"
]

def get_config():
    user = getpass.getuser()
    home_dir = os.path.expanduser("~" + user)
    config_path = os.path.join(home_dir, config_file)
    try:
        config = imp.load_source("config", config_path)
        for key in expected_keys:
            config.__getattribute__(key)
        return config
    except IOError:
        raise RuntimeError("No config file found at %s" % config_path)
    except SyntaxError:
        raise RuntimeError("Could not parse config file")
    except AttributeError as e:
        raise RuntimeError("Missing config key: %s" % e.args[0])
