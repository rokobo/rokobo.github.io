"""Personal portfolio using Dash."""
from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP


if __name__ == '__main__':
    app = Dash(
        __name__,
        update_title=None,
        external_stylesheets=[BOOTSTRAP],
        title="Pedro Kobori Portfolio",
        assets_folder='../assets',
        use_pages=True
    )
    app.run_server(port="8080")
