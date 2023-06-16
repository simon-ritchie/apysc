from typing import List

import apysc as ap
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs


class TestPolygon:
    @apply_test_settings()
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

    @apply_test_settings()
    def test___repr__(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        points: ap.Array[ap.Point2D] = ap.Array(
            [ap.Point2D(50, 50), ap.Point2D(150, 50), ap.Point2D(100, 100)]
        )
        polygon: ap.Polygon = ap.Polygon(parent=sprite.graphics, points=points)
        repr_str: str = repr(polygon)
        assert repr_str == f'Polygon("{polygon.variable_name}")'

    @apply_test_settings()
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

    @apply_test_settings()
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

    @apply_test_settings()
    def test__initialize_for_loop_key_or_value(self) -> None:
        ap.Stage()
        polygon: ap.Polygon = ap.Polygon._initialize_for_loop_key_or_value()
        assert polygon._points == ap.Array(
            [
                ap.Point2D(x=-2, y=-2),
                ap.Point2D(x=-1, y=-2),
                ap.Point2D(x=-1, y=-1),
            ]
        )
        assert polygon.visible == ap.Boolean(False)
