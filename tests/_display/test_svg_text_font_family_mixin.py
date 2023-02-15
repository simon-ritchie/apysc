import apysc as ap
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._display.svg_text_font_family_mixin import SVGTextFontFamilyMixIn


class _TestMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameSuffixMixIn,
    SVGTextFontFamilyMixIn,
):
    pass


class TestSVGTextFontFamilyMixIn:
    @apply_test_settings()
    def test__initialize_font_family_if_not_initialized(self) -> None:
        mixin: _TestMixIn = _TestMixIn()
        mixin._variable_name_suffix = "test_suffix"
        mixin._initialize_font_family_if_not_initialized()
        assert mixin._font_family == ap.Array([ap.String("")])
        assert "font_family" in mixin._font_family._variable_name_suffix

        mixin._font_family[0].value = "Impact"
        mixin._initialize_font_family_if_not_initialized()
        assert mixin._font_family == ap.Array([ap.String("Impact")])
