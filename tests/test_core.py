"""
PyWeather core tests.
"""

import unittest
import datetime
from unittest.mock import patch

import requests

from .context import pyweather
from .fixtures import test_data

class CoreTestSuite(unittest.TestCase):
    """Core Test Suite."""
    @patch('pyweather.core.make_api_request')
    def test_current_weather(self, mock_api_request):
        """
        Test for current weather.
        """
        mock_api_request.return_value = test_data.current_weather
        weather = pyweather.core.current_weather('London', test_data.API_KEY)
        self.assertIsInstance(weather, list)
        self.assertTrue(len(weather))
        expected_result = [
                           ['location', 'condition', 'last_updated', 'temp_c'],
                           [test_data.current_weather['location']['name'],
                           test_data.current_weather['current']['condition']['text'],
                           test_data.current_weather['current']['last_updated'],
                           test_data.current_weather['current']['temp_c']]
        ]
        self.assertEqual(len(expected_result), len(weather))
        for actual, expected in zip(weather, expected_result):
            self.assertEqual(actual, expected)

    @patch('requests.get')
    def test_current_weather_error(self, mock_requests):
        """
        Test error case for current weather.
        """
        mock_requests.side_effect = requests.RequestException
        weather = pyweather.core.current_weather('London', test_data.API_KEY)
        self.assertEqual(weather, [])

    @patch('requests.Response.json')
    def test_current_weather_api_error(self, mock_requests):
        """
        Test web api error for current weather.
        """
        mock_requests.return_value = {'error': {'code': 1002,
                                                'message': 'API key is invalid or not provided.'}
                                      }
        weather = pyweather.core.current_weather('London', test_data.API_KEY)
        self.assertEqual(weather, [])

    @patch('pyweather.core.make_api_request')
    def test_forecast(self, mock_api_request):
        """
        Test weather forecast.
        """
        mock_api_request.return_value = test_data.forecast
        weather = pyweather.core.forecast_weather('London', 2, test_data.API_KEY)
        self.assertIsInstance(weather, list)
        self.assertTrue(len(weather))

        expected_header = ['date', 'maxtemp (c)', 'mintemp (c)', 'chance of rain', 'condition']
        self.assertIsInstance(weather[0], list)
        self.assertEqual(weather[0], expected_header)

        expected_instances = [str, (int, float), (int, float), (int, float), str]
        for row in weather[1:]:
            self.assertIsInstance(row, list)
            self.assertEqual(len(row), len(expected_header))
            for element, instance in zip(row, expected_instances):
                self.assertIsInstance(element, instance)

            date_format = '%Y-%m-%d'
            self.assertTrue(datetime.datetime.strptime(row[0], date_format))

    @patch('requests.get')
    def test_forecast_error(self, mock_requests):
        """
        Test error case for forecast.
        """
        mock_requests.side_effect = requests.RequestException
        weather = pyweather.core.forecast_weather('London', 10, test_data.API_KEY)
        self.assertEqual(weather, [])

    @patch('requests.Response.json')
    def test_forecast_weather_api_error(self, mock_requests):
        """
        Test web api error for forecast weather.
        """
        mock_requests.return_value = {'error': {'code': 1002,
                                                'message': 'API key is invalid or not provided.'}
                                      }
        weather = pyweather.core.forecast_weather('London', 10, test_data.API_KEY)
        self.assertEqual(weather, [])

    @patch('pyweather.core.make_api_request')
    def test_weather_alerts(self, mock_api_request):
        """
        Test getting weather alerts.
        """
        mock_api_request.return_value = test_data.current_alerts
        weather_alerts = pyweather.core.current_weather_alerts('Montreal', test_data.API_KEY)
        self.assertIsInstance(weather_alerts, list)
        self.assertTrue(len(weather_alerts))


        header = ['headline', 'areas', 'event', 'effective', 'expires']
        self.assertIsInstance(weather_alerts[0], list)
        self.assertEqual(weather_alerts[0], header)

        for row in weather_alerts[1:]:
            self.assertIsInstance(row, list)
            for element in row:
                self.assertIsInstance(element, str)

    @patch('requests.get')
    def test_weather_alerts_error(self, mock_requests):
        """
        Test error case for alerts.
        """
        mock_requests.side_effect = requests.RequestException
        weather = pyweather.core.current_weather_alerts('London', test_data.API_KEY)
        self.assertEqual(weather, [])

    @patch('requests.Response.json')
    def test_weather_alerts_api_error(self, mock_requests):
        """
        Test web api error for alerts.
        """
        mock_requests.return_value = {'error': {'code': 1002,
                                                'message': 'API key is invalid or not provided.'}
                                      }
        weather = pyweather.core.current_weather_alerts('London', test_data.API_KEY)
        self.assertEqual(weather, [])
