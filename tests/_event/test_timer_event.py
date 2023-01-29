from typing import Any
from typing import Dict

import apysc as ap
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings


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

    @apply_test_settings()
    def test___init__(self) -> None:
        timer: ap.Timer = ap.Timer(handler=self.on_timer, delay=33)
        event: ap.TimerEvent = ap.TimerEvent(this=timer)
        assert event.variable_name.startswith(f"{var_names.TIMER_EVENT}_")
        assert event._this == timer

    @apply_test_settings()
    def test_this(self) -> None:
        timer: ap.Timer = ap.Timer(handler=self.on_timer, delay=33)
        event: ap.TimerEvent = ap.TimerEvent(this=timer)
        assert event.this == timer
