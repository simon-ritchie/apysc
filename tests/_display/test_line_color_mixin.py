import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._display.line_color_mixin import LineColorMixIn
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings


class TestLineColorMixIn:
    @apply_test_settings()
    def test_line_color(self) -> None:
        line_color_interface: LineColorMixIn = LineColorMixIn()
        line_color_interface.variable_name = "test_line_color_interface"
        line_color_interface.line_color = ap.Color("#555555")
        assert line_color_interface.line_color._value == ap.String("#555555")

        color_1: ap.Color = line_color_interface.line_color
        color_1._value = ap.String("#666666")
        assert line_color_interface.line_color != color_1
        assert (
            line_color_interface.line_color._value.variable_name
            != color_1._value.variable_name
        )

    @apply_test_settings()
    def test__append_line_color_update_expression(self) -> None:
        line_color_interface: LineColorMixIn = LineColorMixIn()
        line_color_interface.variable_name = "test_line_color_interface"
        line_color_interface.line_color = ap.Color("#333")
        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                r"test_line_color_interface\.stroke" rf"\({var_names.STRING}_.+?\);"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @apply_test_settings()
    def test__update_line_color_and_skip_appending_exp(self) -> None:
        line_color_interface: LineColorMixIn = LineColorMixIn()
        line_color_interface.variable_name = "test_line_color_interface"
        line_color_interface._update_line_color_and_skip_appending_exp(
            value=ap.Color("#777")
        )
        assert line_color_interface.line_color._value == ap.String("#777777")
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{line_color_interface.variable_name}.stroke("
        assert expected not in expression

    @apply_test_settings()
    def test__initialize_line_color_if_not_initialized(self) -> None:
        line_color_interface: LineColorMixIn = LineColorMixIn()
        line_color_interface.variable_name = "test_line_color_interface"
        line_color_interface._initialize_line_color_if_not_initialized()
        assert line_color_interface.line_color == ap.COLORLESS
        line_color_interface.line_color = ap.Color("#333")
        line_color_interface._initialize_line_color_if_not_initialized()
        assert line_color_interface.line_color._value == ap.String("#333333")

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        line_color_interface: LineColorMixIn = LineColorMixIn()
        line_color_interface.variable_name = "test_line_color_interface"
        line_color_interface.line_color = ap.Color("#333")
        snapshot_name: str = "snapshot_1"
        line_color_interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if line_color_interface._line_color_snapshots is None:
            raise AssertionError()
        assert line_color_interface._line_color_snapshots[snapshot_name] == "#333333"

        line_color_interface.line_color = ap.Color("#222")
        line_color_interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert line_color_interface._line_color_snapshots[snapshot_name] == "#333333"

    @apply_test_settings()
    def test__revert(self) -> None:
        line_color_interface: LineColorMixIn = LineColorMixIn()
        line_color_interface.variable_name = "test_line_color_interface"
        line_color_interface.line_color = ap.Color("#333")
        snapshot_name: str = "snapshot_1"
        line_color_interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        line_color_interface.line_color = ap.Color("#222")
        line_color_interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert line_color_interface.line_color._value == ap.String("#333333")

        line_color_interface.line_color = ap.Color("#222")
        line_color_interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert line_color_interface.line_color._value == ap.String("#222222")

    @apply_test_settings()
    def test__set_initial_line_color_if_not_colorless(self) -> None:
        line_color_interface: LineColorMixIn = LineColorMixIn()
        line_color_interface.variable_name = "test_line_color_interface"
        line_color_interface._set_initial_line_color_if_not_colorless(
            line_color=ap.COLORLESS
        )
        assert line_color_interface.line_color == ap.COLORLESS

        line_color_interface._set_initial_line_color_if_not_colorless(
            line_color=ap.Color("0af")
        )
        assert line_color_interface.line_color._value == ap.String("#00aaff")
