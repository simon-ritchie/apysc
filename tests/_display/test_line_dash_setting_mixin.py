import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

from apysc._display.line_dash_setting import LineDashSetting
from apysc._display.line_dash_setting_mixin import LineDashSettingMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import assert_raises


class TestLineDashSettingMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_dash_setting_if_not_initialized(self) -> None:
        interface: LineDashSettingMixIn = LineDashSettingMixIn()
        interface._initialize_line_dash_setting_if_not_initialized()
        assert interface._line_dash_setting is None

        interface._line_dash_setting = LineDashSetting(dash_size=10, space_size=5)
        interface._initialize_line_dash_setting_if_not_initialized()
        assert interface._line_dash_setting.dash_size == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_dash_setting(self) -> None:
        interface: LineDashSettingMixIn = LineDashSettingMixIn()
        interface.variable_name = "test_line_dash_setting_interface"
        line_dash_setting: Optional[LineDashSetting] = interface.line_dash_setting
        assert line_dash_setting is None

        interface._line_dash_setting = LineDashSetting(dash_size=10, space_size=5)
        line_dash_setting = interface.line_dash_setting
        assert line_dash_setting.dash_size == 10  # type: ignore

        interface.line_dash_setting = LineDashSetting(dash_size=5, space_size=3)
        line_dash_setting = interface.line_dash_setting
        assert line_dash_setting.dash_size == 5  # type: ignore

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__update_line_dash_setting_and_skip_appending_exp(self) -> None:
        expression_data_util.empty_expression()
        interface: LineDashSettingMixIn = LineDashSettingMixIn()
        assert_raises(
            expected_error_class=TypeError,
            callable_=interface._update_line_dash_setting_and_skip_appending_exp,
            match="Not supported line_dash_setting type specified: ",
            value="dash",
        )

        interface._update_line_dash_setting_and_skip_appending_exp(
            value=LineDashSetting(dash_size=10, space_size=5)
        )
        line_dash_setting: Optional[LineDashSetting] = interface.line_dash_setting
        assert line_dash_setting.dash_size == 10  # type: ignore
        expression: str = expression_data_util.get_current_expression()
        assert ".css(" not in expression

        interface._update_line_dash_setting_and_skip_appending_exp(value=None)
        line_dash_setting = interface.line_dash_setting
        assert line_dash_setting is None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_line_dash_setting_update_expression(self) -> None:
        expression_data_util.empty_expression()
        interface: LineDashSettingMixIn = LineDashSettingMixIn()
        interface._initialize_line_dash_setting_if_not_initialized()
        interface.variable_name = "test_line_dash_interface"
        interface._append_line_dash_setting_update_expression()
        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(rf'{interface.variable_name}.css\("stroke-dasharray", ""\);'),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

        expression_data_util.empty_expression()
        interface._line_dash_setting = LineDashSetting(dash_size=10, space_size=5)
        interface._append_line_dash_setting_update_expression()
        expression = expression_data_util.get_current_expression()
        match = re.search(
            pattern=(
                rf'{interface.variable_name}.css\("stroke-dasharray", '
                rf'String\(.+?\) \+ " " \+ String\(.+\)\);'
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: LineDashSettingMixIn = LineDashSettingMixIn()
        interface.variable_name = "test_line_dash_setting_interface"
        interface.line_dash_setting = LineDashSetting(dash_size=10, space_size=5)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert isinstance(
            interface._line_dash_setting_snapshots[snapshot_name], LineDashSetting
        )

        interface.line_dash_setting = None
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert isinstance(
            interface._line_dash_setting_snapshots[snapshot_name], LineDashSetting
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: LineDashSettingMixIn = LineDashSettingMixIn()
        interface.variable_name = "test_line_dash_setting_interface"
        interface.line_dash_setting = LineDashSetting(dash_size=10, space_size=5)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.line_dash_setting = None
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert isinstance(interface._line_dash_setting, LineDashSetting)