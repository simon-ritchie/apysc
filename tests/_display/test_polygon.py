from random import randint

from retrying import retry

from apysc import Array
from apysc import LineDotSetting
from apysc import Point2D
from apysc import Polygon
from apysc import Sprite
from apysc import Stage
from apysc._display.stage import get_stage_variable_name
from apysc._expression import expression_file_util
from apysc._expression import var_names
from tests._display.test_graphics_expression import \
    assert_stroke_attr_expression_exists


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

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___repr__(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        points: Array[Point2D] = Array(
            [Point2D(50, 50), Point2D(150, 50), Point2D(100, 100)])
        polygon: Polygon = Polygon(
            parent=sprite.graphics,
            points=points)
        repr_str: str = repr(polygon)
        assert repr_str == f"Polygon('{polygon.variable_name}')"

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_constructor_expression(self) -> None:
        expression_file_util.remove_expression_file()
        stage: Stage = Stage()
        stage_variable_name: str = get_stage_variable_name()
        sprite: Sprite = Sprite(stage=stage)
        points: Array[Point2D] = Array(
            [Point2D(50, 50), Point2D(150, 50), Point2D(100, 100)])
        sprite.graphics.line_style(color='#333')
        polygon: Polygon = Polygon(
            parent=sprite.graphics, points=points)
        expression: str = expression_file_util.get_current_expression()
        assert_stroke_attr_expression_exists(expression=expression)
        expected: str = (
            f'\nvar {polygon.variable_name} = {stage_variable_name}'
            f'\n  .polygon('
        )
        assert expected in expression
        assert '\n  .attr({' in expression
