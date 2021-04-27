from random import randint

from retrying import retry
import pytest

from apysc import WheelEvent
from apysc.expression import var_names
from apysc import Int
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
