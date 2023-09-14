"""
Dash app entry point

To launch the app, run

> python app.py

Dash documentation: https://dash.plot.ly/
"""
import os
from dash import Input, Output, State, ClientsideFunction, html, dcc, Dash


# -----------App definition-----------------------
app = Dash(
    __name__
)
app.title = 'Testing title'
server = app.server

app.layout = html.Div([
    html.H1(children=app.title, className="title"),
    html.H3("testing"),
    html.Button("hello button")
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
    app.run_server(debug=False, port="8080")