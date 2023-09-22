"""Functions for building components."""
# pylint: disable=import-error
from os import listdir
from os.path import join, abspath, dirname, exists
import json
import yaml
from dash import html, Input, Output, clientside_callback, ClientsideFunction
import dash_bootstrap_components as dbc
from helper_functions import short_display_num

HOME = dirname(dirname(abspath(__file__)))
ASSETS_CERTIFICATES = "assets/certificates"
ASSET_DIR = join(HOME, ASSETS_CERTIFICATES)
ASSETS_REPOS = "assets/repos"
REPO_DIR = join(HOME, ASSETS_REPOS)
CERTIFICATES = [f for f in listdir(ASSET_DIR) if f.endswith((".png", ".jpg"))]
with open(join(ASSET_DIR, "tags.yml"), "r", encoding="utf-8") as config:
    TAGS = yaml.safe_load(config)


def certificates() -> dbc.Row:
    """
    Generates certificate cards and modals for certificates page.

    Returns:
        dbc.Row: Row with all cards and modals.
    """
    components = []
    for file in CERTIFICATES[::-1]:
        body = [dbc.Badge(number, pill=True) for number in TAGS[file[:3]]]
        body.append(html.P(file[4:-4], className="card-text"))
        card = dbc.Card([
            html.Div(dbc.CardImg(
                src=join(ASSETS_CERTIFICATES, file), top=True
            ), id=f"card-image-{file[:3]}"),
            dbc.Modal([
                dbc.ModalBody([html.Img(
                    src=join(ASSETS_CERTIFICATES, file),
                    className="modal-image"
                )], class_name="certificate-modal-body"),
            ], id=f"card-modal-{file[:3]}", centered=True, size="xl"),
            dbc.CardBody(body, class_name="certificate-card-body"),
        ], class_name="certificate-card")
        components.append(card)
    component = dbc.Row(
        components, justify="evenly",
        style={"margin-top": "15px"}
    )
    return component


clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='certificate_click'
    ),
    [Output(f'card-modal-{str(number).zfill(3)}', 'is_open')
        for number in range(1, len(CERTIFICATES) + 1)],
    [Input(f'card-image-{str(number).zfill(3)}', 'n_clicks')
        for number in range(1, len(CERTIFICATES) + 1)],
    prevent_initial_call=True
)


def projects() -> dbc.Row:
    """
    Generates project cards for projects page.

    Returns:
        dbc.Row: Row with all project cards.
    """
    components = []
    with open(join(REPO_DIR, "repos.json"), "r", encoding="utf-8") as file:
        repos = json.load(file)

    for _, url, description, languages in repos:
        tags = [
            dbc.Badge(
                f"{lang} {short_display_num(count)}", pill=True,
                color="rgba(233, 233, 222, 0.15)"  #TODO language colorcode
            )
            for lang, count in languages.items()
        ]
        repo_name = url.split('/')[-1]

        image_path = join(REPO_DIR, f"{repo_name}.png")
        if exists(image_path):
            image_path = join(ASSETS_REPOS, f"{repo_name}.png")
        else:
            image_path = join(ASSETS_REPOS, "_.png")

        body = [
            html.H5(
                html.A(
                    repo_name, href=url,
                    target="_blank", style={"color": "white"}
                ), className="project-card-title",
                id=f"project-card-title-{repo_name}"
            ),
            dbc.Col(
                html.P(f"{description}", className="card-text"),
                class_name="project-description"
            ),
            dbc.Col(
                tags, class_name="project-languages",
                id=f"project-tags-column-{repo_name}"
            )
        ]

        card = dbc.Card([
            html.Div(dbc.CardImg(
                src=image_path, top=True, class_name="project-card-image"
            )),
            dbc.CardBody(body, class_name="project-card-body"),
            dbc.Tooltip(
                repo_name,
                target=f"project-card-title-{repo_name}"
            ),
        ], class_name="project-card")
        components.append(card)

    component = dbc.Row(
        components, justify="evenly", class_name="project-row")
    return component
