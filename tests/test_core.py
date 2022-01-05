"""
PyWeather core tests.
"""

import unittest
from unittest.mock import patch

import requests
import pyweather

class CoreTestSuite(unittest.TestCase):
    """Core Test Suit."""
    @patch('requests.get')
    def test_current_weather(self, mock_requests):
        """
        Test for current weather.
        """

    @patch('requests.get')
    def test_current_weather_error(self, mock_requests):
        """
        Test error case for current weather.
        """
        mock_requests.side_effect = requests.RequestException
        weather = pyweather.current_weather('London')
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
        weather = pyweather.forecast_weather('London', 10)
        self.assertEqual(weather, {})

    @patch('requests.get')
    def test_weather_alerts(self, mock_requests):
        """
        Test getting weather alerts.
        """
        mock_requests.side_effect = requests.RequestException
        weather = pyweather.current_weather_alerts('London')
        self.assertEqual(weather, {})

    @patch('requests.get')
    def test_weather_alerts_error(self, mock_requests):
        """
        Test error case for forecast.
        """
