from random import randint
from typing import Optional

from retrying import retry

from apysc import LineRoundDotSetting
from apysc.display.line_round_dot_setting_interface import \
    LineRoundDotSettingInterface


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
