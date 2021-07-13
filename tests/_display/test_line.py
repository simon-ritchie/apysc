import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._display.stage import get_stage_variable_name
from apysc._expression import expression_file_util
from apysc._expression import var_names
from tests._display.test_graphics_expression import \
    assert_stroke_attr_expression_exists


class TestLine:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        line_dot_setting: ap.LineDotSetting = ap.LineDotSetting(dot_size=10)
        sprite.graphics.line_style(
            color='#0af', dot_setting=line_dot_setting)
        line: ap.Line = ap.Line(
            parent=sprite.graphics,
            start_point=ap.Point2D(x=10, y=20),
            end_point=ap.Point2D(x=30, y=40))
        assert line.variable_name.startswith(f'{var_names.LINE}_')
        assert line._start_point == ap.Point2D(x=10, y=20)
        assert line._end_point == ap.Point2D(x=30, y=40)
        assert line.line_color == '#00aaff'
        assert line.line_dot_setting == line_dot_setting

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_points_expression(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        line: ap.Line = ap.Line(
            parent=sprite.graphics,
            start_point=ap.Point2D(x=10, y=20),
            end_point=ap.Point2D(x=30, y=40))
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
        stage: ap.Stage = ap.Stage()
        stage_variable_name: str = get_stage_variable_name()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        sprite.graphics.line_style(color='#333', thickness=3)
        line: ap.Line = ap.Line(
            parent=sprite.graphics,
            start_point=ap.Point2D(x=10, y=20),
            end_point=ap.Point2D(x=30, y=40))
        expression: str = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'var {line.variable_name} = {stage_variable_name}'
                r'\n  .line\(.+?\)'
                r'\n  .attr\(\{.*?'
                r'\n  \}\);'
            ),
            string=expression, flags=re.MULTILINE | re.DOTALL)
        assert match is not None
        assert_stroke_attr_expression_exists(expression=expression)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___repr__(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        line: ap.Line = ap.Line(
            parent=sprite.graphics,
            start_point=ap.Point2D(x=10, y=20),
            end_point=ap.Point2D(x=30, y=40))
        repr_str: str = repr(line)
        expected: str = f"Line('{line.variable_name}')"
        assert repr_str == expected
