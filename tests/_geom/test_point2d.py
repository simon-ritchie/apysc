import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs


class TestPoint2D:
    @apply_test_settings()
    def test___init__(self) -> None:
        point: ap.Point2D = ap.Point2D(x=10, y=20, variable_name_suffix="test_point")
        assert_attrs(
            expected_attrs={
                "_x": 10,
                "_y": 20,
            },
            any_obj=point,
        )
        assert isinstance(point._x, ap.Number)
        assert isinstance(point._y, ap.Number)
        assert point.variable_name.startswith(f"{var_names.POINT2D}_")
        assert point._variable_name_suffix == "test_point"
        assert point._x._variable_name_suffix == "test_point__x"
        assert point._y._variable_name_suffix == "test_point__y"

        x: ap.Number = ap.Number(10)
        y: ap.Number = ap.Number(20)
        point = ap.Point2D(x=x, y=y)
        assert_attrs(
            expected_attrs={
                "_x": x,
                "_y": y,
            },
            any_obj=point,
        )

    @apply_test_settings()
    def test_x(self) -> None:
        point: ap.Point2D = ap.Point2D(x=10, y=20, variable_name_suffix="test_point")
        x: ap.Number = point.x
        assert isinstance(x, ap.Number)
        assert x == 10
        assert x._variable_name_suffix == "test_point__x"

        point.x += 20
        assert point.x == 30

    @apply_test_settings()
    def test_y(self) -> None:
        point: ap.Point2D = ap.Point2D(x=10, y=20, variable_name_suffix="test_point")
        y: ap.Number = point.y
        assert isinstance(y, ap.Number)
        assert y == 20
        assert y._variable_name_suffix == "test_point__y"

        point.y += 20
        assert point.y == 40

    @apply_test_settings()
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

    @apply_test_settings()
    def test___ne__(self) -> None:
        point: ap.Point2D = ap.Point2D(x=10, y=20)
        result: ap.Boolean = point != ap.Point2D(x=20, y=20)
        assert result

        result = point != ap.Point2D(x=10, y=20)
        assert not result

    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        ap.Stage()
        x: ap.Number = ap.Number(10)
        y: ap.Number = ap.Number(20)
        point: ap.Point2D = ap.Point2D(x=x, y=y)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{point.variable_name} = "
            f'{{"x": {x.variable_name}, "y": {y.variable_name}}};'
        )
        assert expected in expression

    @apply_test_settings()
    def test__append_x_getter_expression(self) -> None:
        ap.Stage()
        point: ap.Point2D = ap.Point2D(x=10, y=20)
        x: ap.Number = point.x
        expression: str = expression_data_util.get_current_expression()
        expected: str = f'{x.variable_name} = {point.variable_name}["x"];'
        assert expected in expression

    @apply_test_settings()
    def test__append_y_getter_expression(self) -> None:
        ap.Stage()
        point: ap.Point2D = ap.Point2D(x=10, y=20)
        y: ap.Number = point.y
        expression: str = expression_data_util.get_current_expression()
        expected: str = f'{y.variable_name} = {point.variable_name}["y"];'
        assert expected in expression

    @apply_test_settings()
    def test__append_x_setter_expression(self) -> None:
        ap.Stage()
        point: ap.Point2D = ap.Point2D(x=10, y=20)
        x: ap.Number = ap.Number(20)
        point.x = x
        expression: str = expression_data_util.get_current_expression()
        expected: str = f'{point.variable_name}["x"] = {x.variable_name};'
        assert expected in expression

    @apply_test_settings()
    def test__append_y_setter_expression(self) -> None:
        ap.Stage()
        point: ap.Point2D = ap.Point2D(x=10, y=20)
        y: ap.Number = ap.Number(30)
        point.y = y
        expression: str = expression_data_util.get_current_expression()
        expected: str = f'{point.variable_name}["y"] = {y.variable_name};'
        assert expected in expression

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        point: ap.Point2D = ap.Point2D(x=10, y=20)
        snapshot_name: str = point._get_next_snapshot_name()
        point._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert point._x_snapshots == {snapshot_name: 10}
        assert point._y_snapshots == {snapshot_name: 20}

        point.x = ap.Number(30)
        point.y = ap.Number(40)
        point._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert point._x_snapshots == {snapshot_name: 10}
        assert point._y_snapshots == {snapshot_name: 20}

    @apply_test_settings()
    def test__revert(self) -> None:
        point: ap.Point2D = ap.Point2D(x=10, y=20)
        snapshot_name: str = point._get_next_snapshot_name()
        point._run_all_revert_methods(snapshot_name=snapshot_name)

        point._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        point.x = ap.Number(30)
        point.y = ap.Number(40)
        point._run_all_revert_methods(snapshot_name=snapshot_name)
        assert point.x == 10
        assert point.y == 20

    @apply_test_settings()
    def test___repr__(self) -> None:
        point: ap.Point2D = ap.Point2D(x=10, y=20)
        repr_str: str = repr(point)
        assert repr_str == "Point2D(Number(10.0), Number(20.0))"
