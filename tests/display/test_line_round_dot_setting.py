from random import randint

from retrying import retry

from apysc import LineRoundDotSetting, Int


class TestLineRoundDotSetting:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        setting: LineRoundDotSetting = LineRoundDotSetting(
            round_size=20, space_size=10)
        assert setting._value == {
            'round_size': 20,
            'space_size': 10,
        }
        assert isinstance(setting['round_size'], Int)
        assert isinstance(setting['space_size'], Int)

        setting = LineRoundDotSetting(
            round_size=Int(20), space_size=Int(10))
        assert setting._value == {
            'round_size': 20,
            'space_size': 10,
        }

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_round_size(self) -> None:
        setting: LineRoundDotSetting = LineRoundDotSetting(
            round_size=20, space_size=10)
        round_size: Int = setting.round_size
        assert round_size == 20
        assert isinstance(round_size, Int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_space_size(self) -> None:
        setting: LineRoundDotSetting = LineRoundDotSetting(
            round_size=20, space_size=10)
        space_size: Int = setting.space_size
        assert space_size == 10
        assert isinstance(space_size, Int)
