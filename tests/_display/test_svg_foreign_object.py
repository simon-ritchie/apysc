import apysc as ap
from apysc._display.svg_foreign_object import SVGForeignObject
from apysc._display.svg_foreign_object_child import SVGForeignObjectChild
from apysc._expression import expression_data_util, var_names
from apysc._testing.testing_helper import apply_test_settings
import re
from typing import Match, Optional


class TestSVGForeignObject:

    @apply_test_settings()
    def test___init__(self) -> None:
        foreign_object: SVGForeignObject = SVGForeignObject(
            width=100,
            height=150,
            variable_name_suffix="test_suffix",
        )
        stage: ap.Stage = ap.get_stage()
        assert f"{var_names.SVG_FOREIGN_OBJECT}_" in foreign_object.variable_name
        assert foreign_object._width._value == 100
        assert foreign_object._height._value == 150
        assert foreign_object.parent == stage
        assert foreign_object._variable_name_suffix == "test_suffix"
        assert "width" in foreign_object._width.variable_name
        assert "height" in foreign_object._height.variable_name

    @apply_test_settings()
    def test__initialize_with_base_value(self) -> None:
        foreign_object: SVGForeignObject = (
            SVGForeignObject._initialize_with_base_value()
        )
        assert foreign_object._width == 0
        assert foreign_object._height == 0
