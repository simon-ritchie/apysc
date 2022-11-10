from typing import Dict

import apysc as ap
from apysc._event.handler import HandlerData
from apysc._event.handler import get_handler_name
from apysc._event.set_handler_data_mixin import SetHandlerDataMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn


class _TestMIxIn1(VariableNameMixIn, SetHandlerDataMixIn[ap.MouseEvent]):
    def __init__(self) -> None:
        """
        The mix-in for testing.
        """
        self.variable_name = "test_mixin"


class TestSetHandlerDataMixIn:
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
        mixin: _TestMIxIn1 = _TestMIxIn1()
        mixin._set_handler_data(
            handler=self.on_click,
            handlers_dict=handlers_dict,
            options={"msg": "Hello!"},
        )
        name: str = get_handler_name(handler=self.on_click, instance=mixin)
        handler_data: HandlerData[ap.MouseEvent] = HandlerData(
            handler=self.on_click, options={"msg": "Hello!"}
        )
        assert handlers_dict[name] == handler_data
