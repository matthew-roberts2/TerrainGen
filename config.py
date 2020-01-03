import configparser
import os.path

CONFIG_DIR = "./"
CONFIG_NAME = "config.ini"

CONFIG_FULL = f"{CONFIG_DIR}{CONFIG_NAME}"


def set_defaults(config):
    config['Basic World'] = {
        "xdim": "50",
        "ydim": "50",
    }


def load():
    config = configparser.ConfigParser()
    print("Checking for config file...")
    if not os.path.isfile(CONFIG_FULL):
        with open(CONFIG_FULL, 'w') as conf:
            print("Config does not exist. Loading config defaults...")
            set_defaults(config)
            print("Writing config to file.")
            config.write(conf)
    else:
        print("Config already exists. Reading values...")
        config.read(CONFIG_FULL)

    try:
        x = config['Basic World']["xdim"]
        y = config['Basic World']["ydim"]
    except KeyError:
        print("Malformed config detected.")
        os.remove(CONFIG_FULL)
        print("Reloading...")
        load()
        return

    print("X dimension: " + str(x))
    print("Y dimension: " + str(y))


