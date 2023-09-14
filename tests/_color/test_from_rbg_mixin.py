import apysc as ap
from apysc._color import from_rbg_mixin
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test__get_hex_str_from_int() -> None:
    hex_str: str = from_rbg_mixin._get_hex_str_from_int(color_int=0)
    assert hex_str == "00"

    hex_str = from_rbg_mixin._get_hex_str_from_int(color_int=1)
    assert hex_str == "01"

    hex_str = from_rbg_mixin._get_hex_str_from_int(color_int=255)
    assert hex_str == "FF"

    hex_str = from_rbg_mixin._get_hex_str_from_int(color_int=ap.Int(255))
    assert hex_str == "FF"
