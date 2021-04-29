"""Class implementation for each event interfaces' base class.
"""

from typing import Any
from typing import Dict
from typing import Optional

from apysc.event.event_type import EventType
from apysc.event.handler import Handler
from apysc.event.handler import HandlerData
from apysc.type.variable_name_interface import VariableNameInterface


class EventInterfaceBase:

    def _validate_self_is_variable_name_interface(
            self) -> VariableNameInterface:
        """
        Validate whether this instance is a VariableNameInterface
        instance or not.

        Returns
        -------
        self_instance : VariableNameInterface
            This instance.

        Raises
        ------
        TypeError
            If this instance is not a VariableNameInterface.
        """
        from apysc.validation.variable_name_validation import \
            validate_variable_name_interface_type
        return validate_variable_name_interface_type(instance=self)

    def _set_handler_data(
            self, handler: Handler,
            handlers_dict: Dict[str, HandlerData],
            options: Optional[Dict[str, Any]]) -> None:
        """
        Set handler's data to the given dictionary.

        Parameters
        ----------
        handler : Handler
            Callable that called when event is dispatched.
        handlers_dict : dict
            Dictionary to be set handler's data.
        options : dict or None, default None
            Optional arguments dictionary to be passed to handler.
        """
        from apysc.event.handler import get_handler_name
        name: str = get_handler_name(handler=handler, instance=self)
        if options is None:
            options = {}
        handlers_dict[name] = {
            'handler': handler,
            'options': options,
        }

    def _unbind_event(
            self, handler: Handler, event_type: EventType,
            handlers_dict: Dict[str, HandlerData]) -> None:
        """
        Unbind specified handler's event.

        Parameters
        ----------
        handler : Handler
            Callable to be unbinded.
        event_type : EventType
            Event type to unbind.
        handlers_dict : dict
            Dictionary that has handler's data.
        """
        from apysc.event.handler import append_unbinding_expression
        from apysc.event.handler import get_handler_name
        self_instance: VariableNameInterface = \
            self._validate_self_is_variable_name_interface()
        name: str = get_handler_name(handler=handler, instance=self)
        if name in handlers_dict:
            del handlers_dict[name]
        append_unbinding_expression(
            this=self_instance, handler_name=name,
            event_type=event_type)

    def _unbind_all_events(
            self, event_type: EventType,
            handlers_dict: Dict[str, HandlerData]) -> None:
        """
        Unbind specified all event type's events.

        Parameters
        ----------
        event_type : EventType
            Event type to unbind.
        handlers_dict : dict
            Dictionary that has handler's data.
        """
        from apysc.event.handler import append_unbinding_all_expression
        self_instance: VariableNameInterface = \
            self._validate_self_is_variable_name_interface()
        handlers_dict.clear()
        append_unbinding_all_expression(
            this=self_instance, event_type=event_type)

    def _append_event_binding_expression(
            self, name: str, event_type: EventType) -> None:
        """
        Append event binding expression to file.

        Parameters
        ----------
        name : str
            Handler's name.
        event_type : EventType
            Event type to bind.
        """
        from apysc.expression import expression_file_util
        from apysc.type.variable_name_interface import VariableNameInterface
        self_instance: VariableNameInterface = \
            self._validate_self_is_variable_name_interface()
        expression: str = (
            f'{self_instance.variable_name}'
            f'.{event_type.value}({name});'
        )
        expression_file_util.append_js_expression(expression=expression)
