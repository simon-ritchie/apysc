from random import randint

from retrying import retry

from apysc import Polygon, Stage, Sprite, Array, Point2D, LineDotSetting
from apysc.expression import var_names


class TestPolygon:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        sprite.graphics.line_style(
            color='#333', dot_setting=LineDotSetting(dot_size=10))
        points: Array[Point2D] = Array(
            [Point2D(50, 50), Point2D(150, 50), Point2D(100, 100)])
        polygon: Polygon = Polygon(
            parent=sprite.graphics,
            points=points)
        assert polygon.points == points
        assert polygon.variable_name.startswith(f'{var_names.POLYGON}_')
        assert polygon.line_color == '#333333'
        assert isinstance(polygon.line_dot_setting, LineDotSetting)
