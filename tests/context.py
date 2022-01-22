"""
Test context for imports.
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pyweather
from pyweather import parser
from pyweather import display
