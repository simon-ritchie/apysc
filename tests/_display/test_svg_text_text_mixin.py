import apysc as ap
from apysc._testing.testing_helper import apply_test_settings
from apysc._expression import expression_data_util
from apysc._display.svg_text_text_mixin import SvgTextTextMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class _TestMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameSuffixMixIn,
    SvgTextTextMixIn,
):
    pass


class TestSvgTextTextMixIn:
    @apply_test_settings()
    def test__append_text_getter_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: SvgTextTextMixIn = SvgTextTextMixIn()
        mixin.variable_name = "test_mixin"
        text: ap.String = ap.String("Lorem ipsum")
        mixin._append_text_getter_expression(text=text)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{text.variable_name} = {mixin._variable_name}.text();"
        assert expected in expression

    @apply_test_settings()
    def test_text(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: SvgTextTextMixIn = SvgTextTextMixIn()
        mixin_1.variable_name = "test_mixin"
        mixin_1._text = "Lorem ipsum"
        text: ap.String = mixin_1.text
        assert text._value == "Lorem ipsum"
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{text.variable_name} = {mixin_1._variable_name}.text();"
        assert expected in expression

        mixin_1.text = ap.String("test text")
        assert mixin_1._text == "test text"
        expression = expression_data_util.get_current_expression()
        expected = f"{mixin_1.variable_name}.text({text.variable_name});"

        mixin_2: _TestMixIn = _TestMixIn()
        mixin_2._variable_name_suffix = "test_suffix"
        mixin_2._text = "Lorem ipsum"
        text: ap.String = mixin_2.text
        assert "test_suffix" in text.variable_name


    @apply_test_settings()
    def test__append_text_setter_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: SvgTextTextMixIn = SvgTextTextMixIn()
        mixin.variable_name = "test_mixin"
        text: ap.String = ap.String("Lorem ipsum")
        mixin._append_text_setter_expression(text=text)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin.variable_name}.text({text.variable_name});"
        assert expected in expression
