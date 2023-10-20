from apysc._display.multi_line_text import MultiLineText
from apysc._testing.testing_helper import apply_test_settings
import apysc as ap


class TestSVGForeignObjectTextMixIn:
    @apply_test_settings()
    def test__initialize_text(self) -> None:
        text: MultiLineText = MultiLineText(
            text="test text",
            width=100,
            variable_name_suffix="test_suffix",
        )
        assert isinstance(text._text, ap.String)
        assert text._text.value == "test text"
        assert "test_suffix" in text._text.variable_name
        assert "text" in text._text.variable_name
