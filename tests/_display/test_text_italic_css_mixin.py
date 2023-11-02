import apysc as ap
from apysc._display.text_italic_css_mixin import TextItalicCssMixIn
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
