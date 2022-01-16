"""
Pyweather main entry point.
"""

import sys
from pyweather import parser
from pyweather import core
from pyweather import display

def main():
    """Main entry point for pyweather"""
    args = parser.parse_args(sys.argv)

    if args.subparser_name == 'weather':
        weather = core.current_weather(args.city)
    elif args.subparser_name == 'forecast':
        weather = core.forecast_weather(args.city, args.days)
    else:
        weather = core.current_weather_alerts(args.city)

    display.print_weather(weather)
