"""
Pyweather main entry point.
"""

import sys
from pyweather import parser
from pyweather import core
from pyweather import display
from pyweather import config

def main():
    """Main entry point for pyweather"""
    arg_parser = parser.get_parser()
    args = arg_parser.parse_args(sys.argv[1:])

    pyweather_cfg = config.get_config()

    try:
        api_key = pyweather_cfg['api_key']
    except KeyError:
        print('Configuration file does not define api key.')
        sys.exit(1)

    if args.subparser_name == 'weather':
        weather = core.current_weather(args.city, api_key)
    elif args.subparser_name == 'forecast':
        weather = core.forecast_weather(args.city, args.days, api_key)
    elif args.subparser_name == 'alerts':
        weather = core.current_weather_alerts(args.city, api_key)
    else:
        arg_parser.print_help(sys.stderr)
        sys.exit(1)

    display.print_weather(weather)
