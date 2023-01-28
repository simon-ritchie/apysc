from random import randint
from typing import Any
from typing import Dict

from retrying import retry

import apysc as ap
from apysc._event.custom_event_mixin import CustomEventMixIn
from apysc._event.custom_event_type import CustomEventType
from apysc._expression import expression_data_util
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._testing.testing_helper import apply_test_settings


class _TestObject(CustomEventMixIn, VariableNameMixIn):
    def __init__(self) -> None:
        """
        Test object class.
        """
        self.variable_name = "test_object"


class TestCustomEventMixIn:
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

    @apply_test_settings()
    def test__get_custom_event_type_str(self) -> None:
        mixin: CustomEventMixIn = CustomEventMixIn()
        custom_event_type_str: str = mixin._get_custom_event_type_str(
            custom_event_type="test_custom_event"
        )
        assert custom_event_type_str == "test_custom_event"

        custom_event_type_str = mixin._get_custom_event_type_str(
            custom_event_type=CustomEventType.TIMER_COMPLETE
        )
        assert custom_event_type_str == CustomEventType.TIMER_COMPLETE.value
        assert isinstance(custom_event_type_str, str)

    @apply_test_settings()
    def test__initialize_custom_event_handlers_if_not_initialized(self) -> None:
        mixin: CustomEventMixIn = CustomEventMixIn()
        mixin._initialize_custom_event_handlers_if_not_initialized(
            custom_event_type_str="test_custom_event"
        )
        assert "test_custom_event" in mixin._custom_event_handlers

    @apply_test_settings()
    def test__append_custom_event_binding_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: _TestObject = _TestObject()
        e: ap.Event = ap.Event(this=mixin)
        name: str = mixin.bind_custom_event(
            custom_event_type="test_custom_event", handler=self.on_custom_event, e=e
        )
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"$({mixin.blank_object_variable_name})"
            f'.off("test_custom_event", {name});'
            f"\n$({mixin.blank_object_variable_name})"
            f'.on("test_custom_event", {name});'
        )
        assert expected in expression

    @apply_test_settings()
    def test_bind_custom_event(self) -> None:
        expression_data_util.empty_expression()
        mixin: _TestObject = _TestObject()
        e: ap.Event = ap.Event(this=mixin)
        name: str = mixin.bind_custom_event(
            custom_event_type="test_custom_event",
            handler=self.on_custom_event,
            e=e,
            in_handler_head_expression='console.log("hello");',
        )
        expression: str = (
            expression_data_util.get_current_event_handler_scope_expression()
        )
        expected: str = f"function {name}({e.variable_name}) {{"
        assert expected in expression
        assert 'console.log("hello");' in expression

    @apply_test_settings()
    def test_trigger_custom_event(self) -> None:
        expression_data_util.empty_expression()
        mixin: _TestObject = _TestObject()
        mixin.trigger_custom_event(custom_event_type="test_event")
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"$({mixin.blank_object_variable_name})" f'.trigger("test_event");'
        )
        assert expected in expression

    @apply_test_settings()
    def test__unset_custom_event_handler_data(self) -> None:
        mixin: _TestObject = _TestObject()
        mixin._custom_event_handlers = {}
        mixin._unset_custom_event_handler_data(
            handler=self.on_custom_event, custom_event_type_str="test_event"
        )
        assert mixin._custom_event_handlers == {}

        mixin._initialize_custom_event_handlers_if_not_initialized(
            custom_event_type_str="test_event"
        )
        mixin._unset_custom_event_handler_data(
            handler=self.on_custom_event, custom_event_type_str="test_event"
        )
        assert mixin._custom_event_handlers == {"test_event": {}}

        mixin._set_handler_data(
            handler=self.on_custom_event,
            handlers_dict=mixin._custom_event_handlers["test_event"],
            options=None,
        )
        mixin._unset_custom_event_handler_data(
            handler=self.on_custom_event, custom_event_type_str="test_event"
        )
        assert mixin._custom_event_handlers == {"test_event": {}}

    @apply_test_settings()
    def test__append_custom_event_unbinding_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: _TestObject = _TestObject()
        name: str = mixin.unbind_custom_event(
            custom_event_type="test_event", handler=self.on_custom_event
        )
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"$({mixin.blank_object_variable_name})" f'.off("test_event", {name});'
        )
        assert expected in expression

    @apply_test_settings()
    def test_unbind_custom_event(self) -> None:
        expression_data_util.empty_expression()
        mixin: _TestObject = _TestObject()
        e: ap.Event = ap.Event(this=mixin)
        name_1: str = mixin.bind_custom_event(
            custom_event_type="test_event", handler=self.on_custom_event, e=e
        )
        name_2: str = mixin.unbind_custom_event(
            custom_event_type="test_event", handler=self.on_custom_event
        )
        assert name_1 == name_2
        assert mixin._custom_event_handlers == {"test_event": {}}
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"$({mixin.blank_object_variable_name})" f'.off("test_event", {name_2});'
        )
        assert expected in expression

    @apply_test_settings()
    def test_unbind_custom_event_all(self) -> None:
        expression_data_util.empty_expression()
        mixin: _TestObject = _TestObject()
        e: ap.Event = ap.Event(this=mixin)
        mixin.bind_custom_event(
            custom_event_type="test_event", handler=self.on_custom_event, e=e
        )
        mixin.unbind_custom_event_all(custom_event_type="test_event")
        assert mixin._custom_event_handlers == {"test_event": {}}
        expression: str = expression_data_util.get_current_expression()
        expected: str = f'$({mixin.blank_object_variable_name}).off("test_event");'
        assert expected in expression
