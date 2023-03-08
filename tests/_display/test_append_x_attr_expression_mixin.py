import apysc as ap
from tests._display.test_graphics_expression import (
    assert_x_attr_expression_exists
)
from apysc._testing.testing_helper import apply_test_settings, assert_raises
from apysc._display.append_x_attr_expression_mixin import AppendXAttrExpressionMixIn
from apysc._display.x_mixin import XMixIn


class _TestMixIn(AppendXAttrExpressionMixIn, XMixIn):
    pass


class TestAppendXAttrExpressionMixIn:
    @apply_test_settings()
    def test__append_x_attr_expression(self) -> None:
        mixin_1: AppendXAttrExpressionMixIn = AppendXAttrExpressionMixIn()
        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin_1._append_x_attr_expression,
            expression=".attr({\n",
            indent_num=2,
            skip_appending=False,
        )

        mixin_2: _TestMixIn = _TestMixIn()
        mixin_2.x = ap.Number(100.0)
        expression: str = mixin_2._append_x_attr_expression(
            expression=".attr({\n",
            indent_num=2,
            skip_appending=True,
        )
        assert expression == ".attr({\n"

        expression = mixin_2._append_x_attr_expression(
            expression=".attr({\n",
            indent_num=2,
            skip_appending=False,
        )
        assert_x_attr_expression_exists(expression=expression)
