from apysc._display.svg_foreign_object_initialize_width_mixin import (
    SvgForeignObjectInitializeWidthMixIn,
)
from apysc._display.width_mixin import WidthMixIn
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class _TestObject(
    WidthMixIn,
    VariableNameSuffixMixIn,
    SvgForeignObjectInitializeWidthMixIn,
):
    def __init__(self) -> None:
        """
        The class for testing of the `SvgForeignObjectInitializeWidthMixIn`.
        """
        self.variable_name = "test_object"
        self._variable_name_suffix = "test_suffix"


class TestSVGForeignObjectInitializeWidthMixIn:
    @apply_test_settings()
    def test__initialize_width(self) -> None:
        test_object: _TestObject = _TestObject()
        test_object._initialize_width(width=100)
        assert test_object._width._value == 100
        assert "test_suffix" in test_object._width.variable_name
        assert "width" in test_object._width.variable_name
