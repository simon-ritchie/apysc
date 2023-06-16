import apysc as ap
from apysc._display.triangle import Triangle
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs


class TestTriangle:
    @apply_test_settings()
    def test__set_points_with_each_coordinate(self) -> None:
        ap.Stage()
        triangle: Triangle = Triangle(
            x1=50,
            y1=0,
            x2=0,
            y2=50,
            x3=100,
            y3=50,
        )
        assert triangle._points == ap.Array(
            value=[
                ap.Point2D(x=50, y=0),
                ap.Point2D(x=0, y=50),
                ap.Point2D(x=100, y=50),
            ],
        )

    @apply_test_settings()
    def test__set_x_and_y_with_minimum_point(self) -> None:
        ap.Stage()
        triangle: Triangle = Triangle(
            x1=50,
            y1=10,
            x2=15,
            y2=50,
            x3=100,
            y3=50,
        )
        assert triangle.x == ap.Number(15)
        assert triangle.y == ap.Number(10)

    @apply_test_settings()
    def test___repr__(self) -> None:
        ap.Stage()
        triangle: Triangle = Triangle(
            x1=50,
            y1=0,
            x2=0,
            y2=50,
            x3=100,
            y3=50,
        )
        repr_str: str = repr(triangle)
        expected: str = f'Triangle("{triangle.variable_name}")'
        assert repr_str == expected

    @apply_test_settings()
    def test___init__(self) -> None:
        expression_data_util.empty_expression()
        stage: ap.Stage = ap.Stage()
        triangle: Triangle = Triangle(
            x1=50,
            y1=0,
            x2=0,
            y2=50,
            x3=100,
            y3=50,
            fill_color="#0af",
            variable_name_suffix="test_triangle",
        )
        assert_attrs(
            expected_attrs={
                "_x1": 50,
                "_y1": 0,
                "_x2": 0,
                "_y2": 50,
                "_x3": 100,
                "_y3": 50,
                "_parent": stage,
                "_variable_name_suffix": "test_triangle",
                "_fill_color": "#00aaff",
            },
            any_obj=triangle,
        )
        assert triangle.variable_name.startswith(
            var_names.TRIANGLE,
        )
        expression: str = expression_data_util.get_current_expression()
        assert ".polygon(" in expression

        sprite: ap.Sprite = ap.Sprite()
        triangle = Triangle(
            x1=50,
            y1=0,
            x2=0,
            y2=50,
            x3=100,
            y3=50,
            parent=sprite,
        )
        assert triangle.parent == sprite

    @apply_test_settings()
    def test__create_with_graphics(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.begin_fill(color="#0af", alpha=0.5)
        dot_setting: ap.LineDotSetting = ap.LineDotSetting(dot_size=10)
        sprite.graphics.line_style(
            color="#fff",
            thickness=3,
            alpha=0.3,
            dot_setting=dot_setting,
        )
        triangle: Triangle = Triangle._create_with_graphics(
            graphics=sprite.graphics,
            x1=50,
            y1=50,
            x2=25,
            y2=75,
            x3=75,
            y3=50,
        )
        assert_attrs(
            expected_attrs={
                "_x1": 50,
                "_y1": 50,
                "_x2": 25,
                "_y2": 75,
                "_x3": 75,
                "_y3": 50,
                "_parent": sprite.graphics,
                "_fill_color": "#00aaff",
                "_fill_alpha": 0.5,
                "_line_color": "#ffffff",
                "_line_thickness": 3,
                "_line_alpha": 0.3,
                "_line_dot_setting": dot_setting,
            },
            any_obj=triangle,
        )

    @apply_test_settings()
    def test__initialize_for_loop_key_or_value(self) -> None:
        triangle: ap.Triangle = ap.Triangle._initialize_for_loop_key_or_value()
        assert triangle.x1 == ap.Number(-2)
        assert triangle.y1 == ap.Number(-2)
        assert triangle.x2 == ap.Number(-1)
        assert triangle.y2 == ap.Number(-2)
        assert triangle.x3 == ap.Number(-1)
        assert triangle.y3 == ap.Number(-1)
        assert triangle.visible == ap.Boolean(False)
