import apysc as ap
from apysc._display.append_line_color_attr_expression_mixin import (
    AppendLineColorAttrExpressionMixIn,
)
from apysc._display.line_color_mixin import LineColorMixIn
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
from tests._display.test_graphics_expression import assert_stroke_attr_expression_exists


class _TestMixIn(AppendLineColorAttrExpressionMixIn, LineColorMixIn):
    pass


class TestAppendLineColorAttrExpressionMixIn:
    @apply_test_settings()
    def test__append_line_color_attr_expression(self) -> None:
        mixin_1: AppendLineColorAttrExpressionMixIn
        mixin_1 = AppendLineColorAttrExpressionMixIn()
        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin_1._append_line_color_attr_expression,
            match="This instance is not a ",
            expression=".attr({\n",
            indent_num=2,
            skip_appending=False,
        )

        mixin_2: _TestMixIn = _TestMixIn()
        mixin_2.line_color = ap.String("#00aaff")
        expression: str = mixin_2._append_line_color_attr_expression(
            expression=".attr({\n",
            indent_num=2,
            skip_appending=True,
        )
        assert expression == ".attr({\n"

        expression = mixin_2._append_line_color_attr_expression(
            expression=".attr({\n",
            indent_num=2,
            skip_appending=False,
        )
        assert_stroke_attr_expression_exists(expression=expression)
