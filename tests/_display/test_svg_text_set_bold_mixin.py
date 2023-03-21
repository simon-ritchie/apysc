import apysc as ap
from apysc._display.svg_text_bold_mixin import SVGTextBoldMixIn
from apysc._display.svg_text_set_bold_mixin import SVGTextSetBoldMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class _TestMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameSuffixMixIn,
    SVGTextBoldMixIn,
    SVGTextSetBoldMixIn,
):
    pass


class TestSVGTextSetBoldMixIn:
    @apply_test_settings()
    def test__set_bold(self) -> None:
        mixin_1: SVGTextSetBoldMixIn = SVGTextSetBoldMixIn()
        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin_1._set_bold,
            match="This method is only supported an ",
            bold=True,
        )

        expression_data_util.empty_expression()
        mixin_2: _TestMixIn = _TestMixIn()
        mixin_2.variable_name = "test_mixin"
        mixin_2._set_bold(bold=True)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f'{mixin_2.variable_name}.font("weight", "bold");'
        assert expected in expression
        assert mixin_2.bold

        expression_data_util.empty_expression()
        mixin_2.bold = ap.Boolean(False)
        mixin_2._set_bold(bold=ap.Boolean(True))
        expression = expression_data_util.get_current_expression()
        expected = f'{mixin_2.variable_name}.font("weight", "bold");'
        assert expected in expression
        assert mixin_2.bold

        expression_data_util.empty_expression()
        mixin_2._set_bold(bold=None)
        expression = expression_data_util.get_current_expression()
        assert ".font" not in expression
