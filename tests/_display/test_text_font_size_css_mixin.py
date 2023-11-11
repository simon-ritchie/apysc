from apysc._display.text_font_size_css_mixin import TextFontSizeCssMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
import apysc as ap


class TestTextFontSizeCssMixIn:
    @apply_test_settings()
    def test__initialize_font_size(self) -> None:
        mixin: TextFontSizeCssMixIn = TextFontSizeCssMixIn()
        mixin._initialize_font_size()
        assert mixin._font_size == 16

        mixin._font_size._value = 32
        mixin._initialize_font_size()
        assert mixin._font_size == 32

    @apply_test_settings()
    def test_font_size(self) -> None:
        text: ap.MultiLineText = ap.MultiLineText(text="", width=100)
        text.font_size = ap.Int(32)
        assert text.font_size._value == 32

        expression: str = expression_data_util.get_current_expression()
        assert ".css(" in expression
