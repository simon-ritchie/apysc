import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._display.line_dot_setting_interface import LineDotSettingInterface
from apysc._expression import expression_file_util
from apysc._expression import var_names
from tests.testing_helper import assert_raises


class TestLineDotSettingInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_dot_setting_if_not_initialized(self) -> None:
        interface: LineDotSettingInterface = LineDotSettingInterface()
        interface._initialize_line_dot_setting_if_not_initialized()
        assert interface._line_dot_setting is None

        interface._line_dot_setting = ap.LineDotSetting(dot_size=10)
        interface._initialize_line_dot_setting_if_not_initialized()
        assert interface._line_dot_setting.dot_size == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_dot_setting(self) -> None:
        interface: LineDotSettingInterface = LineDotSettingInterface()
        interface.variable_name = 'test_line_dot_setting_interface'
        line_dot_setting: Optional[ap.LineDotSetting] = \
            interface.line_dot_setting
        assert line_dot_setting is None

        interface._line_dot_setting = ap.LineDotSetting(dot_size=10)
        line_dot_setting = interface.line_dot_setting
        assert line_dot_setting.dot_size == 10  # type: ignore

        interface.line_dot_setting = None
        line_dot_setting = interface.line_dot_setting
        assert line_dot_setting is None

        interface.line_dot_setting = ap.LineDotSetting(dot_size=20)
        line_dot_setting = interface.line_dot_setting
        assert line_dot_setting.dot_size == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_line_dot_setting_update_expression(self) -> None:
        expression_file_util.empty_expression_dir()
        interface: LineDotSettingInterface = LineDotSettingInterface()
        interface.variable_name = 'test_line_dot_setting_interface'
        interface._initialize_line_dot_setting_if_not_initialized()
        interface._append_line_dot_setting_update_expression()
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.css("stroke-dasharray", "");'
        )
        assert expected in expression

        expression_file_util.empty_expression_dir()
        interface._line_dot_setting = ap.LineDotSetting(dot_size=10)
        interface._append_line_dot_setting_update_expression()
        expression = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'{interface.variable_name}.css\("stroke-dasharray", '
                rf'{var_names.INT}_.+\);'
            ),
            string=expression, flags=re.MULTILINE)
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__update_line_dot_setting_and_skip_appending_exp(self) -> None:
        expression_file_util.empty_expression_dir()
        interface: LineDotSettingInterface = LineDotSettingInterface()
        interface._update_line_dot_setting_and_skip_appending_exp(
            value=None)
        line_dot_setting: Optional[ap.LineDotSetting] = \
            interface.line_dot_setting
        assert line_dot_setting is None
        expression: str = expression_file_util.get_current_expression()
        assert '.css' not in expression

        interface._update_line_dot_setting_and_skip_appending_exp(
            value=ap.LineDotSetting(dot_size=10))
        line_dot_setting = interface.line_dot_setting
        assert line_dot_setting.dot_size == 10  # type: ignore

        assert_raises(
            expected_error_class=TypeError,
            func_or_method=interface.
            _update_line_dot_setting_and_skip_appending_exp,
            kwargs={'value': 10},
            match='Not supported line_dot_setting type specified: ')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: LineDotSettingInterface = LineDotSettingInterface()
        interface.variable_name = 'test_line_dot_setting_interface'
        interface.line_dot_setting = ap.LineDotSetting(dot_size=10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert isinstance(
            interface._line_dot_setting_snapshots[snapshot_name],
            ap.LineDotSetting)

        interface.line_dot_setting = None
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert isinstance(
            interface._line_dot_setting_snapshots[snapshot_name],
            ap.LineDotSetting)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: LineDotSettingInterface = LineDotSettingInterface()
        interface.variable_name = 'test_line_dot_setting_interface'
        interface.line_dot_setting = ap.LineDotSetting(dot_size=10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.line_dot_setting = None
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert isinstance(interface.line_dot_setting, ap.LineDotSetting)

        interface.line_dot_setting = None
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.line_dot_setting is None
