import re
from typing import List
from typing import Match
from typing import Optional

import apysc as ap
from apysc._display.set_lower_scale_limit_mixin import SetLowerScaleLimitMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestSetLowerScaleLimitMixIn:
    @apply_test_settings()
    def test__set_lower_scale_limit(self) -> None:
        from apysc._expression import expression_data_util

        expression_data_util.empty_expression()
        value: ap.Number = ap.Number(-1.5)
        interface: SetLowerScaleLimitMixIn = SetLowerScaleLimitMixIn()
        interface._set_lower_scale_limit(value=value)
        expression: str = expression_data_util.get_current_expression()
        expected_patterns: List[str] = [
            r" \< ",
            r"if \(.*?\) {",
            r" = 1e-08",
        ]
        for expected_pattern in expected_patterns:
            match: Optional[Match] = re.search(
                pattern=expected_pattern,
                string=expression,
                flags=re.MULTILINE | re.DOTALL,
            )
            assert match is not None, expected_pattern
