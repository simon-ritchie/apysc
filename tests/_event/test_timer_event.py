from random import randint
from typing import Any, Dict

from retrying import retry

from apysc import TimerEvent, Event
from apysc import Timer
from apysc._expression import var_names


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
