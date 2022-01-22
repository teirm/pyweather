"""
PyWeather parser tests.
"""

import unittest

from .context import parser

class ParserTestSuite(unittest.TestCase):
    """Parser Test Suite."""

    def test_weather(self):
        """
        Test case for current weather weather arguments.
        """
        prsr = parser.get_parser()

        city = 'London'
        args = prsr.parse_args(['weather', '--city', city])
        self.assertTrue(hasattr(args, 'city'))
        self.assertEqual(args.city, city)

    def test_forecast(self):
        """
        Test case for forecast.
        """
        prsr = parser.get_parser()

        city = 'London'
        days = '5'
        args = prsr.parse_args(['forecast', '--city', city, '--days', days])

        self.assertTrue(hasattr(args, 'city'))
        self.assertEqual(args.city, city)

        self.assertTrue(hasattr(args, 'days'))
        self.assertEqual(args.days, 5)

    def test_alerts(self):
        """
        Test case for forecast.
        """
        prsr = parser.get_parser()

        city = 'London'
        args = prsr.parse_args(['alerts', '--city', city])

        self.assertTrue(hasattr(args, 'city'))
        self.assertEqual(args.city, city)
