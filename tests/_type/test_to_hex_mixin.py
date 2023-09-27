import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestToHexMixIn:
    @apply_test_settings()
    def test_to_hex(self) -> None:
        int_value: ap.Int = ap.Int(0)
        hex_str: ap.String = int_value.to_hex(variable_name_suffix="test_suffix")
        assert hex_str._value == "0"
        assert hex_str._variable_name_suffix == "test_suffix"
        expression: str = expression_data_util.get_current_expression()
        assert "Math.trunc(" in expression
        match_: Optional[Match] = re.search(
            pattern=rf"{hex_str.variable_name} = .+?\.toString\(16\);",
            string=expression,
        )
        assert match_ is not None

        int_value = ap.Int(10)
        hex_str = int_value.to_hex()
        assert hex_str._value == "a"

        number: ap.Number = ap.Number(10.5)
        hex_str = number.to_hex()
        assert hex_str._value == "a"
