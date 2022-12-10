from random import randint
from typing import List

from retrying import retry

import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import assert_attrs
from tests._display.test_graphics_expression import assert_stroke_attr_expression_exists


class TestPolygon:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        stage: ap.Stage = ap.Stage()
        points: List[ap.Point2D] = [
            ap.Point2D(50, 50),
            ap.Point2D(150, 50),
            ap.Point2D(100, 100),
        ]
        polygon: ap.Polygon = ap.Polygon(
            points=points,
            fill_color="#0af",
            fill_alpha=0.5,
            line_color="fff",
            line_alpha=0.3,
            line_thickness=3,
            line_cap=ap.LineCaps.ROUND,
            line_joints=ap.LineJoints.BEVEL,
            line_dot_setting=ap.LineDotSetting(dot_size=5),
            variable_name_suffix="test_polygon",
        )
        assert_attrs(
            expected_attrs={
                "_points": points,
                "_fill_color": "#00aaff",
                "_fill_alpha": 0.5,
                "_line_color": "#ffffff",
                "_line_alpha": 0.3,
                "_line_thickness": 3,
                "_line_cap": ap.LineCaps.ROUND.value,
                "_line_joints": ap.LineJoints.BEVEL.value,
                "_line_dot_setting": ap.LineDotSetting(dot_size=5),
                "_parent": stage,
                "_variable_name_suffix": "test_polygon",
            },
            any_obj=polygon,
        )

        sprite: ap.Sprite = ap.Sprite()
        polygon = ap.Polygon(
            points=points,
            line_dash_setting=ap.LineDashSetting(dash_size=10, space_size=5),
            parent=sprite,
        )
        assert_attrs(
            expected_attrs={
                "_parent": sprite,
                "_line_dash_setting": ap.LineDashSetting(dash_size=10, space_size=5),
            },
            any_obj=polygon,
        )

        polygon = ap.Polygon(
            points=points,
            line_round_dot_setting=ap.LineRoundDotSetting(round_size=10, space_size=5),
        )
        assert polygon._line_round_dot_setting == ap.LineRoundDotSetting(
            round_size=10, space_size=5
        )

        polygon = ap.Polygon(
            points=points,
            line_dash_dot_setting=ap.LineDashDotSetting(
                dot_size=5, dash_size=10, space_size=3
            ),
        )
        assert polygon._line_dash_dot_setting == ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=3
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___repr__(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        points: ap.Array[ap.Point2D] = ap.Array(
            [ap.Point2D(50, 50), ap.Point2D(150, 50), ap.Point2D(100, 100)]
        )
        polygon: ap.Polygon = ap.Polygon(parent=sprite.graphics, points=points)
        repr_str: str = repr(polygon)
        assert repr_str == f"Polygon('{polygon.variable_name}')"

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_constructor_expression(self) -> None:
        expression_data_util.empty_expression()
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        points: ap.Array[ap.Point2D] = ap.Array(
            [ap.Point2D(50, 50), ap.Point2D(150, 50), ap.Point2D(100, 100)]
        )
        sprite.graphics.line_style(color="#333")
        polygon: ap.Polygon = sprite.graphics.draw_polygon(points=points)
        expression: str = expression_data_util.get_current_expression()
        assert_stroke_attr_expression_exists(expression=expression)
        expected: str = (
            f"\nvar {polygon.variable_name} = {stage.variable_name}" f"\n  .polygon("
        )
        assert expected in expression
        assert "\n  .attr({" in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__create_with_graphics(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.begin_fill(color="#0af", alpha=0.5)
        points: ap.Array[ap.Point2D] = ap.Array(
            [ap.Point2D(50, 50), ap.Point2D(150, 50), ap.Point2D(100, 100)]
        )
        sprite.graphics.line_style(
            color="fff",
            thickness=3,
            alpha=0.3,
            cap=ap.LineCaps.ROUND,
            joints=ap.LineJoints.BEVEL,
            dot_setting=ap.LineDotSetting(dot_size=5),
        )
        polygon: ap.Polygon = ap.Polygon._create_with_graphics(
            graphics=sprite.graphics, points=points, variable_name_suffix="test_polygon"
        )
        assert_attrs(
            expected_attrs={
                "_points": points,
                "_fill_color": "#00aaff",
                "_fill_alpha": 0.5,
                "_line_color": "#ffffff",
                "_line_thickness": 3,
                "_line_alpha": 0.3,
                "_line_cap": ap.LineCaps.ROUND.value,
                "_line_joints": ap.LineJoints.BEVEL.value,
                "_line_dot_setting": ap.LineDotSetting(dot_size=5),
                "_parent": sprite.graphics,
                "_variable_name_suffix": "test_polygon",
            },
            any_obj=polygon,
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_x_and_y_with_minimum_point(self) -> None:
        ap.Stage()
        points: List[ap.Point2D] = [
            ap.Point2D(50, 50),
            ap.Point2D(150, 30),
            ap.Point2D(20, 100),
        ]
        polygon: ap.Polygon = ap.Polygon(
            points=points, variable_name_suffix="test_polygon"
        )
        assert polygon.x == 20
        assert polygon.y == 30
        assert polygon._x._variable_name_suffix == "test_polygon__x"
        assert polygon._y._variable_name_suffix == "test_polygon__y"