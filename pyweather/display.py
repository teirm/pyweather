"""
PyWeather display functionality.
"""

def show_current_weather(weather : list):
    """
    Display current weather on stdout.

    Args:
        weather: dictionary containing the current weather
    """
    if not weather:
        print('No weather information.')
        return
    print_weather(weather)

def show_weather_alerts(alerts: list):
    """
    Display current weather alerts on stdout.

    Args:
        alerts: dictionary containing alerts
    """
    if not alerts:
        print('No weather alerts.')
    print_weather(alerts)

def show_weather_forecast(forecast: list):
    """
    Display the weather forecast on stdout.

    Args:
        alerts: list of forecast information.
    """
    if not forecast:
        print('No forecast information.')
    print_weather(forecast)

def print_weather(weather: list):
    """
    Print the weather as a table to stdout.

    Args:
        weather: list of lists containing weather information
    """
    column_widths = get_column_widths(weather)
    for row in weather:
        print([f'{element : <{column_widths[idx]+3}}'
              for element, idx in enumerate(row)], sep='|')

def get_column_widths(table_data : list) -> list:
    """
    Get the maximum length for each k,y pair.

    Args:
        table_data: data for table

    Return:
        list of lengths
    """
    widths = [0] * len(table_data[0])
    for row in table_data:
        for idx, element in enumerate(row):
            widths[idx] = max(widths[idx], len(element))
    return widths
