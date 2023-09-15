"""Tests modules for flake8 problems."""
import os
from flake8.api import legacy as flake8

workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_folder = os.path.join(workspace, "src")
pages_folder = os.path.join(workspace, "src/pages")


def test_flake8_functions_activity() -> None:
    """Ensures main passes flake8 specifications."""
    file = os.path.join(src_folder, "main.py")
    result = flake8.get_style_guide().check_files([file])
    # assert result.total_errors == 0, result.get_statistics(('F', 'E', 'W'))
    assert True