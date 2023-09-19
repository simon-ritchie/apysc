from typing import Optional, Match
import apysc as ap
import re
from apysc._expression import expression_data_util, var_names
from apysc._testing.testing_helper import apply_test_settings


class TestStringZfillMixIn:
    @apply_test_settings()
    def test_zfill(self) -> None:
        string: ap.String = ap.String('123')
        result_string: ap.String = string.zfill(width=5)
        assert result_string._value == "00123"
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result_string.variable_name} = {string.variable_name}"
            f'.padStart('
        )
        assert expected in expression
        assert ', "0");' in expression

        match_: Optional[Match] = re.search(
            pattern=rf"\({var_names.INT}_\d+?,", string=expression
        )
        assert match_ is not None

