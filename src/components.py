"""Functions for building components."""
# pylint: disable=import-error
from os import listdir
from os.path import join, abspath, dirname
import yaml
from dash import html, Input, Output, clientside_callback, ClientsideFunction
import dash_bootstrap_components as dbc


DIRECTORY = join(dirname(dirname(abspath(__file__))), "assets/certificates")
files = [f for f in listdir(DIRECTORY) if f.endswith((".png", ".jpg"))]
with open(join(DIRECTORY, "categories.yml"), "r", encoding="utf-8") as config:
    category = yaml.safe_load(config)


def certificates() -> dbc.Row:
    """
    Generates certificate cards and modals for certificates page.

    Returns:
        dbc.Row: Row with all cards and modals.
    """
    components = []
    for file in files[::-1]:
        body = [dbc.Badge(number, pill=True) for number in category[file[:3]]]
        body.append(html.P(file[4:-4], className="card-text"))
        card = dbc.Card([
            html.Div(dbc.CardImg(
                src=join(DIRECTORY, file), top=True
            ), id=f"card-image-{file[:3]}"),
            dbc.Modal([
                dbc.ModalBody([html.Img(
                    src=join(DIRECTORY, file),
                    className="modal-image"
                )], class_name="certificate-modal-body"),
            ], id=f"card-modal-{file[:3]}", centered=True, size="xl"),
            dbc.CardBody(body, class_name="certificate-card-body"),
        ], class_name="certificate-card")
        components.append(card)
    component = dbc.Row(components, justify="evenly")
    return component


clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='certificate_click'
    ),
    [Output(f'card-modal-{str(number).zfill(3)}', 'is_open')
        for number in range(1, len(files) + 1)],
    [Input(f'card-image-{str(number).zfill(3)}', 'n_clicks')
        for number in range(1, len(files) + 1)],
    prevent_initial_call=True
)
