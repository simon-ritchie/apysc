from random import randint
from typing import Any
from typing import Dict

from retrying import retry

import apysc as ap
from apysc._expression import var_names
from tests.testing_helper import assert_raises


class TestTimerEvent:

    def on_timer(self, e: ap.Event, options: Dict[str, Any]) -> None:
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
        timer: ap.Timer = ap.Timer(handler=self.on_timer, delay=33)
        event: ap.TimerEvent = ap.TimerEvent(this=timer)
        assert event.variable_name.startswith(f'{var_names.TIMER_EVENT}_')
        assert event._this == timer

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_this(self) -> None:
        timer: ap.Timer = ap.Timer(handler=self.on_timer, delay=33)
        event: ap.TimerEvent = ap.TimerEvent(this=timer)
        assert event.this == timer

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_prevent_default(self) -> None:
        timer: ap.Timer = ap.Timer(handler=self.on_timer, delay=33)
        event: ap.TimerEvent = ap.TimerEvent(this=timer)
        assert_raises(
            expected_error_class=NotImplementedError,
            func_or_method=event.prevent_default,
            match=r'prevent_default')
