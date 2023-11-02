import apysc as ap
from apysc._display.text_italic_css_mixin import TextItalicCssMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestTextItalicCssMixIn:
    @apply_test_settings()
    def test__initialize_italic(self) -> None:
        mixin: TextItalicCssMixIn = TextItalicCssMixIn()
        mixin._initialize_italic()
        assert not mixin._italic._value

        mixin._italic = ap.Boolean(True)
        mixin._initialize_italic()
        assert mixin._italic._value

    @apply_test_settings()
    def test_italic(self) -> None:
        text: ap.MultiLineText = ap.MultiLineText(
            text="Test text",
        )
        italic: ap.Boolean = ap.Boolean(True)
        text.italic = italic
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{text.variable_name}.css("
        assert expected in expression
        assert f"if ({italic.variable_name}) {{" in expression
        assert "else {" in expression
