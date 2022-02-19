"""Class implementation for each mouse event interface's base class.
"""

from typing import Callable
from typing import Dict
from typing import Optional
from typing import TypeVar

from apysc._event.handler import HandlerData
from apysc._event.mouse_event import MouseEvent
from apysc._event.mouse_event_type import MouseEventType
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.variable_name_interface import VariableNameInterface

_O = TypeVar('_O')
_Handler = Callable[[MouseEvent, _O], None]


class MouseEventInterfaceBase:

    def _set_mouse_event_handler_data(
            self, *, handler: _Handler[_O],
            handlers_dict: Dict[str, HandlerData],
            options: Optional[_O]) -> None:
        """
        Set a handler's data to the given dictionary.

        Parameters
        ----------
        handler : _Handler
            Callable that this instance calls when dispatching.
        handlers_dict : dict
            Dictionary that this instance sets a handler's data.
        options : dict or None
            Optional arguments dictionary that this instance passes
            to a handler.
        """
        from apysc._event.handler import get_handler_name
        from apysc._validation.handler_options_validation import \
            validate_options_type
        validate_options_type(options=options)
        name: str = get_handler_name(handler=handler, instance=self)
        if options is None:
            options = {}  # type: ignore
        handlers_dict[name] = {  # type: ignore
            'handler': handler,  # type: ignore
            'options': options,
        }

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='MouseEventInterfaceBase')
    def _unbind_mouse_event(
            self, *, handler: _Handler[_O], mouse_event_type: MouseEventType,
            handlers_dict: Dict[str, HandlerData]) -> None:
        """
        Unbind a specified handler's mouse event.

        Parameters
        ----------
        handler : _Handler
            Unbinding target Callable.
        mouse_event_type : MouseEventType
            Event type to unbind.
        handlers_dict : dict
            Dictionary that has handler's data.
        """
        from apysc._event.handler import append_unbinding_expression
        from apysc._event.handler import get_handler_name
        from apysc._validation.variable_name_validation import \
            validate_variable_name_interface_type
        self_instance: VariableNameInterface = \
            validate_variable_name_interface_type(instance=self)
        name: str = get_handler_name(handler=handler, instance=self)
        if name in handlers_dict:
            del handlers_dict[name]
        append_unbinding_expression(
            this=self_instance, handler_name=name,
            mouse_event_type=mouse_event_type)

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='MouseEventInterfaceBase')
    def _unbind_all_mouse_events(
            self, *, mouse_event_type: MouseEventType,
            handlers_dict: Dict[str, HandlerData]) -> None:
        """
        Unbind specified all mouse event type's events.

        Parameters
        ----------
        mouse_event_type : MouseEventType
            Event type to unbind.
        handlers_dict : dict
            Dictionary that has handler's data.
        """
        from apysc._event.handler import append_unbinding_all_expression
        from apysc._validation.variable_name_validation import \
            validate_variable_name_interface_type
        self_instance: VariableNameInterface = \
            validate_variable_name_interface_type(instance=self)
        handlers_dict.clear()
        append_unbinding_all_expression(
            this=self_instance, mouse_event_type=mouse_event_type)

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='MouseEventInterfaceBase')
    def _append_mouse_event_binding_expression(
            self, *, name: str, mouse_event_type: MouseEventType) -> None:
        """
        Append a mouse event binding expression.

        Parameters
        ----------
        name : str
            Handler's name.
        mouse_event_type : MouseEventType
            Event type to bind.
        """
        import apysc as ap
        from apysc._type.variable_name_interface import VariableNameInterface
        from apysc._validation.variable_name_validation import \
            validate_variable_name_interface_type
        self_instance: VariableNameInterface = \
            validate_variable_name_interface_type(instance=self)
        expression: str = (
            f'{self_instance.variable_name}'
            f'.{mouse_event_type.value}({name});'
        )
        ap.append_js_expression(expression=expression)
