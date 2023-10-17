import apysc as ap
from apysc._display.svg_foreign_object_initialize_width_and_height_mixin import (
    SVGForeignObjectInitializeWidthAndHeightMixIn
)
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._display.width_mixin import WidthMixIn



class _TestObject(
    WidthMixIn,
    VariableNameSuffixMixIn,
    SVGForeignObjectInitializeWidthAndHeightMixIn,
):
    def __init__(self) -> None:
        self.variable_name = "test_object"
        self._variable_name_suffix = "test_suffix"


class TestSVGForeignObjectInitializeWidthAndHeightMixIn:
    @apply_test_settings()
    def test__initialize_width_and_height(self) -> None:
        test_object: _TestObject = _TestObject()
        test_object._initialize_width_and_height(width=100, height=200)
        assert test_object._width._value == 100
        assert "test_suffix" in test_object._width.variable_name
        assert "width" in test_object._width.variable_name
        assert test_object._height._value == 200
        assert "test_suffix" in test_object._height.variable_name
        assert "height" in test_object._height.variable_name
