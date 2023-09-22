"""Navigation bar component layout."""
import dash_bootstrap_components as dbc
from dash import html

layout = dbc.Row([
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("About", href="/")),
            dbc.NavItem(dbc.NavLink("Certificates", href="/certificates")),
            dbc.NavItem(dbc.NavLink("Projects", href="/projects")),
            dbc.NavItem(dbc.NavLink("Blog", href="/")),
            dbc.NavItem(dbc.NavLink("CV", href="/")),
        ],
        dark=True, fluid=True,
        color="rgb(50, 50, 50)",
        brand=dbc.Container([dbc.Row([
            dbc.Col(html.Img(src="assets/logo.svg", height="30px")),
            dbc.Col(dbc.NavbarBrand("Pedro Kobori")),
        ], class_name="d-flex align-items-center g-2")])
    )
])
