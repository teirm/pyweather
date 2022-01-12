"""
PyWeather core tests.
"""

import unittest
from unittest.mock import patch

import requests

from .context import pyweather
from .fixtures import test_data

class CoreTestSuite(unittest.TestCase):
    """Core Test Suit."""
    @patch('pyweather.core.make_api_request')
    def test_current_weather(self, mock_api_request):
        """
        Test for current weather.
        """
        mock_api_request.return_value = test_data.current_weather
        weather = pyweather.core.current_weather('London')
        self.assertIsInstance(weather, dict)
        self.assertTrue(len(weather))

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
        weather = pyweather.core.current_weather('London')
        self.assertEqual(weather, {})

    @patch('pyweather.core.make_api_request')
    def test_forecast(self, mock_api_request):
        """
        Test weather forecast.
        """
        mock_api_request.return_value = test_data.forecast
        weather = pyweather.core.forecast_weather('London', 2)
        self.assertIsInstance(weather, list)
        self.assertTrue(len(weather))

        expected_element_keys = ['date', 'day']
        for element in weather:
            self.assertIsInstance(element, dict)
            for key in expected_element_keys:
                self.assertIn(key, element.keys())

            self.assertIsInstance(element['date'], str)
            self.assertIsInstance(element['day'], dict)
            self.assertTrue(len(element['day']))


    @patch('requests.get')
    def test_forecast_error(self, mock_requests):
        """
        Test error case for forecast.
        """
        mock_requests.side_effect = requests.RequestException
        weather = pyweather.core.forecast_weather('London', 10)
        self.assertEqual(weather, [])

    @patch('pyweather.core.make_api_request')
    def test_weather_alerts(self, mock_api_request):
        """
        Test getting weather alerts.
        """
        mock_api_request.return_value = test_data.current_alerts
        weather_alerts = pyweather.core.current_weather_alerts('Montreal')
        self.assertIsInstance(weather_alerts, dict)
        self.assertTrue(len(weather_alerts))
        self.assertIn("alert", weather_alerts.keys())

        self.assertIsInstance(weather_alerts["alert"], list)
        alerts_list = weather_alerts["alert"]
        self.assertTrue(len(alerts_list))
        key_properties = {"headline": str,
                          "msgtype" : str,
                          "severity": str,
                          "areas": str,
                          "category": str,
                          "certainty": str,
                          "desc": str}
        for item in alerts_list:
            self.assertIsInstance(item, dict)
            item_keys = item.keys()
            for key, prop in key_properties.items():
                self.assertIn(key, item_keys)
                self.assertIsInstance(item[key], prop)



    @patch('requests.get')
    def test_weather_alerts_error(self, mock_requests):
        """
        Test error case for forecast.
        """
        mock_requests.side_effect = requests.RequestException
        weather = pyweather.core.current_weather_alerts('London')
        self.assertEqual(weather, {})
