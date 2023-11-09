import apysc as ap
from apysc._display.text_decoration_underline_css_mixin import (
    TextDecorationUnderlineCssMixIn,
)
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestTextDecorationUnderlineCssMixIn:
    @apply_test_settings()
    def test__initialize_underline(self) -> None:
        mixin: TextDecorationUnderlineCssMixIn = TextDecorationUnderlineCssMixIn()
        mixin._initialize_underline()
        assert not mixin._underline._value

        mixin._underline._value = True
        mixin._initialize_underline()
        assert mixin._underline._value

    @apply_test_settings()
    def test_underline(self) -> None:
        text: ap.MultiLineText = ap.MultiLineText(
            text="Test text.",
        )
        underline: ap.Boolean = ap.Boolean(True)
        text.underline = underline
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{text.variable_name}.css("
        assert expected in expression
        assert f"if ({underline.variable_name}) {{" in expression
        assert "else {" in expression
