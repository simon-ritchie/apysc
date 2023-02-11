import apysc as ap
from apysc._testing.testing_helper import apply_test_settings
from apysc._expression import expression_data_util
from apysc._display.svg_text_text_mixin import SvgTextTextMixIn


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
        mixin: SvgTextTextMixIn = SvgTextTextMixIn()
        mixin.variable_name = "test_mixin"
        mixin._text = "Lorem ipsum"
        text: ap.String = mixin.text
        assert text._value == "Lorem ipsum"
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{text.variable_name} = {mixin._variable_name}.text();"
        assert expected in expression

        mixin.text = ap.String("test text")
        assert mixin._text == "test text"
        expression = expression_data_util.get_current_expression()
        expected = f"{mixin.variable_name}.text({text.variable_name});"

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
