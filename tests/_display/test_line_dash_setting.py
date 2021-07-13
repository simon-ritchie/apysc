from random import randint

from retrying import retry

import apysc as ap


class TestLineDashSetting:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        setting: ap.LineDashSetting = ap.LineDashSetting(
            dash_size=10, space_size=5)
        assert setting._value['dash_size'] == 10
        assert isinstance(setting._value['dash_size'], ap.Int)
        assert setting._value['space_size'] == 5
        assert isinstance(setting._value['space_size'], ap.Int)

        dash_size: ap.Int = ap.Int(15)
        space_size: ap.Int = ap.Int(3)
        setting = ap.LineDashSetting(
            dash_size=dash_size, space_size=space_size)
        assert setting._value['dash_size'].variable_name != \
            dash_size.variable_name
        assert setting._value['space_size'].variable_name != \
            space_size.variable_name

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_dash_size(self) -> None:
        setting: ap.LineDashSetting = ap.LineDashSetting(
            dash_size=10, space_size=5)
        assert setting.dash_size == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_space_size(self) -> None:
        setting: ap.LineDashSetting = ap.LineDashSetting(
            dash_size=10, space_size=5)
        assert setting.space_size == 5
