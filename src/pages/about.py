"""About page layout."""
# pylint: disable=wrong-import-position
# flake8: noqa: E402
import os
import sys
import dash_bootstrap_components as dbc
from dash import html

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


urls = {
    "github": "https://github.com/rokobo",
    "linkedin": "https://www.linkedin.com/in/pedrokobori/"
}

layout = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Card(dbc.CardBody([
                html.H1("Hello! 👋 My name is Pedro Kobori",
                        style={"text-align": "start"}),
                html.Br(),
                html.H4("Self-taught developer with a passion for databases, \
                        productivity software, automations and data analysis.",
                        style={"text-align": "start"})
            ]), class_name="about-card")
        ], class_name="d-flex flex-column justify-content-center"),
        dbc.Col([
            dbc.Row(html.A([html.Img(
                src="assets/github.png", className="home-icons"
            )], href=urls["github"], target="_blank")),
            dbc.Row(html.A([html.Img(
                src="assets/linkedin.png", className="home-icons"
            )], href=urls["linkedin"], target="_blank")),
        ], width="auto", class_name="d-flex flex-column \
            justify-content-between align-items-center")
    ], class_name="about-first-row"),
])
