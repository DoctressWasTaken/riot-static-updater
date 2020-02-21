import json

config_file = "config.json"


def load_file(name):
    """Load the separate json file for all
    variables that have to be loaded externally.
    """
    with open(name, "r") as config:
        return json.loads(config.read())

def load(key, default):
    """Try to load value from config file.

    If the key does not exist takes the default instead.
    """
    global DATA
    if key in DATA:
        return DATA[key]
    else:
        return default

def update(var, val):
    """Update a variable to a file."""
    global DATA
    setattr(DATA, var, val)
    with open(config_file, "w", encoding="utf-8") as config:
        json.dumps(DATA, config, indent=2, sort_keys=True)


DATA = load_file(config_file)


# LINKS
VERSION = load("VERSION", 
        "https://ddragon.leagueoflegends.com/api/versions.json")

TAIL = load("TAIL", 
        "https://ddragon.leagueoflegends.com/cdn/dragontail-%s.tgz")

LATEST = load("LATEST",
        None)
JENKINS_HOOK = load("JENKINS_HOOK", None)
