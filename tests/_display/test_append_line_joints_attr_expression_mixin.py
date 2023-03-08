import apysc as ap
from tests._display.test_graphics_expression import (
    assert_stroke_linejoin_attr_expression_exists
)
from apysc._testing.testing_helper import apply_test_settings, assert_raises
from apysc._display.append_line_joints_attr_expression_mixin import (
    AppendLineJointsAttrExpressionMixIn
)
from apysc._display.line_joints_mixin import LineJointsMixIn


class _TestMixIn(AppendLineJointsAttrExpressionMixIn, LineJointsMixIn):
    pass


class TestAppendLineJointsAttrExpressionMixIn:
    @apply_test_settings()
    def test__append_line_joints_attr_expression(self) -> None:
        mixin_1: AppendLineJointsAttrExpressionMixIn
        mixin_1 = AppendLineJointsAttrExpressionMixIn()
        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin_1._append_line_joints_attr_expression,
            match="This instance is not a ",
            expression=".attr({\n",
            indent_num=2,
            skip_appending=False,
        )

        mixin_2: _TestMixIn = _TestMixIn()
        mixin_2.line_joints = ap.LineJoints.ROUND
        expression: str = mixin_2._append_line_joints_attr_expression(
            expression=".attr({\n",
            indent_num=2,
            skip_appending=True,
        )
        assert expression == ".attr({\n"

        expression = mixin_2._append_line_joints_attr_expression(
            expression=".attr({\n",
            indent_num=2,
            skip_appending=False,
        )
        assert_stroke_linejoin_attr_expression_exists(expression=expression)
