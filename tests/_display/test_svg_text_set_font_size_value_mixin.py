import apysc as ap
from apysc._display.svg_text_font_size_mixin import SvgTextFontSizeMixIn
from apysc._display.svg_text_set_font_size_value_mixin import (
    SvgTextSetFontSizeValueMixIn,
)
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class _TestMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameSuffixMixIn,
    SvgTextFontSizeMixIn,
    SvgTextSetFontSizeValueMixIn,
):
    pass


class TestSvgTextSetFontSizeValueMixIn:
    @apply_test_settings()
    def test__set_font_size_value(self) -> None:
        mixin_1: _TestMixIn = _TestMixIn()
        mixin_1.variable_name = "test_mixin"
        mixin_1._variable_name_suffix = "test_suffix"
        mixin_1._set_font_size_value(font_size=20)
        assert mixin_1.font_size == ap.Int(20)
        assert "test_suffix" in mixin_1.font_size._variable_name_suffix
        assert "font_size" in mixin_1.font_size._variable_name_suffix

        mixin_1._set_font_size_value(font_size=ap.Int(25))
        assert mixin_1.font_size == ap.Int(25)

        mixin_1._set_font_size_value(font_size=None)
        assert mixin_1.font_size == ap.Int(25)

        mixin_2: SvgTextSetFontSizeValueMixIn = SvgTextSetFontSizeValueMixIn()
        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin_2._set_font_size_value,
            match="This method is only supported an ",
            font_size=30,
        )
