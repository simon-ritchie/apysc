from random import randint
from typing import Match, Optional
import re

from retrying import retry

from apysc import Stage, Sprite, LineDotSetting, Point2D
from apysc.expression import expression_file_util, var_names
from apysc import Line
from tests.display.test_graphics_expression import \
    assert_stroke_attr_expression_exists
from apysc.display.stage import get_stage_variable_name


class TestLine:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        line_dot_setting: LineDotSetting = LineDotSetting(dot_size=10)
        sprite.graphics.line_style(
            color='#0af', dot_setting=line_dot_setting)
        line: Line = Line(
            parent=sprite.graphics,
            start_point=Point2D(x=10, y=20),
            end_point=Point2D(x=30, y=40))
        assert line.variable_name.startswith(f'{var_names.LINE}_')
        assert line._start_point == Point2D(x=10, y=20)
        assert line._end_point == Point2D(x=30, y=40)
        assert line.line_color == '#00aaff'
        assert line.line_dot_setting == line_dot_setting

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_points_expression(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        line: Line = Line(
            parent=sprite.graphics,
            start_point=Point2D(x=10, y=20),
            end_point=Point2D(x=30, y=40))
        expression: str = line._make_points_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'{var_names.INT}_.+, {var_names.INT}_.+, '
                rf'{var_names.INT}_.+, {var_names.INT}_.+$'
            ),
            string=expression, flags=re.MULTILINE)
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_constructor_expression(self) -> None:
        stage: Stage = Stage()
        stage_variable_name: str = get_stage_variable_name()
        sprite: Sprite = Sprite(stage=stage)
        sprite.graphics.line_style(color='#333', thickness=3)
        line: Line = Line(
            parent=sprite.graphics,
            start_point=Point2D(x=10, y=20),
            end_point=Point2D(x=30, y=40))
        expression: str = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'var {line.variable_name} = {stage_variable_name}'
                r'\n  .line\(.+?\)'
                r'\n  .attr\(\{.*?'
                r'\n  \}\);'
            ),
            string=expression, flags=re.MULTILINE| re.DOTALL)
        assert match is not None
        assert_stroke_attr_expression_exists(expression=expression)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___repr__(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        line: Line = Line(
            parent=sprite.graphics,
            start_point=Point2D(x=10, y=20),
            end_point=Point2D(x=30, y=40))
        repr_str: str = repr(line)
        expected: str = f"Line('{line.variable_name}')"
        assert repr_str == expected
