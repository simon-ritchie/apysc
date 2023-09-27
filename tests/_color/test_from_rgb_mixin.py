import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._color import from_rgb_mixin
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test__get_py_str_from_rgb() -> None:
    py_str: str = from_rgb_mixin._get_py_str_from_rgb(
        red=0,
        green=1,
        blue=2,
    )
    assert py_str == "#000102"

    py_str = from_rgb_mixin._get_py_str_from_rgb(
        red=255,
        green=255,
        blue=255,
    )
    assert py_str == "#FFFFFF"

    py_str = from_rgb_mixin._get_py_str_from_rgb(
        red=ap.Int(0),
        green=ap.Int(1),
        blue=ap.Int(2),
    )
    assert py_str == "#000102"


class TestFromRgbMixIn:
    @apply_test_settings()
    def test_from_rgb(self) -> None:
        color: ap.Color = ap.Color.from_rgb(
            red=0, green=1, blue=2, variable_name_suffix="test_suffix"
        )
        assert color._value._value == "#000102"
        assert color._variable_name_suffix == "test_suffix"
        expression: str = expression_data_util.get_current_expression()
        assert expression.count("toString(16);") >= 3
        assert expression.count(".toUpperCase();") >= 3
        match_: Optional[Match] = re.search(
            pattern=rf'{color.variable_name} = "#" \+ .+? \+ .+? \+ .+?\;',
            string=expression,
        )
        assert match_ is not None

        color = ap.Color.from_rgb(red=255, green=255, blue=255)
        assert color._value._value == "#FFFFFF"
