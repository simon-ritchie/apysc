from apysc import LineDashDotSetting


class TestLineDashDotSetting:

    def test___init__(self) -> None:
        setting: LineDashDotSetting = LineDashDotSetting(
            dot_size=5, dash_size=20, space_size=7)
        assert setting['dot_size'] == 5
        assert setting['dash_size'] == 20
        assert setting['space_size'] == 7
