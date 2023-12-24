"""Tests modules for pylint problems."""
import os
from pylint.lint import Run

workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_folder = os.path.join(workspace, "src")
pages_folder = os.path.join(workspace, "src/pages")


def test_pylint_main() -> None:
    """Ensures main passes pylint specifications."""
    file = os.path.join(src_folder, "main.py")
    result = Run([file], exit=False).linter.stats
    assert result.global_note == 10, result.by_msg


def test_pylint_components() -> None:
    """Ensures components passes pylint specifications."""
    file = os.path.join(src_folder, "components.py")
    result = Run([file], exit=False).linter.stats
    assert result.global_note == 10, result.by_msg


def test_pylint_helper_functions() -> None:
    """Ensures helper_functions passes pylint specifications."""
    file = os.path.join(src_folder, "helper_functions.py")
    result = Run([file], exit=False).linter.stats
    assert result.global_note == 10, result.by_msg


def test_pylint_about() -> None:
    """Ensures about passes pylint specifications."""
    file = os.path.join(pages_folder, "about.py")
    result = Run([file], exit=False).linter.stats
    assert result.global_note == 10, result.by_msg


def test_pylint_certificates() -> None:
    """Ensures certificates passes pylint specifications."""
    file = os.path.join(pages_folder, "certificates.py")
    result = Run([file], exit=False).linter.stats
    assert result.global_note == 10, result.by_msg
