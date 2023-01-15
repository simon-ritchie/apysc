from random import randint

from retrying import retry

import apysc as ap
from apysc._display.triangle import Triangle
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import assert_attrs


class TestTriangle:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
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

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
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
        assert triangle.x == ap.Int(15)
        assert triangle.y == ap.Int(10)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
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
        expected: str = f"Triangle('{triangle.variable_name}')"
        assert repr_str == expected

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
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
