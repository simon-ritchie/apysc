import apysc as ap
from tests._display.test_graphics_expression import (
    assert_stroke_width_attr_expression_exists
)
from apysc._testing.testing_helper import apply_test_settings, assert_raises
from apysc._display.append_line_thickness_attr_expression_mixin import (
    AppendLineThicknessAttrExpressionMixIn
)
from apysc._display.line_thickness_mixin import LineThicknessMixIn


class _TestMixIn(AppendLineThicknessAttrExpressionMixIn, LineThicknessMixIn):
    pass


class TestAppendLineThicknessAttrExpressionMixIn:
    @apply_test_settings()
    def test__append_line_thickness_attr_expression(self) -> None:
        mixin_1: AppendLineThicknessAttrExpressionMixIn
        mixin_1 = AppendLineThicknessAttrExpressionMixIn()
        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin_1._append_line_thickness_attr_expression,
            match="This instance is not a ",
            expression=".attr({\n",
            indent_num=2,
            skip_appending=False,
        )

        mixin_2: _TestMixIn = _TestMixIn()
        mixin_2.line_thickness = ap.Int(2)
        expression: str = mixin_2._append_line_thickness_attr_expression(
            expression=".attr({\n",
            indent_num=2,
            skip_appending=True,
        )
        assert expression == ".attr({\n"

        expression = mixin_2._append_line_thickness_attr_expression(
            expression=".attr({\n",
            indent_num=2,
            skip_appending=False,
        )
        assert_stroke_width_attr_expression_exists(expression=expression)
