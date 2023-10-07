import apysc as ap
from apysc._expression import expression_data_util, var_names
from apysc._testing.testing_helper import apply_test_settings
import re
from typing import Optional, Match


class TestBlueColorMixIn:
    @apply_test_settings()
    def test_blue_color(self) -> None:
        color: ap.Color = ap.Color("#fa0", variable_name_suffix="test_color")
        blue_color: ap.Int = color.blue_color
        assert blue_color._value == 0
        assert "test_color" in blue_color._variable_name_suffix
        assert "blue_color" in blue_color._variable_name_suffix
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{blue_color.variable_name} = "
            f"parseInt({color.variable_name}.substring(5, 7), 16);"
        )
        assert expected in expression

        color = ap.Color("#00aaff")
        blue_color = color.blue_color
        assert blue_color._value == 255

        color.blue_color = ap.Int(0)
        blue_color = color.blue_color
        assert blue_color._value == 0
        color.blue_color = ap.Int(255)
        blue_color = color.blue_color
        assert blue_color._value == 255
        expression = expression_data_util.get_current_expression()
        match_: Optional[Match] = re.search(
            pattern=(
                rf"{color.variable_name} = {var_names.STRING}_\d+? "
                rf"\+ {var_names.STRING}_\d+?;"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match_ is not None
