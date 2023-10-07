import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings


class TestGreenColorMixIn:
    @apply_test_settings()
    def test_green_color(self) -> None:
        color: ap.Color = ap.Color("#a0f", variable_name_suffix="test_color")
        green_color: ap.Int = color.green_color
        assert green_color._value == 0
        assert "test_color" in green_color._variable_name_suffix
        assert "green_color" in green_color._variable_name_suffix
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{green_color.variable_name} = "
            f"parseInt({color.variable_name}.substring(3, 5), 16);"
        )
        assert expected in expression

        color = ap.Color("#00ffaa")
        green_color = color.green_color
        assert green_color._value == 255

        color.green_color = ap.Int(0)
        green_color = color.green_color
        assert green_color._value == 0
        color.green_color = ap.Int(255)
        green_color = color.green_color
        assert green_color._value == 255
        expression = expression_data_util.get_current_expression()
        match_: Optional[Match] = re.search(
            pattern=(
                rf"{color.variable_name} = {var_names.STRING}_\d+? \+ "
                rf"{var_names.STRING}_\d+? \+ {var_names.STRING}_\d+?;"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match_ is not None
