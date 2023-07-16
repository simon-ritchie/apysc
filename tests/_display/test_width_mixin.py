import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._display.width_mixin import WidthMixIn
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings


class TestWidthMixIn:
    @apply_test_settings()
    def test_width(self) -> None:
        width_interface: WidthMixIn = WidthMixIn()
        width_interface.variable_name = "test_width_interface"
        width_interface.width = ap.Int(100)
        assert width_interface.width == 100

    @apply_test_settings()
    def test__append_width_update_expression(self) -> None:
        width_interface: WidthMixIn = WidthMixIn()
        width_interface.variable_name = "test_width_interface"
        ap.Stage()
        width_interface.width = ap.Int(200)
        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=rf"test_width_interface\.width\({var_names.INT}_.+?\);",
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @apply_test_settings()
    def test_update_width_and_skip_appending_exp(self) -> None:
        width_interface: WidthMixIn = WidthMixIn()
        width_interface.variable_name = "test_width_interface"
        ap.Stage()
        width_interface._update_width_and_skip_appending_exp(value=ap.Int(300))
        assert width_interface.width == 300
        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(rf"width\({var_names.INT}_.+?\)"),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is None

        width_interface._update_width_and_skip_appending_exp(value=400)
        assert width_interface.width == 400

    @apply_test_settings()
    def test__initialize_width_if_not_initialized(self) -> None:
        width_interface: WidthMixIn = WidthMixIn()
        width_interface.variable_name = "test_width_interface"
        width_interface._initialize_width_if_not_initialized()
        assert width_interface.width == 0

        width_interface.width = ap.Int(10)
        width_interface._initialize_width_if_not_initialized()
        assert width_interface.width == 10

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        width_interface: WidthMixIn = WidthMixIn()
        width_interface.variable_name = "test_width_interface"
        width_interface.width = ap.Int(10)
        snapshot_name: str = "snapshot_1"
        width_interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if width_interface._width_snapshots is None:
            raise AssertionError()
        assert width_interface._width_snapshots[snapshot_name] == 10

        width_interface.width = ap.Int(15)
        width_interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert width_interface._width_snapshots[snapshot_name] == 10

    @apply_test_settings()
    def test__revert(self) -> None:
        width_interface: WidthMixIn = WidthMixIn()
        width_interface.variable_name = "test_width_interface"
        width_interface.width = ap.Int(10)
        snapshot_name: str = "snapshot_1"
        width_interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        width_interface.width = ap.Int(15)
        width_interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert width_interface.width == 10

        width_interface.width = ap.Int(15)
        width_interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert width_interface.width == 15

    @apply_test_settings()
    def test__append_width_attr_linking_setting(self) -> None:
        interface: WidthMixIn = WidthMixIn()
        interface.variable_name = "test_width_interface"
        interface._initialize_width_if_not_initialized()
        assert interface._attr_linking_stack["width"] == [ap.Int(0)]
