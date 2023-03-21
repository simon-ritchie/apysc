import apysc as ap
from apysc._display.svg_text_font_family_mixin import SVGTextFontFamilyMixIn
from apysc._display.svg_text_set_font_family_mixin import SVGTextSetFontFamilyMixIn
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
    SVGTextFontFamilyMixIn,
    SVGTextSetFontFamilyMixIn,
):
    pass


class TestSVGTextSetFontFamilyMixIn:
    @apply_test_settings()
    def test__set_font_family(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: SVGTextSetFontFamilyMixIn = SVGTextSetFontFamilyMixIn()
        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin_1._set_font_family,
            match="This method is only supported an ",
            font_family=None,
        )

        mixin_2: _TestMixIn = _TestMixIn()
        mixin_2.variable_name = "test_mixin"
        mixin_2._variable_name_suffix = "test_suffix"
        mixin_2._set_font_family(font_family=None)
        expression: str = expression_data_util.get_current_expression()
        assert "family" not in expression

        mixin_2._set_font_family(font_family=["Impact", "Arial"])
        expression = expression_data_util.get_current_expression()
        assert "family" in expression

        expression_data_util.empty_expression()
        mixin_2._set_font_family(
            font_family=ap.Array([ap.String("Impact"), ap.String("Times New Roman")])
        )
        expression = expression_data_util.get_current_expression()
        assert "family" in expression
