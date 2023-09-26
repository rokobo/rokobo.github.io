"""Functions for building components."""
# pylint: disable=import-error
from os import listdir
from os.path import join, abspath, dirname, exists
import json
import yaml
from dash import html, Input, Output, clientside_callback, ClientsideFunction
import dash_bootstrap_components as dbc
from pdf2image import convert_from_path
from helper_functions import short_display_num, get_repos

HOME = dirname(dirname(abspath(__file__)))
CV_PDF = join(HOME, "assets/cv/Pedro Kobori CV.pdf")
CV_PNG = join(HOME, "assets/cv/Pedro Kobori CV.png")
ASSETS_CERTIFICATES = "assets/certificates"
ASSET_DIR = join(HOME, ASSETS_CERTIFICATES)
ASSETS_REPOS = "assets/repos"
REPO_DIR = join(HOME, ASSETS_REPOS)
CERTIFICATES = [f for f in listdir(ASSET_DIR) if f.endswith((".png", ".jpg"))]
CERTIFICATES.sort()
with open(join(ASSET_DIR, "tags.yml"), "r", encoding="utf-8") as config:
    TAGS = yaml.safe_load(config)
CATEGORIES = list({tag[0] for tag in TAGS.values()})
CATEGORIES.insert(0, "All")
with open(join(REPO_DIR, "order.json"), "r", encoding="utf-8") as config:
    ORDER = json.load(config)
with open(join(REPO_DIR, "colors.json"), "r", encoding="utf-8") as config:
    COLORS = json.load(config)


def certificates() -> dbc.Row:
    """
    Generates certificate cards and modals for certificates page.

    Returns:
        dbc.Row: Row with all cards and modals.
    """
    tabs = []
    all_modal_ids = []
    all_image_ids = []
    for category in CATEGORIES:
        tab, modal_ids, image_ids = make_category_cards(category)
        tabs.append(tab)
        all_modal_ids.extend(modal_ids)
        all_image_ids.extend(image_ids)
    component = dbc.Row(dbc.Tabs(tabs, active_tab="All"))

    # Create all callbacks with the used ids
    clientside_callback(
        ClientsideFunction(
            namespace='clientside',
            function_name='certificate_click'
        ),
        [Output(card_modal, 'is_open') for card_modal in all_modal_ids],
        [Input(image_modal, 'n_clicks') for image_modal in all_image_ids],
        prevent_initial_call=True
    )
    return component


def make_category_cards(category: str) -> tuple[dbc.Tab, list[str], list[str]]:
    """
    Generates cards with the given category.

    Args:
        category (str): Category of the certificate.

    Returns:
        tuple[dbc.Tab, list[str], list[str]]:
            Tab with all the cards of the given category.
            Modal ids of the cards.
            Image ids of the cards.
    """
    cards = []
    modal_ids = []
    image_ids = []
    for file in CERTIFICATES[::-1]:
        if category != "All":
            if category != TAGS[file[:3]][0]:
                continue

        modal_id = f"card-modal-{file[:3]}-{category}"
        image_id = f"card-image-{file[:3]}-{category}"
        modal_ids.append(modal_id)
        image_ids.append(image_id)

        body = [dbc.Badge(tag, pill=True) for tag in TAGS[file[:3]][1:]]
        body.append(html.P(file[4:-4], className="card-text"))
        card = dbc.Card([
            html.Div(dbc.CardImg(
                src=join(ASSETS_CERTIFICATES, file), top=True
            ), id=image_id),
            dbc.Modal([
                dbc.ModalBody([html.Img(
                    src=join(ASSETS_CERTIFICATES, file),
                    className="modal-image"
                )], class_name="certificate-modal-body"),
            ], id=modal_id, centered=True, size="xl"),
            dbc.CardBody(body, class_name="certificate-card-body"),
        ], class_name="certificate-card")
        cards.append(card)

    tab = dbc.Tab(dbc.Row(
        cards, justify="evenly", style={"marginTop": "15px"}
    ), label=f"{category} ({len(cards)})", tab_id=category)
    return tab, modal_ids, image_ids


def projects() -> dbc.Row:
    """
    Generates project cards for projects page.

    Returns:
        dbc.Row: Row with all project cards.
    """
    ordered_components = [None] * len(ORDER)
    head_components = []
    repos_directory = join(REPO_DIR, "repos.json")
    if not exists(repos_directory):
        get_repos()

    with open(repos_directory, "r", encoding="utf-8") as file:
        repos = json.load(file)

    for _, url, description, languages in repos:
        tags = [
            dbc.Badge(
                f"{lang} {short_display_num(count)}", pill=True,
                color=COLORS.get(lang, "rgba(233, 233, 222, 0.2)")
            )
            for lang, count in languages.items()
        ]
        repo_name = url.split('/')[-1]

        image_path = join(REPO_DIR, f"{repo_name}.png")
        if exists(image_path):
            image_path = join(ASSETS_REPOS, f"{repo_name}.png")
        else:
            image_path = join("assets/", "github.png")

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
        if url in ORDER:
            ordered_components[ORDER.index(url)] = card
        else:
            head_components.append(card)

    head_components.extend(ordered_components)
    component = dbc.Row(
        list(filter(None, head_components)),
        justify="evenly", class_name="project-row")
    return component


def curriculum_vitae() -> dbc.Row:
    """
    Generates cv preview and download button for cv page.

    Returns:
        dbc.Row: Row for cv page.
    """
    convert_from_path(CV_PDF)[0].save(CV_PNG, 'PNG')

    components = [
        dbc.Row(dbc.Button(
            "Download CV",
            href="assets/cv/Pedro Kobori CV.pdf",
            download="assets/cv/Pedro Kobori CV.pdf",
            external_link=True,
            color="info",
            size="lg",
            class_name="curriculum-button"
        ), class_name="curriculum-row"),
        dbc.Row(html.Img(
            src="assets/cv/Pedro Kobori CV.png",
            className="curriculum-image modal-content"
        ), class_name="curriculum-row")
    ]

    component = dbc.Row(
        components, class_name="curriculum-row")
    return component
