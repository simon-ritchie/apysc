from random import randint
from typing import Any
from typing import Dict

from retrying import retry

import apysc as ap
from apysc._event.custom_event_interface import CustomEventInterface
from apysc._event.custom_event_type import CustomEventType
from apysc._expression import expression_data_util
from apysc._type.variable_name_interface import VariableNameInterface


class _TestObject(CustomEventInterface, VariableNameInterface):

    def __init__(self) -> None:
        """
        Test object class.
        """
        self.variable_name = 'test_object'


class TestCustomEventInterface:

    def on_custom_event(self, e: ap.Event, options: Dict[str, Any]) -> None:
        """
        The test handler.

        Parameters
        ----------
        e : Event
            Event instance.
        options : dict
            Optional arguments dictionary.
        """

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_custom_event_type_str(self) -> None:
        interface: CustomEventInterface = CustomEventInterface()
        custom_event_type_str: str = interface._get_custom_event_type_str(
            custom_event_type='test_custom_event')
        assert custom_event_type_str == 'test_custom_event'

        custom_event_type_str = interface._get_custom_event_type_str(
            custom_event_type=CustomEventType.TIMER_COMPLETE)
        assert custom_event_type_str == CustomEventType.TIMER_COMPLETE.value
        assert isinstance(custom_event_type_str, str)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_custom_event_handlers_if_not_initialized(
            self) -> None:
        interface: CustomEventInterface = CustomEventInterface()
        interface._initialize_custom_event_handlers_if_not_initialized(
            custom_event_type_str='test_custom_event')
        assert 'test_custom_event' in interface._custom_event_handlers

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_custom_event_handler_data(self) -> None:
        interface: _TestObject = _TestObject()
        e: ap.Event = ap.Event(this=interface)
        name: str = interface.bind_custom_event(
            custom_event_type='test_custom_event',
            handler=self.on_custom_event,
            e=e)
        expected: Dict[str, Any] = {
            'handler': self.on_custom_event,
            'options': {},
        }
        assert interface._custom_event_handlers['test_custom_event'][name] == \
            expected

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_custom_event_binding_expression(self) -> None:
        expression_data_util.empty_expression()
        interface: _TestObject = _TestObject()
        e: ap.Event = ap.Event(this=interface)
        name: str = interface.bind_custom_event(
            custom_event_type='test_custom_event',
            handler=self.on_custom_event,
            e=e)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'$({interface.blank_object_variable_name})'
            f'.off("test_custom_event", {name});'
            f'\n$({interface.blank_object_variable_name})'
            f'.on("test_custom_event", {name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_bind_custom_event(self) -> None:
        expression_data_util.empty_expression()
        interface: _TestObject = _TestObject()
        e: ap.Event = ap.Event(this=interface)
        name: str = interface.bind_custom_event(
            custom_event_type='test_custom_event',
            handler=self.on_custom_event,
            e=e)
        expression: str = expression_data_util.\
            get_current_event_handler_scope_expression()
        expected: str = (
            f'function {name}({e.variable_name}) {{'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_trigger_custom_event(self) -> None:
        expression_data_util.empty_expression()
        interface: _TestObject = _TestObject()
        interface.trigger_custom_event(custom_event_type='test_event')
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'$({interface.blank_object_variable_name})'
            f'.trigger("test_event");'
        )
        assert expected in expression
