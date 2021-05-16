from random import randint
from typing import List

from retrying import retry

from apysc import Polyline, Stage, Sprite, LineDotSetting, Array, Point2D, LineDashSetting, LineRoundDotSetting, LineDashDotSetting, LineCaps, LineJoints


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

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_initial_basic_values(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        sprite.graphics.begin_fill(color='#333', alpha=0.5)
        points: Array[Point2D] = Array([Point2D(0, 0)])
        sprite.graphics.line_style(
            color='#666', thickness=2, alpha=0.7,
            cap=LineCaps.ROUND, joints=LineJoints.BEVEL)
        polyline = Polyline(parent=sprite.graphics, points=points)
        assert polyline.fill_color == '#333333'
        assert polyline.fill_alpha == 0.5
        assert polyline.line_color == '#666666'
        assert polyline.line_thickness == 2
        assert polyline.line_alpha == 0.7
        assert polyline.x == 0
        assert polyline.y == 0
        assert polyline.line_cap == LineCaps.ROUND.value
        assert polyline.line_joints == LineJoints.BEVEL.value
