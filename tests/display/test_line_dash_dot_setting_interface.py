from random import randint

from retrying import retry

from apysc import LineDashDotSetting
from apysc.display.line_dash_dot_setting_interface import \
    LineDashDotSettingInterface


class TestLineDashDotSettingInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_dash_dot_setting_if_not_initialized(
            self) -> None:
        interface: LineDashDotSettingInterface = LineDashDotSettingInterface()
        interface._initialize_line_dash_dot_setting_if_not_initialized()
        assert interface._line_dash_dot_setting is None

        interface._line_dash_dot_setting = LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=7)
        interface._initialize_line_dash_dot_setting_if_not_initialized()
        assert isinstance(
            interface._line_dash_dot_setting, LineDashDotSetting)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_dash_dot_setting(self) -> None:
        interface: LineDashDotSettingInterface = LineDashDotSettingInterface()
        line_dash_dot_setting: LineDashDotSetting = LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=7)
        interface._line_dash_dot_setting = line_dash_dot_setting
        assert interface.line_dash_dot_setting == line_dash_dot_setting
