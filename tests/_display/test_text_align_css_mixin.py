import apysc as ap
from apysc._display.text_align_css_mixin import TextAlignCssMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestTextAlignCssMixIn:
    @apply_test_settings()
    def test_text_align(self) -> None:
        text: ap.MultiLineText = ap.MultiLineText(text="test text")
        text.text_align = ap.CssTextAlign.CENTER
        assert text.text_align == ap.CssTextAlign.CENTER
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{text.variable_name}.css("
        assert expected in expression
