import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._display.append_line_point_mixin import AppendLinePointMixIn
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import VariableNameSuffixAttrOrVarMixIn


class _TestObject(
    AppendLinePointMixIn,
    VariableNameMixIn,
    VariableNameSuffixMixIn,
    VariableNameSuffixAttrOrVarMixIn,
):
    pass


class TestAppendLinePointMixIn:
    @apply_test_settings()
    def test_append_line_point(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_append_line_point_mixin"
        instance._variable_name_suffix = "test_mixin"
        x: ap.Number = ap.Number(50)
        y: ap.Number = ap.Number(100)
        assert_raises(
            expected_error_class=AttributeError,
            callable_=instance.append_line_point,
            match=r"_points_var_name attribute is not set.",
            x=x,
            y=y,
        )

        instance._points_var_name = "test_points"
        instance.append_line_point(x=x, y=y)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"test_points.push([{x.variable_name}, {y.variable_name}]);"
        assert expected in expression
        assert "test_mixin" in instance.points[0]._variable_name_suffix
        match: Optional[Match] = re.search(
            pattern=rf"{instance.variable_name}\.plot\({var_names.ARRAY}\_.+?\);",
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None
