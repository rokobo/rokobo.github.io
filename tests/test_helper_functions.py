"""Test input and output functions."""
# pylint: disable=import-error

from helper_functions import short_display_num


def test_short_display_num() -> None:
    """Tests short_display_num function."""
    assert short_display_num(1) == "1"
    assert short_display_num(20) == "20"
    assert short_display_num(865) == "865"
    assert short_display_num(5648) == "5k"
    assert short_display_num(97018) == "97k"
    assert short_display_num(642864) == "642k"
    assert short_display_num(27649818) == "27m"
    assert short_display_num(4046545465) == "4b"
