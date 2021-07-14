from random import randint

import pytest
from retrying import retry

import apysc as ap
from apysc._expression import expression_file_util
from apysc._expression import var_names
from tests import testing_helper


class TestWheelEvent:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        e: ap.WheelEvent = ap.WheelEvent()
        assert e.variable_name.startswith(f'{var_names.WHEEL_EVENT}_')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_this(self) -> None:
        e: ap.WheelEvent = ap.WheelEvent()
        with pytest.raises(
                Exception, match='WheelEvent'):  # type: ignore
            e.this

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_delta_y(self) -> None:
        e: ap.WheelEvent = ap.WheelEvent()
        delta_y: ap.Int = e.delta_y
        assert isinstance(delta_y, ap.Int)
        assert delta_y == 0

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_delta_y_getter_expression(self) -> None:
        expression_file_util.remove_expression_file()
        e: ap.WheelEvent = ap.WheelEvent()
        delta_y: ap.Int = e.delta_y
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{delta_y.variable_name} = '
            f'{e.variable_name}.deltaY;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_delta_x(self) -> None:
        e: ap.WheelEvent = ap.WheelEvent()
        delta_x: ap.Int = e.delta_x
        assert isinstance(delta_x, ap.Int)
        assert delta_x == 0

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_delta_x_getter_expression(self) -> None:
        expression_file_util.remove_expression_file()
        e: ap.WheelEvent = ap.WheelEvent()
        delta_x: ap.Int = e.delta_x
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{delta_x.variable_name} = '
            f'{e.variable_name}.deltaX;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_prevent_default(self) -> None:
        e: ap.WheelEvent = ap.WheelEvent()
        testing_helper.assert_raises(
            expected_error_class=Exception,
            func_or_method=e.prevent_default)
