import apysc as ap
from apysc._display.append_fill_color_expression_mixin import (
    AppendFillColorAttrExpressionMixIn,
)
from apysc._display.fill_color_mixin import FillColorMixIn
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
from tests._display.test_graphics_expression import assert_fill_attr_expression_exists


class _TestMixIn(AppendFillColorAttrExpressionMixIn, FillColorMixIn):
    pass


class TestAppendFillColorAttrExpressionMixIn:
    @apply_test_settings()
    def test__append_fill_color_attr_expression(self) -> None:
        mixin_1: AppendFillColorAttrExpressionMixIn
        mixin_1 = AppendFillColorAttrExpressionMixIn()
        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin_1._append_fill_color_attr_expression,
            match="This instance is not a ",
            expression=".attr({\n",
            indent_num=2,
            skip_appending=False,
        )

        mixin_2: _TestMixIn = _TestMixIn()
        mixin_2.fill_color = ap.String("#0af")
        expression: str = mixin_2._append_fill_color_attr_expression(
            expression=".attr({\n",
            indent_num=2,
            skip_appending=True,
        )
        assert expression == ".attr({\n"

        expression = mixin_2._append_fill_color_attr_expression(
            expression=".attr({\n",
            indent_num=2,
            skip_appending=False,
        )
        assert_fill_attr_expression_exists(expression=expression)
