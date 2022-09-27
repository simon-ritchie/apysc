from random import randint
from typing import Dict

from retrying import retry

from apysc._event.set_handler_data_interface import SetHandlerDataInterface
import apysc as ap
from apysc._event.handler import HandlerData
from apysc._event.handler import get_handler_name


class _TestInterface1(SetHandlerDataInterface[ap.MouseEvent]):
    pass


class TestSetHandlerDataInterface:

    def on_click(self, e: ap.MouseEvent, options: dict) -> None:
        """
        The test hadnler method.

        Parameters
        ----------
        e : ap.MouseEvent
            Event instance.
        options : dict
            Optional arguments dictionary.
        """

    def test__set_handler_data(self) -> None:
        handlers_dict: Dict[str, HandlerData] = {}
        interface: _TestInterface1 = _TestInterface1()
        interface._set_handler_data(
            handler=self.on_click,
            handlers_dict=handlers_dict,
            options={"msg": "Hello!"},
        )
        name: str = get_handler_name(handler=self.on_click, instance=interface)
        handler_data: HandlerData[ap.MouseEvent] = HandlerData(
            handler=self.on_click, options={"msg": "Hello!"}
        )
        assert handlers_dict[name] == handler_data


