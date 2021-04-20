from random import randint
from typing import Any, Dict

from retrying import retry

from apysc.event.event_interface_base import EventInterfaceBase
from apysc.event.handler import Handler
from apysc.event.handler import HandlerData
from apysc import MouseEvent
from tests import testing_helper
from apysc.event.handler import get_handler_name


class TestEventInterfaceBase:

    def on_click_1(self, e: MouseEvent, kwargs: Dict[str, Any]) -> None:
        """
        Test handler method.

        Parameters
        ----------
        e : MouseEvent
            Event instance.
        kwargs : dict
            Keyword arguments.
        """

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_validate_self_is_variable_name_interface(self) -> None:
        interface_1: EventInterfaceBase = EventInterfaceBase()
        testing_helper.assert_raises(
            expected_error_class=TypeError,
            func_or_method=interface_1.
            validate_self_is_variable_name_interface,
            match=interface_1.VARIABLE_NAME_INTERFACE_TYPE_ERR_MSG)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__set_handler_data(self) -> None:
        handlers_dict: Dict[str, HandlerData] = {}
        interface_1: EventInterfaceBase = EventInterfaceBase()
        interface_1._set_handler_data(
            handler=self.on_click_1,
            handlers_dict=handlers_dict,
            kwargs=None)
        name: str = get_handler_name(handler=self.on_click_1)
        assert handlers_dict == {
            name: {
                'handler': self.on_click_1,
                'kwargs': {},
            }
        }
