import apysc as ap
from apysc._display.append_fill_alpha_attr_expression_mixin import (
    AppendFillAlphaAttrExpressionMixIn,
)
from apysc._display.fill_alpha_mixin import FillAlphaMixIn
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
from tests._display.test_graphics_expression import (
    assert_fill_opacity_attr_expression_exists,
)


class _TestMixIn(AppendFillAlphaAttrExpressionMixIn, FillAlphaMixIn):
    pass


class TestAppendFillAlphaAttrExpressionMixIn:
    @apply_test_settings()
    def test__append_fill_alpha_attr_expression(self) -> None:
        mixin_1: AppendFillAlphaAttrExpressionMixIn
        mixin_1 = AppendFillAlphaAttrExpressionMixIn()
        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin_1._append_fill_alpha_attr_expression,
            match="This instance is not a ",
            expression=".attr({\n",
            indent_num=2,
            skip_appending=False,
        )

        mixin_2: _TestMixIn = _TestMixIn()
        mixin_2.fill_alpha = ap.Number(0.5)
        expression: str = mixin_2._append_fill_alpha_attr_expression(
            expression=".attr({\n",
            indent_num=2,
            skip_appending=True,
        )
        assert expression == ".attr({\n"

        expression = mixin_2._append_fill_alpha_attr_expression(
            expression=".attr({\n",
            indent_num=2,
            skip_appending=False,
        )
        assert_fill_opacity_attr_expression_exists(expression=expression)
