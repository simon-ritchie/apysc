import apysc as ap
from apysc._display.line_dot_setting import LineDotSetting
from apysc._testing.testing_helper import apply_test_settings


class TestLineDotSetting:
    @apply_test_settings()
    def test___init__(self) -> None:
        setting: LineDotSetting = LineDotSetting(
            dot_size=5, variable_name_suffix="test_setting"
        )
        assert isinstance(setting._value["dot_size"], ap.Int)
        assert setting._value["dot_size"] == 5
        assert setting._variable_name_suffix == "test_setting"
        assert setting["dot_size"]._variable_name_suffix == "test_setting__dot_size"

        setting = LineDotSetting(dot_size=ap.Int(10))
        assert setting._value["dot_size"] == 10

    @apply_test_settings()
    def test_dot_size(self) -> None:
        setting: LineDotSetting = LineDotSetting(dot_size=5)
        assert setting.dot_size == 5
        assert isinstance(setting.dot_size, ap.Int)
