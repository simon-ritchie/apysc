import apysc as ap
from apysc._display.svg_text_set_text_value_mixin import SVGTextSetTextValueMixIn
from apysc._testing.testing_helper import apply_test_settings, assert_raises
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._display.svg_text_text_mixin import SVGTextTextMixIn


class _TestMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameSuffixMixIn,
    SVGTextTextMixIn,
    SVGTextSetTextValueMixIn,
):
    pass


class TestSVGTextSetTextValueMixIn:
    @apply_test_settings()
    def test__set_text_value(self) -> None:
        mixin_1: _TestMixIn = _TestMixIn()
        mixin_1.variable_name = "test_mixin"
        mixin_1._variable_name_suffix = "test_suffix"
        mixin_1._set_text_value(text="test text 1")
        assert mixin_1.text == ap.String("test text 1")
        assert "test_suffix" in mixin_1.text._variable_name_suffix
        assert "text" in mixin_1.text._variable_name_suffix

        mixin_1._set_text_value(text=ap.String("test text 2"))
        assert mixin_1.text == ap.String("test text 2")

        mixin_2: SVGTextSetTextValueMixIn = SVGTextSetTextValueMixIn()
        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin_2._set_text_value,
            match="This method is only supported a ",
            text="test text 3",
        )
