"""
PyWeather config file handling.
"""

import json
import os

def get_config():
    """
    Get configuration file with API key from several known locations.

    Return:
        JSON blob of configuration file.
    """

    config_dirs = [os.curdir,
                   os.path.expanduser('~'),
                  '/etc/pyweather']

    for location in config_dirs:
        config_path = os.path.join(location, 'pyweather.json')
        if os.path.exists(config_path):
            try:
                with open(config_path, encoding='utf-8') as json_fp:
                    return json.load(json_fp)
            except IOError as exp:
                print(f'Unable to open {config_path}: {repr(exp)}.')
                return None
            except json.JSONDecodeError as exp:
                print(f'{config_path} is not valid json {repr(exp)}.')
                return None
    return None
