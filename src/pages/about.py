"""About page layout."""
# pylint: disable=wrong-import-position, import-error
# flake8: noqa: E402
import os
import sys
from dash import html

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components import about


layout = html.Div([
    about()
])
