import apysc as ap
from apysc._display.append_line_cap_attr_expression_mixin import (
    AppendLineCapAttrExpressionMixIn,
)
from apysc._display.line_cap_mixin import LineCapMixIn
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from tests._display.test_graphics_expression import (
    assert_stroke_linecap_attr_expression_exists,
)


class _TestObject(
    AppendLineCapAttrExpressionMixIn,
    LineCapMixIn,
    VariableNameMixIn,
    VariableNameSuffixMixIn,
    VariableNameSuffixAttrOrVarMixIn,
):
    pass


class TestAppendLineCapAttrExpressionMixIn:
    @apply_test_settings()
    def test__append_line_cap_attr_expression(self) -> None:
        instance_1: AppendLineCapAttrExpressionMixIn = (
            AppendLineCapAttrExpressionMixIn()
        )
        assert_raises(
            expected_error_class=TypeError,
            callable_=instance_1._append_line_cap_attr_expression,
            match="This instance is not a ",
            expression=".attr({\n",
            indent_num=2,
            skip_appending=False,
        )

        instance_2: _TestObject = _TestObject()
        instance_2.line_cap = ap.LineCaps.ROUND
        expression: str = instance_2._append_line_cap_attr_expression(
            expression=".attr({\n",
            indent_num=2,
            skip_appending=True,
        )
        assert expression == ".attr({\n"

        expression = instance_2._append_line_cap_attr_expression(
            expression=".attr({\n",
            indent_num=2,
            skip_appending=False,
        )
        assert_stroke_linecap_attr_expression_exists(expression=expression)
