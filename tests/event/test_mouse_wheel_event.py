from random import randint

from retrying import retry
import pytest

from apysc import MouseWheelEvent
from apysc.expression import var_names
from tests import testing_helper


class TestMouseWheelEvent:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        e: MouseWheelEvent = MouseWheelEvent()
        assert e.variable_name.startswith(f'{var_names.MOUSE_WHEEL_EVENT}_')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_this(self) -> None:
        e: MouseWheelEvent = MouseWheelEvent()
        with pytest.raises(
                Exception, match='MouseWheelEvent'):  # type: ignore
            e.this
