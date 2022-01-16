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

    column_widths = get_column_widths([weather])
    header = []
    rows = []
    for key, value in weather.items():
        header.append(f'{key : <{column_widths[key]+3}}')
        rows.append(f'{value:  <{column_widths[key]+3}}')
    print(header, sep='|')
    print(rows, sep='|')


def show_weather_alerts(alerts: dict):
    """
    Display current weather alerts on stdout.

    Args:
        alerts: dictionary containing alerts
    """
    if not alerts:
        print('No weather alerts.')

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
