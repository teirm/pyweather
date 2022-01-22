"""
PyWeather display tests.
"""

import unittest

from .context import display

class DisplayTestSuite(unittest.TestCase):
    """Display Test Suite."""
    def test_column_widths(self):
        """
        Test for column widths.
        """
        data = [['Homura', 'did', 'right'],
                ['Mami', 'got', 'nommed'],
                ['Madoka', 'is', 'OP']]

        col_widths = display.get_column_widths(data)
        self.assertEqual(col_widths, [6, 3, 6])

    def test_column_widths_bad_data(self):
        """
        Test for column widths with bad data.
        """
        data = [['a', 'b'],
                ['c', 'd', 'x']]
        with self.assertRaises(ValueError):
            display.get_column_widths(data)
