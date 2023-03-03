import apysc as ap
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._expression import expression_data_util
from apysc._display.svg_text_set_leading_mixin import SVGTextSetLeadingMixIn
from apysc._display.svg_text_leading_mixin import SVGTextLeadingMixIn
from apysc._testing.testing_helper import apply_test_settings, assert_raises


class _TestMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameSuffixMixIn,
    SVGTextLeadingMixIn,
    SVGTextSetLeadingMixIn,
):
    pass


class TestSVGTextSetLeadingMixIn:
    @apply_test_settings()
    def test__set_leading(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: SVGTextSetLeadingMixIn = SVGTextSetLeadingMixIn()
        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin_1._set_leading,
            leading=1.5,
        )

        mixin_2: _TestMixIn = _TestMixIn()
        mixin_2._set_leading(leading=1.8)
        assert mixin_2.leading == ap.Number(1.8)
        expression: str = expression_data_util.get_current_expression()
        assert '.font("leading",' in expression

        expression_data_util.empty_expression()
        mixin_2._set_leading(leading=ap.Number(2.0))
        assert mixin_2.leading == ap.Number(2.0)
        expression = expression_data_util.get_current_expression()
        assert '.font("leading",' in expression
