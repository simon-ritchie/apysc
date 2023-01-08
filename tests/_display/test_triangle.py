from random import randint

from retrying import retry

from apysc._display.triangle import Triangle
import apysc as ap


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
