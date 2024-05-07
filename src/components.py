"""Functions for building components."""
# pylint: disable=import-error
from os import listdir
from os.path import join, abspath, dirname, exists
import json
import yaml
from dash import html, Input, Output, clientside_callback, ClientsideFunction
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from pdf2image import convert_from_path
from helper_functions import short_display_num, get_repos

HOME = dirname(dirname(abspath(__file__)))
ASSETS_CERTIFICATES = "assets/certificates"
ASSET_DIR = join(HOME, ASSETS_CERTIFICATES)
ASSETS_REPOS = "assets/repos"
REPO_DIR = join(HOME, ASSETS_REPOS)
CERTIFICATES = [f for f in listdir(ASSET_DIR) if f.endswith((".png", ".jpg"))]
CERTIFICATES.sort()
with open(join(ASSET_DIR, "tags.yml"), "r", encoding="utf-8") as config:
    TAGS = yaml.safe_load(config)
CATEGORIES = list({tag for tags in TAGS.values() for tag in tags[0]})
CATEGORIES.insert(0, "All")
with open(join(REPO_DIR, "order.json"), "r", encoding="utf-8") as config:
    ORDER = json.load(config)
with open(join(REPO_DIR, "colors.json"), "r", encoding="utf-8") as config:
    COLORS = json.load(config)
URLS = {
    "github": "https://github.com/rokobo",
    "linkedin": "https://www.linkedin.com/in/pedrokobori/"
}


def about() -> dbc.Row:
    """
    Generates about section.

    Returns:
        dbc.Row: Row with about sections.
    """
    component = dbc.Row([

        dbc.Row([
            html.H1(["Hello! 👋, I am ", html.Span("Pedro Kobori", style={
                "text-decoration": "underline", "color": "#0d9efd"})]),
            html.H6("""
                Self-taught developer with a passion for databases,
                productivity software, automations,
                data analysis, data engineering and machine learning.
            """),
            html.Br(),
            dbc.Stack([
                html.A([html.Img(
                    src="assets/github.png", className="home-icons"
                )], href=URLS["github"], target="_blank"),
                html.A([html.Img(
                    src="assets/linkedin.png", className="home-icons"
                )], href=URLS["linkedin"], target="_blank")
            ], direction="horizontal", className="justify-content-evenly"),
        ], className="centered", style={"height": "90vh"}),
        dbc.Row([
            dbc.Card(dbc.CardBody([html.H5(["""
                I am self-taught backend software developer. My education is
                based on the curriculum dictated by the Open Source Society
                University """,
                html.A(
                    "(OSSU)", href="https://github.com/ossu/computer-science"),
                "."
            ], className="about-text")]), className="glass about-card"),
            html.Br(),
            dbc.Card(dbc.CardBody([html.H5(["""
                I always loved hoarding and analyzing all kinds of data.
                Throughout life, this lead me to recording and thinking about
                every piece of information I could get my hands on. I became
                particularly interested in automating data analysis and
                collection, as well as in how information is perceived and
                understood by people. I find it fascinating how people, with
                their own experiences, produced vastly different theories and
                conclusions with the information they are surrounded by. This
                eventually made me become interested in computer software
                development, psychology, market analysis and the dynamics of
                data.
            """], className="about-text")]), className="glass about-card"),
            html.Br(),
            dbc.Card(dbc.CardBody([html.H5(["""
                To me, learning about data analysis is more than a
                mathematical problem. Learning to gather and interpret data
                served me well in numerous situations. By applying the
                knowledge I gained from constantly trying to find patterns in
                data, I was able to make better decisions in life. Information
                is everywhere, training to interpret patterns and biases
                enables one to become a better person.
            """], className="about-text")]), className="glass about-card"),
            html.Br(),
            dbc.Card(dbc.CardBody([html.H5(["""
                I believe the study and analysis of data is a fundamental
                pillar for the development of a better world. Being able to
                transform data into meaningful and helpful insights is what I
                strive for as a software developer.
            """], className="about-text")]), className="glass about-card")

        ], className="centered")
    ])
    return component


def certificates() -> dbc.Row:
    """
    Generates certificate cards and modals for certificates page.

    Returns:
        dbc.Row: Row with all cards and modals.
    """
    index = 0
    tabs = []
    all_modal_ids = []
    all_image_ids = []
    tablist = []

    for category in CATEGORIES:
        tab, modal_ids, image_ids, label, index = make_category_cards(
            category, index)
        tabs.append(tab)
        tablist.append(dmc.TabsTab(label, value=category))
        all_modal_ids.extend(modal_ids)
        all_image_ids.extend(image_ids)

    component = dbc.Row(dmc.Tabs(
        [dmc.TabsList(tablist, grow=True)] + tabs,
        value="All", color="gray", variant="pills"
    ))

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


def make_category_cards(category: str, index: int) -> tuple[
        dmc.TabsPanel, list[str], list[str], str, int]:
    """
    Generates cards with the given category.

    Args:
        category (str): Category of the certificate.
        index (int): Index for callback.

    Returns:
        tuple[dmc.TabsPanel, list[str], list[str]]:
            Tab with all the cards of the given category.
            Modal ids of the cards.
            Image ids of the cards.
    """
    cards = []
    modal_ids = []
    image_ids = []
    for file in CERTIFICATES[::-1]:
        if category != "All":
            if category not in TAGS[file[:3]][0]:
                continue

        modal_id = f"card-modal-{index}-{category}"
        image_id = f"card-image-{index}-{category}"
        modal_ids.append(modal_id)
        image_ids.append(image_id)
        index += 1

        body: list[dbc.Badge | html.P] = [
            dbc.Badge(tag, pill=True) for tag in TAGS[file[:3]][2:]]
        body.append(html.P(file[4:-4], className="card-text"))
        card = dbc.Card([
            html.Div(dbc.CardImg(
                src=join(ASSETS_CERTIFICATES, file), top=True
            ), id=image_id),
            dbc.Modal([
                dbc.ModalBody([
                    html.Img(
                        src=join(ASSETS_CERTIFICATES, file),
                        className="modal-image"
                    ),
                    dbc.Card(dbc.CardBody([  # Learned topics
                        dbc.Badge(tag, pill=True) for tag in TAGS[file[:3]][1]
                    ]))
                ]),
            ], id=modal_id, centered=True, size="xl"),
            dbc.CardBody(body, class_name="certificate-card-body"),
        ], class_name="glass certificate-card base-card")
        cards.append(dmc.GridCol(card, span="auto"))

    tab = dmc.TabsPanel(
        dmc.Grid(cards, gutter="xl"),
        value=category
    )
    return tab, modal_ids, image_ids, f"{category} ({len(cards)})", index


def projects() -> dmc.Grid:
    """
    Generates project cards for projects page.

    Returns:
        dmc.Grid: Row with all project cards.
    """
    repos_directory = join(REPO_DIR, "repos.json")

    if not exists(repos_directory):
        get_repos()

    with open(repos_directory, "r", encoding="utf-8") as file:
        repos = json.load(file)

    components, modal_ids, image_ids = make_project_cards(repos)
    component = dmc.Grid(
        list(filter(None, components)),
        gutter="xl"
    )

    # Create all callbacks with the used ids
    clientside_callback(
        ClientsideFunction(
            namespace='clientside',
            function_name='project_click'
        ),
        [Output(project_modal, 'is_open') for project_modal in modal_ids],
        [Input(image_modal, 'n_clicks') for image_modal in image_ids],
        prevent_initial_call=True
    )
    return component


def make_project_cards(repos: list) -> tuple[
        list[dbc.Card], list[str], list[str]]:
    """
    Generates project cards.

    Args:
        repos (list): Repo information.

    Returns:
        tuple[list[dbc.Card], list[str], list[str]]:
            List of project cards.
            Modal ids of the cards.
            Image ids of the cards.
    """
    ordered_comps = [None] * len(ORDER)
    head_components = []
    modal_ids = []
    image_ids = []
    index = 0

    for _, url, description, languages in repos:
        tags = [
            dbc.Badge(
                f"{lang} {short_display_num(count)}", pill=True,
                color=COLORS.get(lang, "rgba(233, 233, 222, 0.2)")
            )
            for lang, count in languages.items()
        ]
        repo_name = url.split('/')[-1]
        modal_id = f"card-modal-{str(index).zfill(3)}"
        image_id = f"card-image-{str(index).zfill(3)}"
        index += 1
        modal_ids.append(modal_id)
        image_ids.append(image_id)

        image_path = join(REPO_DIR, f"{repo_name}.png")
        if exists(image_path):
            image_path = join(ASSETS_REPOS, f"{repo_name}.png")
        else:
            image_path = join("assets/", "github.png")

        card = dbc.Card([
            html.Div(dbc.CardImg(
                src=image_path, top=True, class_name="project-card-image"
            ), id=image_id),
            dbc.Modal([
                dbc.ModalBody([html.Img(
                    src=join(image_path),
                    className="modal-image"
                )]),
            ], id=modal_id, centered=True, size="xl"),
            dbc.CardBody([
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
            ], class_name="project-card-body"),
            dbc.Tooltip(
                repo_name,
                target=f"project-card-title-{repo_name}"
            ),
        ], class_name="project-card glass base-card")
        if url in ORDER:
            ordered_comps[ORDER.index(url)] = dmc.GridCol(card, span="auto")
        else:
            head_components.append(dmc.GridCol(card, span="auto"))

    head_components.extend(ordered_comps)
    return head_components, modal_ids, image_ids


def curriculum_vitae() -> dbc.Row:
    """
    Generates cv preview and download button for cv page.

    Returns:
        dbc.Row: Row for cv page.
    """
    languages = ["en", "pt"]
    tabs = []
    tablist = [
        dmc.TabsTab("Curriculum (en)", value="en"),
        dmc.TabsTab("Curriculum (pt)", value="pt")
    ]

    for lang in languages:
        cv_pdf = join(HOME, f"assets/cv/Pedro Kobori CV-{lang}.pdf")
        cv_png = f"assets/cv/Pedro Kobori CV-{lang}.png"
        convert_from_path(cv_pdf)[0].save(cv_png, 'PNG')

        card = dbc.Card([
            dbc.Row(dbc.Button(
                "Download CV",
                href=cv_pdf,
                download=cv_pdf,
                external_link=True,
                color="secondary",
                size="lg",
                class_name="curriculum-button"
            ), class_name="curriculum-row"),
            dbc.Row(html.Img(
                src=cv_png,
                className="curriculum-image modal-content"
            ), class_name="curriculum-row")
        ], style={
            'backgroundColor': 'rgba(0,0,0,0)', 'marginBottom': '100px'})

        tabs.append(dmc.TabsPanel(card, value=lang))

    component = dbc.Row(dmc.Tabs(
        [dmc.TabsList(tablist, grow=True)] + tabs,
        value="en", color="gray", variant="pills"
    ))
    return component
