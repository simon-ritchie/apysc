import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._display.svg_text_italic_mixin import SVGTextItalicMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class _TestMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameSuffixMixIn,
    SVGTextItalicMixIn,
):
    pass


class TestSVGTextItalicMixIn:
    @apply_test_settings()
    def test_italic(self) -> None:
        expression_data_util.empty_expression()
        mixin: _TestMixIn = _TestMixIn()
        mixin.variable_name = "test_mixin"
        mixin._variable_name_suffix = "test_suffix"
        italic: ap.Boolean = mixin.italic
        assert not italic
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{italic.variable_name} = {mixin.variable_name}.font("style") '
            '=== "italic";'
        )
        assert expected in expression
