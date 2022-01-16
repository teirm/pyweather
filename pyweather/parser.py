"""
Command line argument parsing.
"""

import argparse

def parse_args(args : list) -> argparse.Namespace:
    """
    Parse command line arguments for pyweather.

    Args:
        args: list of command line arguments to parse

    Return:
        Namespace with arguments parsed
    """
    parser = argparse.ArgumentParser(prog='PyWeather')
    subparsers = parser.add_subparsers(dest='subparser_name')

    weather_parser = subparsers.add_parser('weather',
                                           help='Get the current weather for a city')
    weather_parser.add_argument('--city', required=True, type=str, help='Name of city')

    forecast_parser = subparsers.add_parser('forecast',
                                            help='Get the forecast for a city')
    forecast_parser.add_argument('--city', required=True, type=str, help='Name of city')
    forecast_parser.add_argument('--days', default=3, type=int,
                                 choices=range(1,10), help='Days to forecast')

    alerts_parser = subparsers.add_parser('alerts',
                                          help='Get weather alerts for a city')
    alerts_parser.add_argument('--city', required=True, type=str, help='Name of city')

    return parser.parse_args(args)
