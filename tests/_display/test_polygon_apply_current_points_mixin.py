from random import randint

from retrying import retry

from apysc._display.polygon_apply_current_points_mixin import (
    PolygonApplyCurrentPointsMixIn
)
from apysc._expression import expression_data_util


class TestPolygonApplyCurrentPointsMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__apply_current_points(self) -> None:
        expression_data_util.empty_expression()
        mixin: PolygonApplyCurrentPointsMixIn = PolygonApplyCurrentPointsMixIn()
        mixin.variable_name = "test_mixin"
        mixin._points_var_name = "test_points"
        mixin._apply_current_points()
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin.variable_name}.plot({mixin._points_var_name});"
        assert expected in expression
