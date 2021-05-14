from random import randint
from typing import Optional

from retrying import retry

from apysc import LineRoundDotSetting
from apysc.display.line_round_dot_setting_interface import \
    LineRoundDotSettingInterface
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
