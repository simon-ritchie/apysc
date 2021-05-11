from random import randint
from typing import Optional

from retrying import retry

from apysc.display.line_dash_setting_interface import LineDashSettingInterface
from apysc.display.line_dash_setting import LineDashSetting


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
        line_dash_setting: Optional[LineDashSetting] = \
            interface.line_dash_setting
        assert line_dash_setting is None

        interface._line_dash_setting = LineDashSetting(
            dash_size=10, space_size=5)
        line_dash_setting = interface.line_dash_setting
        assert line_dash_setting.dash_size == 10
