import apysc as ap
from apysc._display.css_interface import CssInterface
from apysc._display.css_mixin import CssMixIn
from apysc._display.text_line_height_css_mixin import TextLineHeightCssMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class _TestObject(CssMixIn, CssInterface, TextLineHeightCssMixIn):
    pass


class TestTextLineHeightCssMixIn:
    @apply_test_settings()
    def test__initialize_line_height(self) -> None:
        mixin: TextLineHeightCssMixIn = TextLineHeightCssMixIn()
        mixin._initialize_line_height()
        assert mixin._line_height == 1.5

        mixin._line_height = ap.Number(2.0)
        mixin._initialize_line_height()
        assert mixin._line_height == 2.0

    @apply_test_settings()
    def test_line_height(self) -> None:
        instance: _TestObject = _TestObject()
        assert instance.line_height == 1.5

        instance.line_height = ap.Number(2.0)
        assert instance.line_height == 2.0
        expression: str = expression_data_util.get_current_expression()
        assert ".css(" in expression
