from random import randint

from retrying import retry

from apysc import Point2D, Int, Boolean
from tests.testing_helper import assert_attrs
from apysc.expression import var_names
from apysc.expression import expression_file_util


class TestPoint2D:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        point: Point2D = Point2D(x=10, y=20)
        assert_attrs(
            expected_attrs={
                '_x': 10,
                '_y': 20,
            },
            any_obj=point)
        assert isinstance(point._x, Int)
        assert isinstance(point._y, Int)
        assert point.variable_name.startswith(f'{var_names.POINT2D}_')

        x: Int = Int(10)
        y: Int = Int(20)
        point = Point2D(x=x, y=y)
        assert_attrs(
            expected_attrs={
                '_x': x,
                '_y': y,
            },
            any_obj=point)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_x(self) -> None:
        point: Point2D = Point2D(x=10, y=20)
        x: Int = point.x
        assert isinstance(x, Int)
        assert x == 10

        point.x = 20
        assert point.x == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_y(self) -> None:
        point: Point2D = Point2D(x=10, y=20)
        y: Int = point.y
        assert isinstance(y, Int)
        assert y == 20

        point.y = 30
        assert point.y == 30

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___eq__(self) -> None:
        point: Point2D = Point2D(x=10, y=20)
        result: Boolean = point == 20
        assert isinstance(result, Boolean)
        assert not result

        result = point == Point2D(x=10, y= 20)
        assert isinstance(result, Boolean)
        assert result

        result = point == Point2D(x=20, y=20)
        assert isinstance(result, Boolean)
        assert not result

        result = point == Point2D(x=10, y=30)
        assert not result

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___ne__(self) -> None:
        point: Point2D = Point2D(x=10, y=20)
        result: Boolean = point != Point2D(x=20, y=20)
        assert result

        result = point != Point2D(x=10, y=20)
        assert not result

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_constructor_expression(self) -> None:
        expression_file_util.remove_expression_file()
        x: Int = Int(10)
        y: Int = Int(20)
        point: Point2D = Point2D(x=x, y=y)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{point.variable_name} = '
            f'{{"x": {x.variable_name}, "y": {y.variable_name}}};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_x_getter_expression(self) -> None:
        expression_file_util.remove_expression_file()
        point: Point2D = Point2D(x=10, y=20)
        x: Int = point.x
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{x.variable_name} = {point.variable_name}["x"];'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_y_getter_expression(self) -> None:
        expression_file_util.remove_expression_file()
        point: Point2D = Point2D(x=10, y=20)
        y: Int = point.y
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{y.variable_name} = {point.variable_name}["y"];'
        )
        assert expected in expression
