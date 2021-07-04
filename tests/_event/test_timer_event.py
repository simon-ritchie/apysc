from random import randint
from typing import Any
from typing import Dict

from retrying import retry

from apysc import Event
from apysc import Timer
from apysc import TimerEvent
from apysc._expression import var_names
from tests.testing_helper import assert_raises


class TestTimerEvent:

    def on_timer(self, e: Event, options: Dict[str, Any]) -> None:
        """
        The handler would be called from a timer.

        Parameters
        ----------
        e : Event
            Event instance.
        options : dict
            Optional arguments dictionary.
        """

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        timer: Timer = Timer(handler=self.on_timer, delay=33)
        event: TimerEvent = TimerEvent(this=timer)
        assert event.variable_name.startswith(f'{var_names.TIMER_EVENT}_')
        assert event._this == timer

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_this(self) -> None:
        timer: Timer = Timer(handler=self.on_timer, delay=33)
        event: TimerEvent = TimerEvent(this=timer)
        assert event.this == timer

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_stop_propagation(self) -> None:
        timer: Timer = Timer(handler=self.on_timer, delay=33)
        event: TimerEvent = TimerEvent(this=timer)
        assert_raises(
            expected_error_class=NotImplementedError,
            func_or_method=event.stop_propagation,
            match=r'stop_propagation')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_prevent_default(self) -> None:
        timer: Timer = Timer(handler=self.on_timer, delay=33)
        event: TimerEvent = TimerEvent(this=timer)
        assert_raises(
            expected_error_class=NotImplementedError,
            func_or_method=event.prevent_default,
            match=r'prevent_default')
