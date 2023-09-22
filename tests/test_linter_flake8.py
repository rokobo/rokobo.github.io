"""Tests modules for flake8 problems."""
import os
from flake8.api import legacy as flake8

workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_folder = os.path.join(workspace, "src")
pages_folder = os.path.join(workspace, "src/pages")


def test_flake8_main() -> None:
    """Ensures main passes flake8 specifications."""
    file = os.path.join(src_folder, "main.py")
    result = flake8.get_style_guide().check_files([file])
    assert result.total_errors == 0, result.get_statistics(('F', 'E', 'W'))


def test_flake8_components() -> None:
    """Ensures components passes flake8 specifications."""
    file = os.path.join(src_folder, "components.py")
    result = flake8.get_style_guide().check_files([file])
    assert result.total_errors == 0, result.get_statistics(('F', 'E', 'W'))


def test_flake8_helper_functions() -> None:
    """Ensures helper_functions passes flake8 specifications."""
    file = os.path.join(src_folder, "helper_functions.py")
    result = flake8.get_style_guide().check_files([file])
    assert result.total_errors == 0, result.get_statistics(('F', 'E', 'W'))


def test_flake8_about() -> None:
    """Ensures about passes flake8 specifications."""
    file = os.path.join(pages_folder, "about.py")
    result = flake8.get_style_guide().check_files([file])
    assert result.total_errors == 0, result.get_statistics(('F', 'E', 'W'))


def test_flake8_certificates() -> None:
    """Ensures certificates passes flake8 specifications."""
    file = os.path.join(pages_folder, "certificates.py")
    result = flake8.get_style_guide().check_files([file])
    assert result.total_errors == 0, result.get_statistics(('F', 'E', 'W'))


def test_flake8_navigation() -> None:
    """Ensures navigation passes flake8 specifications."""
    file = os.path.join(pages_folder, "navigation.py")
    result = flake8.get_style_guide().check_files([file])
    assert result.total_errors == 0, result.get_statistics(('F', 'E', 'W'))
