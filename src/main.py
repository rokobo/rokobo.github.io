"""Personal portfolio using Dash."""
from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP


if __name__ == '__main__':
    app = Dash(
        __name__, update_title=None, external_stylesheets=[BOOTSTRAP],
        title="Pedro Kobori Portfolio", assets_folder='../assets',
        use_pages=True
    )
    app.run_server(
        host="0.0.0.0",
        debug=False,
        port="8080",
        dev_tools_hot_reload=True,
        use_reloader=True
    )
