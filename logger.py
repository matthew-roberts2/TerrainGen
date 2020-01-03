import os.path

LOG_DIR = './logs'

def init():
    if not os.path.isdir(LOG_DIR):
        os.mkdir(LOG_DIR)

