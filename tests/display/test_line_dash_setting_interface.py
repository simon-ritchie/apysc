import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

from apysc.display.line_dash_setting import LineDashSetting
from apysc.display.line_dash_setting_interface import LineDashSettingInterface
from apysc.expression import expression_file_util
from tests.testing_helper import assert_raises


class TestLineDashSettingInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_dash_setting_if_not_initialized(self) -> None:
        interface: LineDashSettingInterface = LineDashSettingInterface()
        interface._initialize_line_dash_setting_if_not_initialized()
        assert interface._line_dash_setting is None

        interface._line_dash_setting = LineDashSetting(
            dash_size=10, space_size=5)
        interface._initialize_line_dash_setting_if_not_initialized()
        assert interface._line_dash_setting.dash_size == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_dash_setting(self) -> None:
        interface: LineDashSettingInterface = LineDashSettingInterface()
        interface.variable_name = 'test_line_dash_setting_interface'
        line_dash_setting: Optional[LineDashSetting] = \
            interface.line_dash_setting
        assert line_dash_setting is None

        interface._line_dash_setting = LineDashSetting(
            dash_size=10, space_size=5)
        line_dash_setting = interface.line_dash_setting
        assert line_dash_setting.dash_size == 10  # type: ignore

        interface.line_dash_setting = LineDashSetting(
            dash_size=5, space_size=3)
        line_dash_setting = interface.line_dash_setting
        assert line_dash_setting.dash_size == 5

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__update_line_dash_setting_and_skip_appending_exp(self) -> None:
        expression_file_util.remove_expression_file()
        interface: LineDashSettingInterface = LineDashSettingInterface()
        assert_raises(
            expected_error_class=TypeError,
            func_or_method=interface.
            _update_line_dash_setting_and_skip_appending_exp,
            kwargs={'value': 'dash'},
            match='Not supported line_dash_setting type specified: ')

        interface._update_line_dash_setting_and_skip_appending_exp(
            value=LineDashSetting(dash_size=10, space_size=5))
        line_dash_setting: Optional[LineDashSetting] = \
            interface.line_dash_setting
        assert line_dash_setting.dash_size == 10  # type: ignore
        expression: str = expression_file_util.get_current_expression()
        assert '.css(' not in expression

        interface._update_line_dash_setting_and_skip_appending_exp(
            value=None)
        line_dash_setting = interface.line_dash_setting
        assert line_dash_setting is None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_line_dash_setting_update_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface: LineDashSettingInterface = LineDashSettingInterface()
        interface._initialize_line_dash_setting_if_not_initialized()
        interface.variable_name = 'test_line_dash_interface'
        interface._append_line_dash_setting_update_expression()
        expression: str = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'{interface.variable_name}.css\("stroke-dasharray", ""\);'
            ),
            string=expression, flags=re.MULTILINE)
        assert match is not None

        expression_file_util.remove_expression_file()
        interface._line_dash_setting = LineDashSetting(
            dash_size=10, space_size=5)
        interface._append_line_dash_setting_update_expression()
        expression = expression_file_util.get_current_expression()
        match = re.search(
            pattern=(
                rf'{interface.variable_name}.css\("stroke-dasharray", '
                rf'String\(.+?\) \+ " " \+ String\(.+\)\);'
            ),
            string=expression, flags=re.MULTILINE)
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: LineDashSettingInterface = LineDashSettingInterface()
        interface.variable_name = 'test_line_dash_setting_interface'
        interface.line_dash_setting = LineDashSetting(
            dash_size=10, space_size=5)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert isinstance(
            interface._line_dash_setting_snapshots[snapshot_name],
            LineDashSetting)

        interface.line_dash_setting = None
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert isinstance(
            interface._line_dash_setting_snapshots[snapshot_name],
            LineDashSetting)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: LineDashSettingInterface = LineDashSettingInterface()
        interface.variable_name = 'test_line_dash_setting_interface'
        interface.line_dash_setting = LineDashSetting(
            dash_size=10, space_size=5)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.line_dash_setting = None
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert isinstance(interface._line_dash_setting, LineDashSetting)
