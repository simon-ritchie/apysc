import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._display.svg_text_leading_mixin import SVGTextLeadingMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class _TestMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameSuffixMixIn,
    SVGTextLeadingMixIn,
):
    pass


class TestSVGTextLeadingMixIn:

    @apply_test_settings()
    def test_leading(self) -> None:
        expression_data_util.empty_expression()
        mixin: _TestMixIn = _TestMixIn()
        mixin.variable_name = "test_mixin"
        mixin._variable_name_suffix = "test_suffix"
        mixin._leading = 1.8
        leading: ap.Number = mixin.leading
        assert leading == ap.Number(1.8)
        assert "test_suffix" in leading.variable_name
        assert "leading" in leading.variable_name
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{leading.variable_name} = {mixin.variable_name}.font("leading");'
        )
        assert expected in expression

        leading = ap.Number(1.5)
        mixin.leading = leading
        assert mixin._leading == ap.Number(1.5)
        expression = expression_data_util.get_current_expression()
        expected = (
            f'{mixin.variable_name}.font("leading", {leading.variable_name});'
        )
        assert expected in expression
