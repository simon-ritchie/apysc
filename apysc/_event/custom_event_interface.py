"""Class implementation for the custom event interface.
"""

from typing import Any, Union
from typing import Dict
from typing import Optional

from apysc._event.handler import Handler
from apysc._event.handler import HandlerData
from apysc._type.variable_name_interface import VariableNameInterface
from apysc._event.custom_event_type import CustomEventType
from apysc._type.blank_object_interface import BlankObjectInterface
from apysc._event.event import Event

_CustomEventType = str
_HandlerName = str


class CustomEventInterface(BlankObjectInterface):

    _custom_event_handlers: Dict[
        _CustomEventType, Dict[_HandlerName, HandlerData]]

    def _initialize_custom_event_handlers_if_not_initialized(
            self, custom_event_type_str: str) -> None:
        """
        Initialize the _custom_event_handlers data if it hasn't been
        initialized yet.

        Parameters
        ----------
        custom_event_type_str : str
            Target custom event type string.
        """
        if not hasattr(self, '_custom_event_handlers'):
            self._custom_event_handlers = {}
        if custom_event_type_str not in self._custom_event_handlers:
            self._custom_event_handlers[custom_event_type_str] = {}

    def _get_custom_event_type_str(
            self,
            custom_event_type: Union[CustomEventType, str]) -> str:
        """
        Get a custom event type string from a type value.

        Parameters
        ----------
        custom_event_type : CustomEventType or str
            Target custom event type or string.

        Returns
        -------
        custom_event_type_str : str
            A custom event type string.
        """
        if isinstance(custom_event_type, str):
            return custom_event_type
        custom_event_type_str: str = custom_event_type.value
        return custom_event_type_str

    def _set_custom_event_handler_data(
            self, handler: Handler,
            custom_event_type_str: str,
            options: Optional[Dict[str, Any]]) -> None:
        """
        Set a handler's data to the dictionary.

        Parameters
        ----------
        handler : Handler
            Callable would be called when event is dispatched.
        custom_event_type_str : str
            Target custom event type string.
        options : dict or None
            Optional arguments dictionary to be passed to a handler.
        """
        from apysc._event.handler import get_handler_name
        name: str = get_handler_name(handler=handler, instance=self)
        if options is None:
            options = {}
        self._custom_event_handlers[custom_event_type_str][name] = {
            'handler': handler,
            'options': options,
        }

    def bind_custom_event(
            self, custom_event_type: Union[CustomEventType, str],
            handler: Handler,
            e: Event,
            options: Optional[Dict[str, Any]] = None) -> str:
        """
        Add a custom event listener setting.

        Parameters
        ----------
        custom_event_type : CustomEventType or str
            Target custom event type.
        handler : Handler
            A handler would be called when the custom event is triggered.
        e : Event
            Event instance.
        options : dict or None, default None
            Optional arguments dictionary to be passed to a handler.

        Returns
        -------
        name : str
            Handler's name.
        """
        from apysc._event.handler import get_handler_name
        custom_event_type_str: str = self._get_custom_event_type_str(
            custom_event_type=custom_event_type)
        self._initialize_custom_event_handlers_if_not_initialized(
            custom_event_type_str=custom_event_type_str)
        self._set_custom_event_handler_data(
            handler=handler, custom_event_type_str=custom_event_type_str,
            options=options)
        name: str = get_handler_name(handler=handler, instance=self)
        # self._append_custom_event_binding_expression()
        return name
