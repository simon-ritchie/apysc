from random import randint

from retrying import retry
import pytest

from apysc import WheelEvent
from apysc.expression import var_names
from apysc import Int
from apysc.expression import expression_file_util
from tests import testing_helper


class TestWheelEvent:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        e: WheelEvent = WheelEvent()
        assert e.variable_name.startswith(f'{var_names.MOUSE_WHEEL_EVENT}_')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_this(self) -> None:
        e: WheelEvent = WheelEvent()
        with pytest.raises(
                Exception, match='WheelEvent'):  # type: ignore
            e.this

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_delta_y(self) -> None:
        e: WheelEvent = WheelEvent()
        delta_y: Int = e.delta_y
        assert isinstance(delta_y, Int)
        assert delta_y == 0

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_delta_y_getter_expression(self) -> None:
        expression_file_util.remove_expression_file()
        e: WheelEvent = WheelEvent()
        delta_y: Int = e.delta_y
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{delta_y.variable_name} = '
            f'{e.variable_name}.deltaY;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_delta_x(self) -> None:
        e: WheelEvent = WheelEvent()
        delta_x: Int = e.delta_x
        assert isinstance(delta_x, Int)
        assert delta_x == 0

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_delta_x_getter_expression(self) -> None:
        expression_file_util.remove_expression_file()
        e: WheelEvent = WheelEvent()
        delta_x: Int = e.delta_x
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{delta_x.variable_name} = '
            f'{e.variable_name}.deltaX;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_prevent_default(self) -> None:
        e: WheelEvent = WheelEvent()
        testing_helper.assert_raises(
            expected_error_class=Exception,
            func_or_method=e.prevent_default)
