from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import var_names
from tests.testing_helper import assert_attrs


class TestPoint2D:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        point: ap.Point2D = ap.Point2D(x=10, y=20)
        assert_attrs(
            expected_attrs={
                '_x': 10,
                '_y': 20,
            },
            any_obj=point)
        assert isinstance(point._x, ap.Int)
        assert isinstance(point._y, ap.Int)
        assert point.variable_name.startswith(f'{var_names.POINT2D}_')

        x: ap.Int = ap.Int(10)
        y: ap.Int = ap.Int(20)
        point = ap.Point2D(x=x, y=y)
        assert_attrs(
            expected_attrs={
                '_x': x,
                '_y': y,
            },
            any_obj=point)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_x(self) -> None:
        point: ap.Point2D = ap.Point2D(x=10, y=20)
        x: ap.Int = point.x
        assert isinstance(x, ap.Int)
        assert x == 10

        point.x = 20  # type: ignore
        assert point.x == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_y(self) -> None:
        point: ap.Point2D = ap.Point2D(x=10, y=20)
        y: ap.Int = point.y
        assert isinstance(y, ap.Int)
        assert y == 20

        point.y = 30  # type: ignore
        assert point.y == 30

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___eq__(self) -> None:
        point: ap.Point2D = ap.Point2D(x=10, y=20)
        result: ap.Boolean = point == 20
        assert isinstance(result, ap.Boolean)
        assert not result

        result = point == ap.Point2D(x=10, y=20)
        assert isinstance(result, ap.Boolean)
        assert result

        result = point == ap.Point2D(x=20, y=20)
        assert isinstance(result, ap.Boolean)
        assert not result

        result = point == ap.Point2D(x=10, y=30)
        assert not result

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___ne__(self) -> None:
        point: ap.Point2D = ap.Point2D(x=10, y=20)
        result: ap.Boolean = point != ap.Point2D(x=20, y=20)
        assert result

        result = point != ap.Point2D(x=10, y=20)
        assert not result

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_constructor_expression(self) -> None:
        expression_data_util.empty_expression()
        x: ap.Int = ap.Int(10)
        y: ap.Int = ap.Int(20)
        point: ap.Point2D = ap.Point2D(x=x, y=y)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{point.variable_name} = '
            f'{{"x": {x.variable_name}, "y": {y.variable_name}}};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_x_getter_expression(self) -> None:
        expression_data_util.empty_expression()
        point: ap.Point2D = ap.Point2D(x=10, y=20)
        x: ap.Int = point.x
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{x.variable_name} = {point.variable_name}["x"];'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_y_getter_expression(self) -> None:
        expression_data_util.empty_expression()
        point: ap.Point2D = ap.Point2D(x=10, y=20)
        y: ap.Int = point.y
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{y.variable_name} = {point.variable_name}["y"];'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_x_setter_expression(self) -> None:
        expression_data_util.empty_expression()
        point: ap.Point2D = ap.Point2D(x=10, y=20)
        x: ap.Int = ap.Int(20)
        point.x = x
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{point.variable_name}["x"] = {x.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_y_setter_expression(self) -> None:
        expression_data_util.empty_expression()
        point: ap.Point2D = ap.Point2D(x=10, y=20)
        y: ap.Int = ap.Int(30)
        point.y = y
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{point.variable_name}["y"] = {y.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        point: ap.Point2D = ap.Point2D(x=10, y=20)
        snapshot_name: str = point._get_next_snapshot_name()
        point._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert point._x_snapshots == {snapshot_name: 10}
        assert point._y_snapshots == {snapshot_name: 20}

        point.x = 30  # type: ignore
        point.y = 40  # type: ignore
        point._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert point._x_snapshots == {snapshot_name: 10}
        assert point._y_snapshots == {snapshot_name: 20}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        point: ap.Point2D = ap.Point2D(x=10, y=20)
        snapshot_name: str = point._get_next_snapshot_name()
        point._run_all_revert_methods(snapshot_name=snapshot_name)

        point._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        point.x = 30  # type: ignore
        point.y = 40  # type: ignore
        point._run_all_revert_methods(snapshot_name=snapshot_name)
        assert point.x == 10
        assert point.y == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___repr__(self) -> None:
        point: ap.Point2D = ap.Point2D(x=10, y=20)
        repr_str: str = repr(point)
        assert repr_str == 'Point2D(Int(10), Int(20))'
