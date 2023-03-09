import apysc as ap
from apysc._display.append_y_attr_expression_mixin import AppendYAttrExpressionMixIn
from apysc._display.y_mixin import YMixIn
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
from tests._display.test_graphics_expression import assert_y_attr_expression_exists


class _TestMixIn(AppendYAttrExpressionMixIn, YMixIn):
    pass


class TestAppendYAttrExpressionMixIn:
    @apply_test_settings()
    def test__append_y_attr_expression(self) -> None:
        mixin_1: AppendYAttrExpressionMixIn = AppendYAttrExpressionMixIn()
        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin_1._append_y_attr_expression,
            match="This instance is not a ",
            expression=".attr({\n",
            indent_num=2,
            skip_appending=False,
        )

        mixin_2: _TestMixIn = _TestMixIn()
        mixin_2.y = ap.Number(100)
        expression: str = mixin_2._append_y_attr_expression(
            expression=".attr({\n",
            indent_num=2,
            skip_appending=True,
        )
        assert expression == ".attr({\n"

        expression = mixin_2._append_y_attr_expression(
            expression=".attr({\n",
            indent_num=2,
            skip_appending=False,
        )
        assert_y_attr_expression_exists(expression=expression)
