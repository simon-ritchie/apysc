from apysc._display.text_color_css_mixin import TextColorCSSMixIn
from apysc._testing.testing_helper import apply_test_settings
import apysc as ap


class TestTextColorCSSMixIn:
    @apply_test_settings()
    def test__initialize_color(self) -> None:
        mixin: TextColorCSSMixIn = TextColorCSSMixIn()
        mixin._initialize_color()
        assert mixin._color == ap.Color("")

        mixin._color = ap.Color("#00aaff")
        mixin._initialize_color()
        assert mixin._color == ap.Color("#00aaff")
