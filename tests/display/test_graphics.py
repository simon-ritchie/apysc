from random import randint
from typing import Optional

from retrying import retry

from apysc import Array
from apysc import Line
from apysc import LineDashDotSetting
from apysc import LineDashSetting
from apysc import LineDotSetting
from apysc import LineRoundDotSetting
from apysc import Point2D
from apysc import Polyline
from apysc import Sprite
from apysc import Stage
from apysc.display.graphics import Graphics
from apysc.display.graphics import Rectangle
from apysc.expression import expression_file_util
from tests import testing_helper


class TestGraphics:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        graphics: Graphics = Graphics(parent=sprite)
        testing_helper.assert_attrs(
            expected_attrs={
                'parent_sprite': sprite,
            },
            any_obj=graphics)
        assert isinstance(graphics.variable_name, str)
        assert graphics.variable_name != ''

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_begin_fill(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        graphics: Graphics = Graphics(parent=sprite)
        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=graphics.begin_fill,
            kwargs={'color': 'red'})

        graphics.begin_fill(color='#0af')
        testing_helper.assert_attrs(
            expected_attrs={
                '_fill_color': '#00aaff',
            },
            any_obj=graphics)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_draw_rect(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        graphics: Graphics = Graphics(parent=sprite)
        rectangle: Rectangle = graphics.draw_rect(
            x=100, y=200, width=300, height=400)
        assert graphics.num_children == 1
        testing_helper.assert_attrs(
            expected_attrs={
                '_x': 100,
                '_y': 200,
                'width': 300,
                'height': 400,
            },
            any_obj=graphics.get_child_at(index=0))
        assert isinstance(graphics.get_child_at(index=0), Rectangle)
        assert rectangle == graphics.get_child_at(index=0)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_clear(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        sprite.graphics.begin_fill(color='#333')
        sprite.graphics.draw_rect(x=50, y=50, width=100, height=100)
        assert sprite.graphics.num_children == 1
        sprite.graphics.clear()
        assert sprite.graphics.num_children == 0

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_constructor_expression(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'var {sprite.graphics.variable_name} = '
            f'{stage.variable_name}.nested();'
            f'\n{sprite.variable_name}.add({sprite.graphics.variable_name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___repr__(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        repr_str: str = repr(sprite.graphics)
        assert repr_str == f"Graphics('{sprite.graphics.variable_name}')"

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_to(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        polyline: Polyline = sprite.graphics.line_to(x=100, y=200)
        assert polyline.points == Array(
            [Point2D(0, 0), Point2D(100, 200)])
        pre_var_name: str = polyline.variable_name

        polyline = sprite.graphics.line_to(x=300, y=400)
        assert polyline.points == Array(
            [Point2D(0, 0), Point2D(100, 200), Point2D(300, 400)])
        assert polyline.variable_name == pre_var_name

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_move_to(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        polyline: Polyline = sprite.graphics.move_to(x=100, y=200)
        assert polyline.points == Array([Point2D(100, 200)])
        pre_var_name: str = polyline.variable_name

        sprite.graphics.line_to(x=0, y=0)
        polyline = sprite.graphics.move_to(x=300, y=400)
        assert polyline.points == Array([Point2D(300, 400)])
        assert polyline.variable_name != pre_var_name

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__reset_each_line_settings(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        sprite.graphics._line_dot_setting = LineDotSetting(dot_size=10)
        sprite.graphics._line_dash_setting = LineDashSetting(
            dash_size=10, space_size=5)
        sprite.graphics._line_round_dot_setting = LineRoundDotSetting(
            round_size=10, space_size=5)
        sprite.graphics._line_dash_dot_setting = LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=5)
        sprite.graphics._reset_each_line_settings()
        assert sprite.graphics._line_dot_setting is None
        assert sprite.graphics._line_dash_setting is None
        assert sprite.graphics._line_round_dot_setting is None
        assert sprite.graphics._line_dash_dot_setting is None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_draw_line(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        sprite.graphics.line_style(
            color='#333', thickness=3,
            dot_setting=LineDotSetting(dot_size=10))
        line: Line = sprite.graphics.draw_line(
            x_start=50, y_start=100, x_end=150, y_end=200)
        assert line.line_color == '#333333'
        assert line.line_thickness == 3
        assert line.line_dot_setting is None
        assert line._start_point == Point2D(x=50, y=100)
        assert line._end_point == Point2D(x=150, y=200)
        assert isinstance(sprite.graphics.line_dot_setting, LineDotSetting)
        sprite.graphics._children == [line]

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_draw_dashed_line(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        sprite.graphics.line_style(
            color='#333', thickness=3,
            dot_setting=LineDotSetting(dot_size=5))
        line: Line = sprite.graphics.draw_dashed_line(
            x_start=50, y_start=100, x_end=150, y_end=200,
            dash_size=10, space_size=5)
        assert line.line_color == '#333333'
        assert line.line_thickness == 3
        line_dash_setting: Optional[LineDashSetting] = \
            line.line_dash_setting
        assert isinstance(line_dash_setting, LineDashSetting)
        assert line_dash_setting.dash_size == 10
        assert line_dash_setting.space_size == 5
        assert line._start_point == Point2D(x=50, y=100)
        assert line._end_point == Point2D(x=150, y=200)
        assert isinstance(sprite.graphics.line_dot_setting, LineDotSetting)
        sprite.graphics._children == [line]
