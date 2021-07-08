"""Class implementation for each mouse event interface's base class.
"""

from typing import Any
from typing import Dict
from typing import Optional

from apysc._event.handler import Handler
from apysc._event.handler import HandlerData
from apysc._event.mouse_event_type import MouseEventType
from apysc._type.variable_name_interface import VariableNameInterface


class MouseEventInterfaceBase:

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
        from apysc._validation.variable_name_validation import \
            validate_variable_name_interface_type
        return validate_variable_name_interface_type(instance=self)

    def _set_mouse_event_handler_data(
            self, handler: Handler,
            handlers_dict: Dict[str, HandlerData],
            options: Optional[Dict[str, Any]]) -> None:
        """
        Set a handler's data to the given dictionary.

        Parameters
        ----------
        handler : Handler
            Callable would be called when event is dispatched.
        handlers_dict : dict
            Dictionary to be set handler's data.
        options : dict or None
            Optional arguments dictionary to be passed to handler.
        """
        from apysc._event.handler import get_handler_name
        name: str = get_handler_name(handler=handler, instance=self)
        if options is None:
            options = {}
        handlers_dict[name] = {
            'handler': handler,
            'options': options,
        }

    def _unbind_mouse_event(
            self, handler: Handler, mouse_event_type: MouseEventType,
            handlers_dict: Dict[str, HandlerData]) -> None:
        """
        Unbind specified handler's mouse event.

        Parameters
        ----------
        handler : Handler
            Callable to be unbinded.
        mouse_event_type : MouseEventType
            Event type to unbind.
        handlers_dict : dict
            Dictionary that has handler's data.
        """
        from apysc._event.handler import append_unbinding_expression
        from apysc._event.handler import get_handler_name
        self_instance: VariableNameInterface = \
            self._validate_self_is_variable_name_interface()
        name: str = get_handler_name(handler=handler, instance=self)
        if name in handlers_dict:
            del handlers_dict[name]
        append_unbinding_expression(
            this=self_instance, handler_name=name,
            mouse_event_type=mouse_event_type)

    def _unbind_all_mouse_events(
            self, mouse_event_type: MouseEventType,
            handlers_dict: Dict[str, HandlerData]) -> None:
        """
        Unbind specified all mouse event type's event.

        Parameters
        ----------
        mouse_event_type : MouseEventType
            Event type to unbind.
        handlers_dict : dict
            Dictionary that has handler's data.
        """
        from apysc._event.handler import append_unbinding_all_expression
        self_instance: VariableNameInterface = \
            self._validate_self_is_variable_name_interface()
        handlers_dict.clear()
        append_unbinding_all_expression(
            this=self_instance, mouse_event_type=mouse_event_type)

    def _append_mouse_event_binding_expression(
            self, name: str, mouse_event_type: MouseEventType) -> None:
        """
        Append a mouse event binding expression to the file.

        Parameters
        ----------
        name : str
            Handler's name.
        mouse_event_type : MouseEventType
            Event type to bind.
        """
        from apysc import append_js_expression
        from apysc._type.variable_name_interface import VariableNameInterface
        self_instance: VariableNameInterface = \
            self._validate_self_is_variable_name_interface()
        expression: str = (
            f'{self_instance.variable_name}'
            f'.{mouse_event_type.value}({name});'
        )
        append_js_expression(expression=expression)
