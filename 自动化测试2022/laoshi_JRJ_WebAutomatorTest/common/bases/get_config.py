import os
import configparser
import sys

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


def read_config(config_file_path, field, key):
    cf = configparser.ConfigParser()
    try:
        cf.read(config_file_path, encoding='utf-8')
        if sys.platform == 'win32':
            result = cf.get(field, key).replace('base_dir', str(BASE_DIR)).replace('/', '\\')
        else:
            result = cf.get(field, key).replace('base_dir', str(BASE_DIR))
    except Exception as e:
        print(e)
        sys.exit(1)
    return result

