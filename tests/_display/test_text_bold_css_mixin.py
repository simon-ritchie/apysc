import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._display.text_bold_css_mixin import TextBoldCssMixIn


class TestTextBoldCssMixIn:
    @apply_test_settings()
    def test__initialize_bold(self) -> None:
        mixin: TextBoldCssMixIn = TextBoldCssMixIn()
        mixin._initialize_bold()
        assert not mixin._bold._value

        mixin._bold = ap.Boolean(True)
        mixin._initialize_bold()
        assert mixin._bold._value

    @apply_test_settings()
    def test_bold(self) -> None:
        text: ap.MultiLineText = ap.MultiLineText(
            text="Test text",
        )
        bold: ap.Boolean = ap.Boolean(True)
        text.bold = bold
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{text.variable_name}.css("
        assert expected in expression
        assert f"if ({bold.variable_name}) {{" in expression
        assert "else {" in expression
