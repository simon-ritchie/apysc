from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import expression_file_util
from tests._display.test_graphics_expression import \
    assert_fill_attr_expression_exists
from tests._display.test_graphics_expression import \
    assert_fill_opacity_attr_expression_exists
from tests._display.test_graphics_expression import \
    assert_stroke_attr_expression_exists
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


class TestLineBase:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_line_setting_if_not_none_value_exists(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        sprite.graphics.line_style(
            color='#333', dot_setting=ap.LineDotSetting(dot_size=10))
        points: ap.Array = ap.Array([ap.Point2D(10, 20), ap.Point2D(30, 40)])
        polyline: ap.Polyline = ap.Polyline(
            parent=sprite.graphics, points=points)
        assert isinstance(polyline.line_dot_setting, ap.LineDotSetting)

        sprite.graphics.line_style(
            color='#333',
            dash_setting=ap.LineDashSetting(dash_size=10, space_size=5))
        polyline = ap.Polyline(
            parent=sprite.graphics, points=points)
        assert isinstance(polyline.line_dash_setting, ap.LineDashSetting)

        sprite.graphics.line_style(
            color='#333',
            round_dot_setting=ap.LineRoundDotSetting(
                round_size=10, space_size=5))
        polyline = ap.Polyline(
            parent=sprite.graphics, points=points)
        assert isinstance(
            polyline.line_round_dot_setting, ap.LineRoundDotSetting)

        sprite.graphics.line_style(
            color='#333',
            dash_dot_setting=ap.LineDashDotSetting(
                dot_size=5, dash_size=10, space_size=7))
        polyline = ap.Polyline(
            parent=sprite.graphics, points=points)
        assert isinstance(
            polyline.line_dash_dot_setting, ap.LineDashDotSetting)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_initial_basic_values(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        sprite.graphics.begin_fill(color='#333', alpha=0.5)
        points: ap.Array[ap.Point2D] = ap.Array([ap.Point2D(0, 0)])
        sprite.graphics.line_style(
            color='#666', thickness=2, alpha=0.7,
            cap=ap.LineCaps.ROUND, joints=ap.LineJoints.BEVEL)
        polyline = ap.Polyline(parent=sprite.graphics, points=points)
        assert polyline.fill_color == '#333333'
        assert polyline.fill_alpha == 0.5
        assert polyline.line_color == '#666666'
        assert polyline.line_thickness == 2
        assert polyline.line_alpha == 0.7
        assert polyline.x == 0
        assert polyline.y == 0
        assert polyline.line_cap == ap.LineCaps.ROUND.value
        assert polyline.line_joints == ap.LineJoints.BEVEL.value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_basic_vals_expression(self) -> None:
        expression_file_util.empty_expression()
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        sprite.graphics.begin_fill(color='#333', alpha=0.5)
        sprite.graphics.line_style(
            color='#666', thickness=2, alpha=0.3,
            cap=ap.LineCaps.ROUND, joints=ap.LineJoints.BEVEL)
        points: ap.Array[ap.Point2D] = ap.Array([ap.Point2D(0, 0)])
        polyline = ap.Polyline(parent=sprite.graphics, points=points)
        expression: str = '.attr({'
        expression = polyline._append_basic_vals_expression(
            expression=expression, indent_num=2)
        assert_fill_attr_expression_exists(expression=expression)
        assert_fill_opacity_attr_expression_exists(expression=expression)
        assert_stroke_attr_expression_exists(expression=expression)
        assert_stroke_linecap_attr_expression_exists(expression=expression)
        assert_stroke_linejoin_attr_expression_exists(expression=expression)
        assert_stroke_opacity_attr_expression_exists(expression=expression)
        assert_stroke_width_attr_expression_exists(expression=expression)
        assert_x_attr_expression_exists(expression=expression)
        assert_y_attr_expression_exists(expression=expression)
