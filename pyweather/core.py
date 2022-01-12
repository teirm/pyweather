"""
PyWeather core functionality for request handling.
"""

import requests

def current_weather(city: str) -> dict:
    """
    Get current weather for given city.

    Args:
        city:   city for which to get current weather

    Return:
        dictionary of weather information
        empty dict on error
    """
    endpoint = 'current.json'
    request_info = {'q': city, 'aqi': 'no'}
    weather =  make_api_request(endpoint, request_info)
    if weather:
        return {'location': weather['location'],
                'condition': weather['current']['condition']['text'],
                'updated': weather['current']['last_updated'],
                'temp': weather['current']['temp_c']}
    return {}

def forecast_weather(city: str, days: int) -> list:
    """
    Get the n-days forecast for the given city.

    Args:
        city: cith for which to get forecast

    Return:
        dictionary of forecast information
    """
    endpoint = 'forecast.json'
    request_info = {'q': city, 'days': days, 'alerts': 'no'}
    weather = make_api_request(endpoint, request_info)
    if weather:
        return [{'date': d['date'], 'day': d['day']} for d in weather['forecast']['forecastday']]
    return []

def current_weather_alerts(city: str) -> dict:
    """
    Get current weather alerts for given city.

    Args:
        city:   city for which to get alert information

    Return:
        dictionary of weather information
    """
    endpoint = 'forecast.json'
    request_info = {'q': city, 'days': 1, 'alerts': 'yes'}
    weather = make_api_request(endpoint, request_info)
    if weather:
        return weather['alerts']
    return {}

def make_api_request(api_endpoint: str, request_info: dict) -> dict:
    """
    Make a weatherapi.com request.

    Args:
        api_endpoint: endpoint for REST api
        request_info: information for the specific request

    Return:
        dictionary of weather information
    """
    api_url = "http://api.weatherapi.com/v1/"
    try:
        request = requests.get(api_url + api_endpoint, request_info)
        return request.json()
    except (requests.RequestException, requests.ConnectionError,
            requests.HTTPError, requests.URLRequired,
            requests.exceptions.InvalidJSONError) as err:
        print(err)
    return {}
