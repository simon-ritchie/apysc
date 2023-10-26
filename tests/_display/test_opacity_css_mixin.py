import apysc as ap
from apysc._display.css_interface import CssInterface
from apysc._display.css_mixin import CssMixIn
from apysc._display.opacity_css_mixin import OpacityCssMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_mixin import VariableNameMixIn


class _ValidObject(
    CssMixIn,
    CssInterface,
    OpacityCssMixIn,
    VariableNameMixIn,
):
    def __init__(self) -> None:
        """
        The class for testing of the `FillAlphaCssMixIn` class.
        """
        self.variable_name = "test_object"


class TestFillAlphaCssMixIn:
    @apply_test_settings()
    def test__initialize_fill_alpha(self) -> None:
        mixin: OpacityCssMixIn = OpacityCssMixIn()
        mixin._initialize_fill_alpha()
        assert mixin._fill_alpha == 1.0

        mixin._fill_alpha = ap.Number(0.5)
        mixin._initialize_fill_alpha()
        assert mixin._fill_alpha == 0.5

    @apply_test_settings()
    def test_fill_alpha(self) -> None:
        valid_object: _ValidObject = _ValidObject()
        valid_object.fill_alpha = ap.Number(0.5)
        assert valid_object.fill_alpha == ap.Number(0.5)

        expression: str = expression_data_util.get_current_expression()
        assert ".css(" in expression
