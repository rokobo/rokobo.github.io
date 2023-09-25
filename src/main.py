"""Personal portfolio using Dash."""
from os.path import abspath, dirname, join, exists
from dash import Dash, dcc, html, Output, Input, clientside_callback, \
    ClientsideFunction
import dash_bootstrap_components as dbc
from pages import about, certificates, navigation, projects, cv


clientside_callback(
    ClientsideFunction(namespace='clientside', function_name='display_page'),
    Output('tabs', 'active_tab'),
    Input('url', 'hash')
)

TITLE = "Pedro Kobori's personal portfolio"
DESCRIPTION = "Projects, certificates, blog, CV and about section."
IMAGE = "https://rokobo.github.io/thumbnail.png"


if __name__ == '__main__':
    app = Dash(
        __name__, assets_folder='../assets',
        title=TITLE,
        external_stylesheets=[dbc.themes.BOOTSTRAP],
        meta_tags=[
            {"property": "og:title", "content": TITLE},
            {"property": "og:description", "content": DESCRIPTION},
            {"property": "og:image", "content": IMAGE},
            {"name": "twitter:title", "content": TITLE},
            {"name": "twitter:description", "content": DESCRIPTION},
            {"name": "twitter:image", "content": IMAGE},
            {"name": "twitter:card", "content": "summary_large_image"},
        ]
    )

    # Tabs were used because they can be clientside, unlike Dash pages.
    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        navigation.layout,
        dbc.Tabs([
            dbc.Tab(about.layout, tab_id="about"),
            dbc.Tab(certificates.layout, tab_id="certificates"),
            dbc.Tab(projects.layout, tab_id="projects"),
            dbc.Tab(cv.layout, tab_id="cv")
        ], id="tabs", active_tab="about")
    ])
    app.server.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    # Run debug mode if desktop.ini is in the main directory
    if exists(join(dirname(dirname(abspath(__file__))), "desktop.ini")):
        app.run_server(
            host="0.0.0.0",
            debug=True,
            port="8020",
            dev_tools_hot_reload=True,
            use_reloader=True
        )
    else:
        app.run_server(port="8080")
