from apysc import LineRoundDotSetting, Int


class TestLineRoundDotSetting:

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
