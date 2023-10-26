import pytest

import apysc as ap
from apysc._display.css_interface import CssInterface
from apysc._display.css_mixin import CssMixIn
from apysc._display.text_fill_color_css_mixin import TextFillColorCssMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_mixin import VariableNameMixIn


class _ValidObject(
    TextFillColorCssMixIn,
    CssMixIn,
    CssInterface,
    VariableNameMixIn,
):
    def __init__(self) -> None:
        """
        The class for testing of the `TextFillColorCssMixIn` class.
        """
        self.variable_name = "test_object"


class TestTextFillColorCssMixIn:
    @apply_test_settings()
    def test__initialize_color(self) -> None:
        mixin: TextFillColorCssMixIn = TextFillColorCssMixIn()
        mixin._initialize_fill_color()
        assert mixin._fill_color == ap.Color("")

        mixin._fill_color = ap.Color("#00aaff")
        mixin._initialize_fill_color()
        assert mixin._fill_color == ap.Color("#00aaff")

    @apply_test_settings()
    def test_color(self) -> None:
        valid_object: _ValidObject = _ValidObject()
        color: ap.Color = ap.Color("#00aaff")
        valid_object.fill_color = color
        assert valid_object._fill_color == color

        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{valid_object.variable_name}.css("
        assert expected in expression

        mixin: TextFillColorCssMixIn = TextFillColorCssMixIn()
        with pytest.raises(TypeError):  # type: ignore
            mixin.fill_color = color
