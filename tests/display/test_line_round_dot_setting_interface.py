from random import randint
from typing import Match, Optional
import re

from retrying import retry

from apysc import LineRoundDotSetting, LineCaps
from apysc.display.line_round_dot_setting_interface import \
    LineRoundDotSettingInterface
from apysc.expression import expression_file_util
from tests.testing_helper import assert_raises


class TestLineRoundDotSettingInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_round_dot_setting_if_not_initialized(
            self) -> None:
        interface: LineRoundDotSettingInterface = \
            LineRoundDotSettingInterface()
        interface._initialize_line_round_dot_setting_if_not_initialized()
        assert interface._line_round_dot_setting is None

        interface._line_round_dot_setting = LineRoundDotSetting(
            round_size=10, space_size=5)
        interface._initialize_line_round_dot_setting_if_not_initialized()
        assert isinstance(
            interface._line_round_dot_setting, LineRoundDotSetting)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_round_dot_setting(self) -> None:
        interface: LineRoundDotSettingInterface = \
            LineRoundDotSettingInterface()
        line_round_dot_setting: Optional[LineRoundDotSetting] = \
            interface.line_round_dot_setting
        assert line_round_dot_setting is None

        interface._line_round_dot_setting = LineRoundDotSetting(
            round_size=10, space_size=5)
        line_round_dot_setting = interface.line_round_dot_setting
        assert isinstance(line_round_dot_setting, LineRoundDotSetting)

        interface.variable_name = 'test_line_round_dot_setting_interface'
        line_round_dot_setting = LineRoundDotSetting(
            round_size=10, space_size=5)
        interface.line_round_dot_setting = line_round_dot_setting
        assert interface.line_round_dot_setting == line_round_dot_setting
        assert interface.line_cap.value == LineCaps.ROUND.value
        assert interface.line_thickness == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__update_line_round_dot_setting_and_skip_appending_exp(
            self) -> None:
        interface: LineRoundDotSettingInterface = \
            LineRoundDotSettingInterface()
        line_round_dot_setting: LineRoundDotSetting = LineRoundDotSetting(
            round_size=10, space_size=5)
        interface._update_line_round_dot_setting_and_skip_appending_exp(
            value=line_round_dot_setting)
        assert interface._line_round_dot_setting == line_round_dot_setting

        interface._update_line_round_dot_setting_and_skip_appending_exp(
            value=None)
        assert interface._line_round_dot_setting is None

        assert_raises(
            expected_error_class=TypeError,
            func_or_method=interface.
            _update_line_round_dot_setting_and_skip_appending_exp,
            kwargs={'value': 10},
            match=r'Not supported line_round_dot_setting type specified: ')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_line_round_dot_setting_update_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface: LineRoundDotSettingInterface = \
            LineRoundDotSettingInterface()
        interface.variable_name = 'test_line_round_dot_setting_interface'
        line_round_dot_setting: LineRoundDotSetting = LineRoundDotSetting(
            round_size=10, space_size=5)
        interface.line_round_dot_setting = line_round_dot_setting
        expression: str = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'{interface.variable_name}.css\("stroke-dasharray", '
                rf'"1 " \+ String\(.+? \+ .+?\)\);'
            ),
            string=expression,
            flags=re.MULTILINE)
        assert match is not None

        expression_file_util.remove_expression_file()
        interface.line_round_dot_setting = None
        expression = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.css'
            f'("stroke-dasharray", "");'
        )
        assert expected in expression
