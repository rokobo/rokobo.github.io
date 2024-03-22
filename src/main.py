"""Personal portfolio using Dash."""
from os.path import abspath, dirname, join, exists
from dash import Dash, html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from helper_functions import convert_certificates
from pages import about, certificates, projects, cv


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
            {"name": "viewport", "content": "initial-scale=1"},
        ]
    )

    # Tabs were used because they can be clientside, unlike Dash pages.
    app.layout = html.Div(dmc.MantineProvider([
        html.Canvas(id="stars"),
        dmc.Tabs([
            dmc.TabsList([
                dmc.Tab(
                    dmc.Badge("Pedro Kobori", color="gray", size="lg"),
                    value="logo", disabled=True,
                    icon=dmc.Avatar(src="assets/logo.svg")
                ),
                dmc.Tab("About", value="about", ml="auto"),
                dmc.Tab("Certificates", value="certificates"),
                dmc.Tab("Projects", value="projects"),
                dmc.Tab("CV", value="cv")
            ]),
            dmc.TabsPanel(about.layout, value="about"),
            dmc.TabsPanel(certificates.layout, value="certificates"),
            dmc.TabsPanel(projects.layout, value="projects"),
            dmc.TabsPanel(cv.layout, value="cv")
        ], id="tabs", value="about"),
    ], theme={"colorScheme": "dark"}))

    # Run debug mode if desktop.ini is in the main directory
    if exists(join(dirname(dirname(abspath(__file__))), ".env")):
        assert app.server is not None
        app.server.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
        convert_certificates()
        app.run_server(
            host="0.0.0.0",
            debug=True,
            port="8020",
            dev_tools_hot_reload=True
        )
    else:
        app.run_server(port="8080")
