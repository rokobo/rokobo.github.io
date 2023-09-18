"""Certificates page layout."""
# pylint: disable=wrong-import-position, import-error
# flake8: noqa: E402
import os
import sys
import dash
from dash import html

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import navigation
from components import certificates

dash.register_page(__name__)

layout = html.Div([
    navigation.layout,
    certificates()
])
