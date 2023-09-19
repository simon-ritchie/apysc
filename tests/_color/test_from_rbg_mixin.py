import apysc as ap
from apysc._color import from_rbg_mixin
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test__get_py_str_from_rgb() -> None:
    py_str: str = from_rbg_mixin._get_py_str_from_rgb(
        red=0,
        green=1,
        blue=2,
    )
    assert py_str == "#000102"

    py_str = from_rbg_mixin._get_py_str_from_rgb(
        red=255,
        green=255,
        blue=255,
    )
    assert py_str == "#FFFFFF"

    py_str = from_rbg_mixin._get_py_str_from_rgb(
        red=ap.Int(0),
        green=ap.Int(1),
        blue=ap.Int(2),
    )
    assert py_str == "#000102"
