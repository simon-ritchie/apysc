from random import randint

from retrying import retry

from apysc.display.line_dot_setting_interface import LineDotSettingInterface
from apysc import LineDotSetting


class TestLineDotSettingInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_dot_setting_if_not_initialized(self) -> None:
        interface = LineDotSettingInterface()
        interface._initialize_line_dot_setting_if_not_initialized()
        assert interface._line_dot_setting is None

        interface._line_dot_setting = LineDotSetting(dot_size=10)
        interface._initialize_line_dot_setting_if_not_initialized()
        assert interface._line_dot_setting.dot_size == 10
