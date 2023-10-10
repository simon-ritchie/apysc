import apysc as ap
from apysc._display.svg_foreign_object import SVGForeignObject
from apysc._expression import expression_data_util, var_names
from apysc._testing.testing_helper import apply_test_settings
import re
from typing import Match, Optional


class TestSVGForeignObject:
    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        foreign_object: SVGForeignObject = SVGForeignObject(
            width=100, height=150,
        )
        stage: ap.Stage = ap.get_stage()
        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{foreign_object.variable_name} = "
                rf"{stage.variable_name}.foreignObject\("
                rf"{var_names.INT}_\d+?, {var_names.INT}_\d+?\);"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

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
    def test__make_snapshot_and__revert(self) -> None:
        foreign_object: SVGForeignObject = SVGForeignObject(
            width=100,
            height=150,
            variable_name_suffix="test_suffix",
        )
        snapshot_name: str = foreign_object._get_next_snapshot_name()
        foreign_object._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        foreign_object._width._value = 200
        foreign_object._height._value = 250
        foreign_object._run_all_revert_methods(snapshot_name=snapshot_name)
        assert foreign_object._width._value == 100
        assert foreign_object._height._value == 150

    @apply_test_settings()
    def test__initialize_with_base_value(self) -> None:
        foreign_object: SVGForeignObject = (
            SVGForeignObject._initialize_with_base_value()
        )
        assert foreign_object._width == 0
        assert foreign_object._height == 0
