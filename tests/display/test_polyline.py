from typing import List, Match, Optional
from apysc.expression import expression_file_util
from random import randint
import re

from retrying import retry

from apysc import Array
from apysc import Point2D
from apysc import Polyline
from apysc import Sprite
from apysc import Stage
from tests.testing_helper import assert_attrs
from tests.display.test_graphics_expression import assert_fill_attr_expression_exists, assert_fill_opacity_attr_expression_exists, assert_stroke_attr_expression_exists, assert_stroke_opacity_attr_expression_exists, assert_stroke_width_attr_expression_exists, assert_x_attr_expression_exists, assert_y_attr_expression_exists
from apysc.display.stage import get_stage_variable_name


class TestPolyline:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        points: Array = Array([Point2D(10, 20), Point2D(30, 40)])
        polyline: Polyline = Polyline(
            parent=sprite.graphics,
            points=points,
            fill_color='0af',
            fill_alpha=0.5,
            line_color='f0a',
            line_thickness=2,
            line_alpha=0.7)
        assert_attrs(
            expected_attrs={
                '_points': points,
                '_fill_color': '#00aaff',
                '_fill_alpha': 0.5,
                '_line_color': '#ff00aa',
                '_line_thickness': 2,
                '_line_alpha': 0.7,
                '_x': 0,
                '_y': 0,
            },
            any_obj=polyline)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___repr__(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        points: Array = Array([Point2D(10, 20), Point2D(30, 40)])
        polyline: Polyline = Polyline(
            parent=sprite.graphics,
            points=points,
            fill_color='0af',
            fill_alpha=0.5,
            line_color='f0a',
            line_thickness=2,
            line_alpha=0.7)
        repr_str: str = repr(polyline)
        expected: str = (
            f"Polyline('{polyline.variable_name}')"
        )
        assert repr_str == expected

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_constructor_expression(self) -> None:
        expression_file_util.remove_expression_file()
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        sprite.graphics.begin_fill(color='#0af')
        sprite.graphics.line_style(color='#f0a')
        points: Array = Array([Point2D(10, 20), Point2D(30, 40)])
        polyline: Polyline = Polyline(
            parent=sprite.graphics,
            points=points)
        stage_variable_name: str = get_stage_variable_name()
        expression: str = expression_file_util.get_current_expression()
        expected_patterns: List[str] = [
            r'var a.+ \= \[\]\;',
            rf'var {polyline.variable_name} \= {stage_variable_name}',
            r'\n  \.polyline\(.+?\)',
            r'\n  \.attr\(\{',
            r'\n  \}\)\;',
        ]
        for expected_pattern in expected_patterns:
            match: Optional[Match] = re.search(
                pattern=expected_pattern, string=expression,
                flags=re.MULTILINE,
            )
            assert match is not None, f'expected_pattern: {expected_pattern}'
        assert_fill_attr_expression_exists(expression=expression)
        assert_fill_opacity_attr_expression_exists(expression=expression)
        assert_x_attr_expression_exists(expression=expression)
        assert_y_attr_expression_exists(expression=expression)
        assert_stroke_attr_expression_exists(expression=expression)
        assert_stroke_width_attr_expression_exists(expression=expression)
        assert_stroke_opacity_attr_expression_exists(expression=expression)
