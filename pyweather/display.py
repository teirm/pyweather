"""
PyWeather display functionality.
"""

def print_weather(weather: list):
    """
    Print the weather as a table to stdout.

    Args:
        weather: list of lists containing weather information
    """
    if len(weather) == 1:
        print('No weather information to display.')
        return

    column_widths = get_column_widths(weather)

    print(*[f'{element : <{column_widths[idx]+3}}'
          for idx, element in enumerate(weather[0])], sep='|')
    print('-' * (sum(column_widths) + 3*len(column_widths)))

    for row in weather[1:]:
        print(*[f'{element : <{column_widths[idx]+3}}'
              for idx, element in enumerate(row)], sep='|')

def get_column_widths(table_data : list) -> list:
    """
    Get the maximum length for each column.

    Args:
        table_data: data for table

    Return:
        list of lengths
    """
    widths = [0] * len(table_data[0])
    for row in table_data:
        if len(row) != len(widths):
            raise ValueError
        for idx, element in enumerate(row):
            widths[idx] = max(widths[idx], len(str(element)))
    return widths
