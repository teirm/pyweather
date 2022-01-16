"""
PyWeather display functionality.
"""

def print_weather(weather: list):
    """
    Print the weather as a table to stdout.

    Args:
        weather: list of lists containing weather information
    """

    if not weather:
        print('No weather information to display.')
        return

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
