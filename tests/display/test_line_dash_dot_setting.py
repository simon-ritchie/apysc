from random import randint

from retrying import retry

from apysc import LineDashDotSetting, Int


class TestLineDashDotSetting:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        setting: LineDashDotSetting = LineDashDotSetting(
            dot_size=5, dash_size=20, space_size=7)
        assert setting['dot_size'] == 5
        assert setting['dash_size'] == 20
        assert setting['space_size'] == 7
        assert isinstance(setting['dot_size'], Int)
        assert isinstance(setting['dash_size'], Int)
        assert isinstance(setting['space_size'], Int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_dot_size(self) -> None:
        setting: LineDashDotSetting = LineDashDotSetting(
            dot_size=5, dash_size=20, space_size=7)
        dot_size: Int = setting.dot_size
        assert dot_size == 5
        assert isinstance(dot_size, Int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_dash_size(self) -> None:
        setting: LineDashDotSetting = LineDashDotSetting(
            dot_size=5, dash_size=20, space_size=7)
        dash_size: Int = setting.dash_size
        assert dash_size == 20
        assert isinstance(dash_size, Int)
