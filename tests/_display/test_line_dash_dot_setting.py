import apysc as ap
from apysc._testing.testing_helper import apply_test_settings


class TestLineDashDotSetting:
    @apply_test_settings()
    def test___init__(self) -> None:
        setting: ap.LineDashDotSetting = ap.LineDashDotSetting(
            dot_size=5, dash_size=20, space_size=7, variable_name_suffix="test_setting"
        )
        assert setting["dot_size"] == 5
        assert setting["dash_size"] == 20
        assert setting["space_size"] == 7
        assert isinstance(setting["dot_size"], ap.Int)
        assert isinstance(setting["dash_size"], ap.Int)
        assert isinstance(setting["space_size"], ap.Int)
        assert setting._variable_name_suffix == "test_setting"
        assert setting["dot_size"]._variable_name_suffix == "test_setting__dot_size"
        assert setting["dash_size"]._variable_name_suffix == "test_setting__dash_size"
        assert setting["space_size"]._variable_name_suffix == "test_setting__space_size"

    @apply_test_settings()
    def test_dot_size(self) -> None:
        setting: ap.LineDashDotSetting = ap.LineDashDotSetting(
            dot_size=5, dash_size=20, space_size=7
        )
        dot_size: ap.Int = setting.dot_size
        assert dot_size == 5
        assert isinstance(dot_size, ap.Int)

    @apply_test_settings()
    def test_dash_size(self) -> None:
        setting: ap.LineDashDotSetting = ap.LineDashDotSetting(
            dot_size=5, dash_size=20, space_size=7
        )
        dash_size: ap.Int = setting.dash_size
        assert dash_size == 20
        assert isinstance(dash_size, ap.Int)

    @apply_test_settings()
    def test_space_size(self) -> None:
        setting: ap.LineDashDotSetting = ap.LineDashDotSetting(
            dot_size=5, dash_size=20, space_size=7
        )
        space_size: ap.Int = setting.space_size
        assert space_size == 7
        assert isinstance(space_size, ap.Int)
