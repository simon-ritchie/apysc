from random import randint

from retrying import retry

from apysc import Polyline, Stage, Sprite, LineDotSetting, Array, Point2D, LineDashSetting, LineRoundDotSetting, LineDashDotSetting


class TestLineBase:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_line_setting_if_not_none_value_exists(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        sprite.graphics.line_style(
            color='#333', dot_setting=LineDotSetting(dot_size=10))
        points: Array = Array([Point2D(10, 20), Point2D(30, 40)])
        polyline: Polyline = Polyline(
            parent=sprite.graphics, points=points)
        assert isinstance(polyline.line_dot_setting, LineDotSetting)

        sprite.graphics.line_style(
            color='#333',
            dash_setting=LineDashSetting(dash_size=10, space_size=5))
        polyline = Polyline(
            parent=sprite.graphics, points=points)
        assert isinstance(polyline.line_dash_setting, LineDashSetting)

        sprite.graphics.line_style(
            color='#333',
            round_dot_setting=LineRoundDotSetting(
                round_size=10, space_size=5))
        polyline = Polyline(
            parent=sprite.graphics, points=points)
        assert isinstance(
            polyline.line_round_dot_setting, LineRoundDotSetting)

        sprite.graphics.line_style(
            color='#333',
            dash_dot_setting=LineDashDotSetting(
                dot_size=5, dash_size=10, space_size=7))
        polyline = Polyline(
            parent=sprite.graphics, points=points)
        assert isinstance(
            polyline.line_dash_dot_setting, LineDashDotSetting)
