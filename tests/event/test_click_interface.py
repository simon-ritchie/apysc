from random import randint
from typing import Any, Dict

from retrying import retry

from apysc.event.click_interface import ClickInterface
from apysc import Event


class TestClickInterface:

    def on_click_1(self, e: Event, kwargs: Dict[str, Any]) -> None:
        """
        Click handler method for testing.

        Parameters
        ----------
        e : Event
            Created event instance.
        kwargs : dict
            Keyword arguments to pass to.
        """

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_click(self) -> None:
        interface_1: ClickInterface = ClickInterface()
        name: str = interface_1.click(
            handler=self.on_click_1)
        assert interface_1._click_handlers[
            name]['handler'] == self.on_click_1
        assert interface_1._click_handlers[name]['kwargs'] == {}

        interface_2: ClickInterface = ClickInterface()
        name = interface_2.click(handler=self.on_click_1, kwargs={'a': 10})
        assert interface_2._click_handlers[
            name]['kwargs'] == {'a': 10}
