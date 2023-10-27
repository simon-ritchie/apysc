import apysc as ap
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
