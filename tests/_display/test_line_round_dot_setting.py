import apysc as ap
from apysc._testing.testing_helper import apply_test_settings


class TestLineRoundDotSetting:
    @apply_test_settings()
    def test___init__(self) -> None:
        setting: ap.LineRoundDotSetting = ap.LineRoundDotSetting(
            round_size=20, space_size=10, variable_name_suffix="test_setting"
        )
        assert setting._value == {
            "round_size": ap.Int(20),
            "space_size": ap.Int(10),
        }
        assert isinstance(setting["round_size"], ap.Int)
        assert isinstance(setting["space_size"], ap.Int)
        assert setting._variable_name_suffix == "test_setting"
        assert setting.round_size._variable_name_suffix == "test_setting__round_size"
        assert setting.space_size._variable_name_suffix == "test_setting__space_size"

        setting = ap.LineRoundDotSetting(round_size=ap.Int(20), space_size=ap.Int(10))
        assert setting._value == {
            "round_size": ap.Int(20),
            "space_size": ap.Int(10),
        }

    @apply_test_settings()
    def test_round_size(self) -> None:
        setting: ap.LineRoundDotSetting = ap.LineRoundDotSetting(
            round_size=20, space_size=10
        )
        round_size: ap.Int = setting.round_size
        assert round_size == 20
        assert isinstance(round_size, ap.Int)

    @apply_test_settings()
    def test_space_size(self) -> None:
        setting: ap.LineRoundDotSetting = ap.LineRoundDotSetting(
            round_size=20, space_size=10
        )
        space_size: ap.Int = setting.space_size
        assert space_size == 10
        assert isinstance(space_size, ap.Int)
