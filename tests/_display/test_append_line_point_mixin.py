import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._display.append_line_point_mixin import AppendLinePointMixIn
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises


class TestAppendLinePointMixIn:
    @apply_test_settings()
    def test_append_line_point(self) -> None:
        ap.Stage()
        mixin: AppendLinePointMixIn = AppendLinePointMixIn()
        mixin.variable_name = "test_append_line_point_mixin"
        mixin._variable_name_suffix = "test_mixin"
        x: ap.Number = ap.Number(50)
        y: ap.Number = ap.Number(100)
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
