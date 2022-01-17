"""
Pyweather main entry point.
"""

import sys
from pyweather import parser
from pyweather import core
from pyweather import display

def main():
    """Main entry point for pyweather"""
    arg_parser = parser.get_parser()
    args = arg_parser.parse_args(sys.argv[1:])

    if args.subparser_name == 'weather':
        weather = core.current_weather(args.city)
    elif args.subparser_name == 'forecast':
        weather = core.forecast_weather(args.city, args.days)
    elif args.subparser_name == 'alerts':
        weather = core.current_weather_alerts(args.city)
    else:
        arg_parser.print_help(sys.stderr)
        sys.exit(-1)

    display.print_weather(weather)
