import pytest
from apysc._display.text_color_css_mixin import TextColorCSSMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
import apysc as ap
from apysc._display.css_mixin import CssMixIn
from apysc._display.css_interface import CssInterface
from apysc._type.variable_name_mixin import VariableNameMixIn


class _ValidObject(
    TextColorCSSMixIn,
    CssMixIn,
    CssInterface,
    VariableNameMixIn,
):
    def __init__(self) -> None:
        """
        The class for testing of the `TextColorCSSMixIn` class.
        """
        self.variable_name = "test_object"


class TestTextColorCSSMixIn:
    @apply_test_settings()
    def test__initialize_color(self) -> None:
        mixin: TextColorCSSMixIn = TextColorCSSMixIn()
        mixin._initialize_color()
        assert mixin._color == ap.Color("")

        mixin._color = ap.Color("#00aaff")
        mixin._initialize_color()
        assert mixin._color == ap.Color("#00aaff")

    @apply_test_settings()
    def test_color(self) -> None:
        valid_object: _ValidObject = _ValidObject()
        color: ap.Color = ap.Color("#00aaff")
        valid_object.color = color
        assert valid_object.color == color

        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{valid_object.variable_name}.css("
        assert expected in expression

        mixin: TextColorCSSMixIn = TextColorCSSMixIn()
        with pytest.raises(TypeError):  # type: ignore
            mixin.color = color
