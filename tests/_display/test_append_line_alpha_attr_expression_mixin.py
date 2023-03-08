import apysc as ap
from tests._display.test_graphics_expression import (
    assert_stroke_opacity_attr_expression_exists
)
from apysc._display.line_alpha_mixin import LineAlphaMixIn
from apysc._display.append_line_alpha_attr_expression_mixin import (
    AppendLineAlphaAttrExpressionMixIn
)
from apysc._testing.testing_helper import apply_test_settings, assert_raises


class _TestMixIn(AppendLineAlphaAttrExpressionMixIn, LineAlphaMixIn):
    pass


class TestAppendLineAlphaAttrExpressionMixIn:
    # @apply_test_settings()
    def test__append_line_alpha_attr_expression(self) -> None:
        mixin_1: AppendLineAlphaAttrExpressionMixIn
        mixin_1 = AppendLineAlphaAttrExpressionMixIn()
        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin_1._append_line_alpha_attr_expression,
            match="This instance is not a ",
            expression="This instance is not a ",
            indent_num=2,
            skip_appending=False,
        )

        mixin_2: _TestMixIn = _TestMixIn()
        mixin_2.line_alpha = ap.Number(0.5)
        expression: str = mixin_2._append_line_alpha_attr_expression(
            expression=".attr({\n",
            indent_num=2,
            skip_appending=True,
        )
        assert expression == ".attr({\n"

        expression = mixin_2._append_line_alpha_attr_expression(
            expression=".attr({\n",
            indent_num=2,
            skip_appending=False,
        )
        assert_stroke_opacity_attr_expression_exists(expression=expression)
