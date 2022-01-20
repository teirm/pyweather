"""
PyWeather core functionality for request handling.
"""

import requests

def current_weather(city: str, api_key: str) -> list:
    """
    Get current weather for given city.

    Args:
        city:   city for which to get current weather

    Return:
        dictionary of weather information
        empty dict on error
    """
    endpoint = 'current.json'
    request_info = {'q': city, 'aqi': 'no', 'key': api_key}
    weather =  make_api_request(endpoint, request_info)
    if weather:
        rows = [
                ['location', 'condition', 'last_updated', 'temp_c'],
                [weather['location'],
                 weather['current']['condition']['text'],
                 weather['current']['last_updated'],
                 weather['current']['temp_c']]
        ]
        return rows
    return []

def forecast_weather(city: str, days: int, api_key: str) -> list:
    """
    Get the n-days forecast for the given city.

    Args:
        city: cith for which to get forecast

    Return:
        dictionary of forecast information
    """
    endpoint = 'forecast.json'
    request_info = {'q': city, 'days': days, 'alerts': 'no', 'key': api_key}
    weather = make_api_request(endpoint, request_info)
    if weather:
        rows = [['date', 'maxtemp (c)', 'mintemp (c)', 'chance of rain', 'condition']]
        for day in weather['forecast']['forecastday']:
            rows.append([day['date'],
                         day['day']['maxtemp_c'],
                         day['day']['mintemp_c'],
                         day['day']['daily_chance_of_rain'],
                         day['day']['condition']['text']])
        return rows
    return []

def current_weather_alerts(city: str, api_key: str) -> list:
    """
    Get current weather alerts for given city.

    Args:
        city:   city for which to get alert information

    Return:
        list of weather alerts
    """
    endpoint = 'forecast.json'
    request_info = {'q': city, 'days': 1, 'alerts': 'yes', 'key': api_key}
    weather = make_api_request(endpoint, request_info)
    if weather:
        header = ['headline', 'areas', 'event', 'effective', 'expires']
        rows = [header]
        for alert in weather['alerts']['alert']:
            rows.append([alert[key] for key in header])
        return rows
    return []

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
        request_json = request.json()
        if 'error' in request_json.keys():
            print(f'Error: {request_json["error"]["message"]}')
            return {}
    except (requests.RequestException, requests.ConnectionError,
            requests.HTTPError, requests.URLRequired,
            requests.exceptions.InvalidJSONError) as err:
        print(err)
    return {}
