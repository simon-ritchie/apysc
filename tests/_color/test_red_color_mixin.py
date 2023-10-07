import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings


class TestRedColorMixIn:
    @apply_test_settings()
    def test_red_color(self) -> None:
        color: ap.Color = ap.Color("#0af", variable_name_suffix="test_color")
        red_color: ap.Int = color.red_color
        assert red_color._value == 0
        assert "test_color" in red_color._variable_name_suffix
        assert "red_color" in red_color._variable_name_suffix
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{red_color.variable_name} = "
            f"parseInt({color.variable_name}.substring(1, 3), 16);"
        )
        assert expected in expression

        color = ap.Color("#ff00aa")
        red_color = color.red_color
        assert red_color._value == 255

        color.red_color = ap.Int(0)
        red_color = color.red_color
        assert red_color._value == 0
        color.red_color = ap.Int(255)
        red_color = color.red_color
        assert red_color._value == 255
        expression = expression_data_util.get_current_expression()
        match_: Optional[Match] = re.search(
            pattern=(
                rf'{color.variable_name} = "#" \+ {var_names.STRING}_\d+? '
                rf"\+ {var_names.STRING}_\d+?;"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match_ is not None
