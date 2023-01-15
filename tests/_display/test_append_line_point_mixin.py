import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._display.append_line_point_mixin import AppendLinePointMixIn
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import assert_raises


class TestAppendLinePointMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_append_line_point(self) -> None:
        expression_data_util.empty_expression()
        mixin: AppendLinePointMixIn = AppendLinePointMixIn()
        mixin.variable_name = "test_append_line_point_mixin"
        mixin._variable_name_suffix = "test_mixin"
        x: ap.Int = ap.Int(50)
        y: ap.Int = ap.Int(100)
        assert_raises(
            expected_error_class=AttributeError,
            callable_=mixin.append_line_point,
            match=r"_points_var_name attribute is not set.",
            x=x,
            y=y,
        )

        mixin._points_var_name = "test_points"
        mixin.append_line_point(x=x, y=y)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"test_points.push([{x.variable_name}, {y.variable_name}]);"
        assert expected in expression
        assert "test_mixin" in mixin.points[0]._variable_name_suffix
        match: Optional[Match] = re.search(
            pattern=rf"{mixin.variable_name}\.plot\({var_names.ARRAY}\_.+?\);",
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None
