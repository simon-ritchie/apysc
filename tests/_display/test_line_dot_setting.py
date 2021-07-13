from random import randint

from retrying import retry

import apysc as ap
from apysc._display.line_dot_setting import LineDotSetting


class TestLineDotSetting:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        setting: LineDotSetting = LineDotSetting(dot_size=5)
        assert isinstance(setting._value['dot_size'], ap.Int)
        assert setting._value['dot_size'] == 5

        setting = LineDotSetting(dot_size=ap.Int(10))
        assert setting._value['dot_size'] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_dot_size(self) -> None:
        setting: LineDotSetting = LineDotSetting(dot_size=5)
        assert setting.dot_size == 5
        assert isinstance(setting.dot_size, ap.Int)
