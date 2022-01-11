"""
PyWeather core tests.
"""

import unittest
from unittest.mock import patch

import requests

from pyweather import core
from .fixtures import test_data

class CoreTestSuite(unittest.TestCase):
    """Core Test Suit."""
    @patch('pyweather.core.make_api_request')
    def test_current_weather(self, mock_api_request):
        """
        Test for current weather.
        """
        mock_api_request.return_value = test_data.current_weather
        weather = core.current_weather('London')
        self.assertIsInstance(weather, dict)
        self.assertTrue(len(weather) != 0)

        expected_result = {'location': test_data.current_weather['location'],
                           'condition': test_data.current_weather['current']['condition']['text'],
                           'updated': test_data.current_weather['current']['last_updated'],
                           'temp': test_data.current_weather['current']['temp_c']}
        for key, value in expected_result.items():
            self.assertIn(key, weather.keys())
            self.assertEqual(value, weather[key])


    @patch('requests.get')
    def test_current_weather_error(self, mock_requests):
        """
        Test error case for current weather.
        """
        mock_requests.side_effect = requests.RequestException
        weather = core.current_weather('London')
        self.assertEqual(weather, {})

    @patch('requests.get')
    def test_forecast(self, mock_requests):
        """
        Test weather forecast.
        """

    @patch('requests.get')
    def test_forecast_error(self, mock_requests):
        """
        Test error case for forecast.
        """
        mock_requests.side_effect = requests.RequestException
        weather = core.forecast_weather('London', 10)
        self.assertEqual(weather, {})

    @patch('requests.get')
    def test_weather_alerts(self, mock_requests):
        """
        Test getting weather alerts.
        """

    @patch('requests.get')
    def test_weather_alerts_error(self, mock_requests):
        """
        Test error case for forecast.
        """
        mock_requests.side_effect = requests.RequestException
        weather = core.current_weather_alerts('London')
        self.assertEqual(weather, {})
