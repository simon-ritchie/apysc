from random import randint
import re
from typing import List, Optional, Match

from retrying import retry

from apysc._display.set_lower_scale_limit_interface import SetLowerScaleLimitInterface
import apysc as ap
from apysc._expression import var_names


class TestSetLowerScaleLimitInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_lower_scale_limit(self) -> None:
        from apysc._expression import expression_data_util
        expression_data_util.empty_expression()
        value: ap.Number = ap.Number(-1.5)
        interface: SetLowerScaleLimitInterface = SetLowerScaleLimitInterface()
        interface._set_lower_scale_limit(value=value)
        expression: str = expression_data_util.get_current_expression()
        expected_patterns: List[str] = [
            r' \< ',
            r'if \(.*?\) {',
            r' = 1e-08',
        ]
        for expected_pattern in expected_patterns:
            match: Optional[Match] = re.search(
                pattern=expected_pattern,
                string=expression,
                flags=re.MULTILINE | re.DOTALL)
            assert match is not None, expected_pattern
