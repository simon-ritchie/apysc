import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._display.line_round_dot_setting_interface import \
    LineRoundDotSettingInterface
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import assert_raises


class TestLineRoundDotSettingInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_round_dot_setting_if_not_initialized(
            self) -> None:
        interface: LineRoundDotSettingInterface = \
            LineRoundDotSettingInterface()
        interface._initialize_line_round_dot_setting_if_not_initialized()
        assert interface._line_round_dot_setting is None

        interface._line_round_dot_setting = ap.LineRoundDotSetting(
            round_size=10, space_size=5)
        interface._initialize_line_round_dot_setting_if_not_initialized()
        assert isinstance(
            interface._line_round_dot_setting, ap.LineRoundDotSetting)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_round_dot_setting(self) -> None:
        interface: LineRoundDotSettingInterface = \
            LineRoundDotSettingInterface()
        line_round_dot_setting: Optional[ap.LineRoundDotSetting] = \
            interface.line_round_dot_setting
        assert line_round_dot_setting is None

        interface._line_round_dot_setting = ap.LineRoundDotSetting(
            round_size=10, space_size=5)
        line_round_dot_setting = interface.line_round_dot_setting
        assert isinstance(line_round_dot_setting, ap.LineRoundDotSetting)

        interface.variable_name = 'test_line_round_dot_setting_interface'
        line_round_dot_setting = ap.LineRoundDotSetting(
            round_size=10, space_size=5)
        interface.line_round_dot_setting = line_round_dot_setting
        assert interface.line_round_dot_setting == line_round_dot_setting
        assert interface.line_cap.value == ap.LineCaps.ROUND.value
        assert interface.line_thickness == 10

        interface.line_round_dot_setting = None
        assert interface.line_cap.value == ap.LineCaps.BUTT.value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__update_line_round_dot_setting_and_skip_appending_exp(
            self) -> None:
        interface: LineRoundDotSettingInterface = \
            LineRoundDotSettingInterface()
        line_round_dot_setting: ap.LineRoundDotSetting = \
            ap.LineRoundDotSetting(
                round_size=10, space_size=5)
        interface._update_line_round_dot_setting_and_skip_appending_exp(
            value=line_round_dot_setting)
        assert interface._line_round_dot_setting == line_round_dot_setting

        interface._update_line_round_dot_setting_and_skip_appending_exp(
            value=None)
        assert interface._line_round_dot_setting is None

        assert_raises(
            expected_error_class=TypeError,
            callable_=interface.
            _update_line_round_dot_setting_and_skip_appending_exp,
            kwargs={'value': 10},
            match=r'Not supported line_round_dot_setting type specified: ')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_line_round_dot_setting_update_expression(self) -> None:
        expression_data_util.empty_expression()
        interface: LineRoundDotSettingInterface = \
            LineRoundDotSettingInterface()
        interface.variable_name = 'test_line_round_dot_setting_interface'
        line_round_dot_setting: ap.LineRoundDotSetting = \
            ap.LineRoundDotSetting(round_size=10, space_size=5)
        interface.line_round_dot_setting = line_round_dot_setting
        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'{interface.variable_name}.css\("stroke-dasharray", '
                rf'"1 " \+ String\(.+? \+ .+?\)\);'
            ),
            string=expression,
            flags=re.MULTILINE)
        assert match is not None

        expression_data_util.empty_expression()
        interface.line_round_dot_setting = None
        expression = expression_data_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.css'
            f'("stroke-dasharray", "");'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: LineRoundDotSettingInterface = \
            LineRoundDotSettingInterface()
        interface.variable_name = 'test_line_round_dot_setting_interface'
        line_round_dot_setting: ap.LineRoundDotSetting = \
            ap.LineRoundDotSetting(round_size=10, space_size=5)
        interface.line_round_dot_setting = line_round_dot_setting
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._line_round_dot_setting_snapshots[snapshot_name] == \
            line_round_dot_setting

        interface.line_round_dot_setting = None
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._line_round_dot_setting_snapshots[snapshot_name] == \
            line_round_dot_setting

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: LineRoundDotSettingInterface = \
            LineRoundDotSettingInterface()
        interface.variable_name = 'test_line_round_dot_setting_interface'
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        line_round_dot_setting: ap.LineRoundDotSetting = \
            ap.LineRoundDotSetting(round_size=10, space_size=5)
        interface.line_round_dot_setting = line_round_dot_setting
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.line_round_dot_setting = None
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.line_round_dot_setting == line_round_dot_setting
