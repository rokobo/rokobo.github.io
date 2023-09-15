"""Tests modules for pylint problems."""
import os
from pylint.lint import Run

workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_folder = os.path.join(workspace, "src")
pages_folder = os.path.join(workspace, "src/pages")


def test_pylint_functions_activity() -> None:
    """Ensures main passes pylint specifications."""
    file = os.path.join(src_folder, "main.py")
    result = Run([file], exit=False).linter.stats
    assert result.global_note == 10, result.by_msg
