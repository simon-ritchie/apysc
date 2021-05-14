from apysc import LineRoundDotSetting
from apysc.display.line_round_dot_setting_interface import \
    LineRoundDotSettingInterface


class TestLineRoundDotSettingInterface:

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
