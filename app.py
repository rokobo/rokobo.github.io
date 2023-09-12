"""
Dash app entry point

To launch the app, run

> python app.py

Dash documentation: https://dash.plot.ly/
"""
import os
import numpy as np

import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_table
import dash_html_components as html
import dash_core_components as dcc


if 'DEBUG' in os.environ:
    debug = os.environ['DEBUG'] == 'True'
    print(f"DEBUG environment variable present, DEBUG set to {debug}")
else:
    print("No DEBUG environment variable: defaulting to debug mode")
    debug = True


# -----------App definition-----------------------
app = dash.Dash(
    __name__,
    external_stylesheets=[],
)
app.title = 'Covid-19: confirmed cases and extrapolation'
server = app.server

app.layout = html.Div([
    html.H1(children=app.title, className="title"),
    html.H3("testing")
])

# ---------------------- Callbacks ---------------------------------
# Callbacks are all client-side (https://dash.plot.ly/performance)
# in order to transform the app into static html pages
# javascript functions are defined in assets/callbacks.js

# app.clientside_callback(
#     ClientsideFunction(
#         namespace='clientside3',
#         function_name='update_table'
#     ),
#     output=Output('table', 'selected_rows'),
#     inputs=[
#         Input('map', 'clickData'),
#         Input('map', 'selectedData'),
#         Input('table', 'data')
#         ],
#     state=[State('table', 'selected_rows'),
#            State('store', 'data')],
#     )


# app.clientside_callback(
#     ClientsideFunction(
#         namespace='clientside',
#         function_name='update_store_data'
#     ),
#     output=Output('plot', 'figure'),
#     inputs=[
#         Input('table', "data"),
#         Input('table', "selected_rows"),
#         Input('radio-cases', 'value'),
#         Input('log-lin', 'value')],
#     state=[State('store', 'data')],
#     )



if __name__ == '__main__':
    app.run_server(debug=debug)
