from random import randint
import re
from typing import Match, Optional

from retrying import retry

from apysc._display.polygon_apply_current_points_mixin import (
    PolygonApplyCurrentPointsMixIn
)
from apysc._expression import expression_data_util
from apysc._expression import var_names


class TestPolygonApplyCurrentPointsMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__apply_current_points(self) -> None:
        expression_data_util.empty_expression()
        mixin: PolygonApplyCurrentPointsMixIn = PolygonApplyCurrentPointsMixIn()
        mixin.variable_name = "test_mixin"
        mixin._apply_current_points()
        expression: str = expression_data_util.get_current_expression()
        assert "for (var " in expression
        match: Optional[Match] = re.search(
            pattern=rf"{mixin.variable_name}\.plot\({var_names.ARRAY}\_.+?\)",
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None
