import apysc as ap
from apysc._display.svg_text_italic_mixin import SVGTextItalicMixIn
from apysc._display.svg_text_set_italic_mixin import SVGTextSetItalicMixIn
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
    SVGTextItalicMixIn,
    SVGTextSetItalicMixIn,
):
    pass


class TestSVGTextSetItalicMixIn:
    @apply_test_settings()
    def test__set_italic(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: SVGTextSetItalicMixIn = SVGTextSetItalicMixIn()
        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin_1._set_italic,
            match="This method is only supported a ",
            italic=True,
        )

        expression_data_util.empty_expression()
        mixin_2: _TestMixIn = _TestMixIn()
        mixin_2.variable_name = "test_mixin"
        mixin_2._set_italic(italic=True)
        assert mixin_2.italic
        expression: str = expression_data_util.get_current_expression()
        expected: str = f'{mixin_2.variable_name}.font("style", "italic");'
        assert expected in expression

        mixin_2.italic = ap.Boolean(False)
        expression_data_util.empty_expression()
        mixin_2._set_italic(italic=ap.Boolean(True))
        assert mixin_2.italic
        expression = expression_data_util.get_current_expression()
        expected = f'{mixin_2.variable_name}.font("style", "italic");'
        assert expected in expression

        expression_data_util.empty_expression()
        mixin_2._set_italic(italic=None)
        expression = expression_data_util.get_current_expression()
        assert ".font" not in expression
