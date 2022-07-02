import re
from random import randint
from typing import List
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._display.stage import get_stage_variable_name
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import assert_attrs
from tests._display.test_graphics_expression import \
    assert_fill_attr_expression_exists
from tests._display.test_graphics_expression import \
    assert_fill_opacity_attr_expression_exists
from tests._display.test_graphics_expression import \
    assert_stroke_attr_expression_exists
from tests._display.test_graphics_expression import \
    assert_stroke_dasharray_css_expression_exists
from tests._display.test_graphics_expression import \
    assert_stroke_linecap_attr_expression_exists
from tests._display.test_graphics_expression import \
    assert_stroke_linejoin_attr_expression_exists
from tests._display.test_graphics_expression import \
    assert_stroke_opacity_attr_expression_exists
from tests._display.test_graphics_expression import \
    assert_stroke_width_attr_expression_exists
from tests._display.test_graphics_expression import \
    assert_x_attr_expression_exists
from tests._display.test_graphics_expression import \
    assert_y_attr_expression_exists


class TestPolyline:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        stage: ap.Stage = ap.Stage()
        points: List[ap.Point2D] = [ap.Point2D(10, 20), ap.Point2D(30, 40)]
        polyline: ap.Polyline = ap.Polyline(
            points=points,
            fill_color='#0af',
            fill_alpha=0.5,
            line_color='fff',
            line_alpha=0.3,
            line_thickness=3,
            line_cap=ap.LineCaps.ROUND,
            line_joints=ap.LineJoints.BEVEL,
            line_dot_setting=ap.LineDotSetting(dot_size=10))
        assert_attrs(
            expected_attrs={
                '_points': points,
                '_fill_color': '#00aaff',
                '_fill_alpha': 0.5,
                '_line_color': '#ffffff',
                '_line_alpha': 0.3,
                '_line_thickness': 3,
                '_line_cap': ap.LineCaps.ROUND.value,
                '_line_joints': ap.LineJoints.BEVEL.value,
                '_line_dot_setting': ap.LineDotSetting(dot_size=10),
                '_parent': stage,
            },
            any_obj=polyline)

        sprite: ap.Sprite = ap.Sprite()
        polyline = ap.Polyline(
            points=points,
            line_dash_setting=ap.LineDashSetting(
                dash_size=10, space_size=5),
            parent=sprite)
        assert_attrs(
            expected_attrs={
                '_line_dash_setting': ap.LineDashSetting(
                    dash_size=10, space_size=5),
                '_parent': sprite,
            },
            any_obj=polyline)

        polyline = ap.Polyline(
            points=points,
            line_round_dot_setting=ap.LineRoundDotSetting(
                round_size=10, space_size=5))
        assert polyline._line_round_dot_setting == ap.LineRoundDotSetting(
            round_size=10, space_size=5)

        polyline = ap.Polyline(
            points=points,
            line_dash_dot_setting=ap.LineDashDotSetting(
                dot_size=5, dash_size=10, space_size=3))
        assert polyline._line_dash_dot_setting == ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=3)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___repr__(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        points: ap.Array = ap.Array([ap.Point2D(10, 20), ap.Point2D(30, 40)])
        polyline: ap.Polyline = ap.Polyline(
            parent=sprite.graphics,
            points=points)
        repr_str: str = repr(polyline)
        expected: str = (
            f"Polyline('{polyline.variable_name}')"
        )
        assert repr_str == expected

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_constructor_expression(self) -> None:
        expression_data_util.empty_expression()
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.begin_fill(color='#0af')
        sprite.graphics.line_style(
            color='#f0a', cap=ap.LineCaps.ROUND, joints=ap.LineJoints.BEVEL,
            dot_setting=ap.LineDotSetting(dot_size=10))
        polyline: ap.Polyline = sprite.graphics.line_to(
            x=10, y=20)
        stage_variable_name: str = get_stage_variable_name()
        expression: str = expression_data_util.get_current_expression()
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
        assert_stroke_linecap_attr_expression_exists(expression=expression)
        assert_stroke_linejoin_attr_expression_exists(expression=expression)
        assert_stroke_dasharray_css_expression_exists(expression=expression)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_append_line_point(self) -> None:
        expression_data_util.empty_expression()
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.begin_fill(color='#0af')
        sprite.graphics.line_style(color='#f0a')
        points: ap.Array = ap.Array([ap.Point2D(10, 20), ap.Point2D(30, 40)])
        polyline: ap.Polyline = ap.Polyline(
            parent=sprite.graphics,
            points=points)
        polyline.append_line_point(x=50, y=60)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{polyline._points_var_name}.push([50, 60]);'
            f'\n{polyline.variable_name}.plot({polyline._points_var_name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__create_with_graphics(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.begin_fill(color='#0af', alpha=0.5)
        sprite.graphics.line_style(
            color='fff', thickness=3, alpha=0.3,
            cap=ap.LineCaps.ROUND, joints=ap.LineJoints.BEVEL,
            dot_setting=ap.LineDotSetting(dot_size=10))
        polyline: ap.Polyline = sprite.graphics.move_to(x=50, y=100)
        assert_attrs(
            expected_attrs={
                '_points': [ap.Point2D(x=50, y=100)],
                '_fill_color': '#00aaff',
                '_fill_alpha': 0.5,
                '_line_color': '#ffffff',
                '_line_alpha': 0.3,
                '_line_thickness': 3,
                '_line_cap': ap.LineCaps.ROUND.value,
                '_line_joints': ap.LineJoints.BEVEL.value,
                '_line_dot_setting': ap.LineDotSetting(dot_size=10),
                '_parent': sprite.graphics,
            },
            any_obj=polyline)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_initial_x_and_y_with_minimum_point(self) -> None:
        ap.Stage()
        points: List[ap.Point2D] = [ap.Point2D(10, 20), ap.Point2D(30, 40)]
        polyline: ap.Polyline = ap.Polyline(points=points)
        assert polyline.x == 10
        assert polyline.y == 20

        points = [ap.Point2D(30, 40), ap.Point2D(10, 20)]
        polyline = ap.Polyline(points=points)
        assert polyline.x == 10
        assert polyline.y == 20
