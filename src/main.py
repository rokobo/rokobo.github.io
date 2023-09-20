"""Personal portfolio using Dash."""
from os.path import abspath, dirname, join, exists
from dash import Dash, dcc, html, Output, Input, clientside_callback, \
    ClientsideFunction
import dash_bootstrap_components as dbc
from pages import about, certificates, navigation


clientside_callback(
    ClientsideFunction(namespace='clientside', function_name='display_page'),
    Output('tabs', 'active_tab'),
    Input('url', 'pathname')
)


if __name__ == '__main__':
    app = Dash(
        __name__, assets_folder='../assets',
        external_stylesheets=[dbc.themes.BOOTSTRAP],
    )

    # Tabs were used because they can be clientside, unlike Dash pages.
    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        navigation.layout,
        dbc.Tabs([
            dbc.Tab(about.layout, tab_id="/"),
            dbc.Tab(certificates.layout, tab_id="/certificates"),
        ], id="tabs", active_tab="/")
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
