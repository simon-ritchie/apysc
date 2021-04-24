"""Class implementation for each event interfaces' base class.
"""

from typing import Any, Dict, Optional
from typing_extensions import Final

from apysc.type.variable_name_interface import VariableNameInterface
from apysc.event.handler import Handler
from apysc.event.handler import HandlerData
from apysc.event.event_type import EventType


class EventInterfaceBase:

    VARIABLE_NAME_INTERFACE_TYPE_ERR_MSG: Final[str] = (
        'This interface can only be used that inheriting '
        'VariableNameInterface.'
    )

    def validate_self_is_variable_name_interface(
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
        if not isinstance(self, VariableNameInterface):
            raise TypeError(self.VARIABLE_NAME_INTERFACE_TYPE_ERR_MSG)
        return self

    def _set_handler_data(
            self, handler: Handler,
            handlers_dict: Dict[str, HandlerData],
            kwargs: Optional[Dict[str, Any]]) -> None:
        """
        Set handler's data to the given dictionary.

        Parameters
        ----------
        handler : Handler
            Callable that called when event is dispatched.
        handlers_dict : dict
            Dictionary to be set handler's data.
        kwargs : dict or None, default None
            Keyword arguments to be passed to handler.
        """
        from apysc.event.handler import get_handler_name
        name: str = get_handler_name(handler=handler)
        if kwargs is None:
            kwargs = {}
        handlers_dict[name] = {
            'handler': handler,
            'kwargs': kwargs,
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
        from apysc.event.handler import get_handler_name
        from apysc.event.handler import append_unbinding_expression
        self_instance: VariableNameInterface = \
            self.validate_self_is_variable_name_interface()
        name: str = get_handler_name(handler=handler)
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
            self.validate_self_is_variable_name_interface()
        handlers_dict.clear()
        append_unbinding_all_expression(
            this=self_instance, event_type=event_type)
