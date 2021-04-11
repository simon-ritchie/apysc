from random import randint

from retrying import retry

from typing import Any, Dict
from apysc.event import handler
from apysc import Boolean
from apysc import Event


class _TestClass1:

    def on_click_1(self, e: Event, kwargs: Dict[str, Any]) -> None:
        """
        Test handler.

        Parameters
        ----------
        e : Event
            Created event instance.
        kwargs : dict
            Keyword arguments to pass to.
        """


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_get_handler_name() -> None:
    test_instance = _TestClass1()
    handler_name: str = handler.get_handler_name(
        handler=test_instance.on_click_1)
    assert 'tests_event_test_handler' in handler_name
    assert '_TestClass1_' in handler_name
    assert 'on_click_1' in handler_name
