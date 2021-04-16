from random import randint

from retrying import retry

from apysc import MouseEvent, Int
from apysc.expression import var_names


class TestMouseEvent:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___init__(self) -> None:
        int_1: Int = Int(10)
        mouse_event: MouseEvent[Int] = MouseEvent(this=int_1)
        assert mouse_event.this == int_1
        assert mouse_event.variable_name.startswith(
            f'{var_names.MOUSE_EVENT}_')
