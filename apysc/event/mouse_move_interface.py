"""Class implementation for mouse move interface.
"""

from typing import Any
from typing import Dict
from typing import Optional

from apysc.event.event_interface_base import EventInterfaceBase
from apysc.event.handler import Handler
from apysc.event.handler import HandlerData


class MouseMoveInterface(EventInterfaceBase):

    _mouse_move_handlers: Dict[str, HandlerData]

    def mousemove(
            self, handler: Handler,
            options: Optional[Dict[str, Any]] = None) -> str:
        """
        Add mouse move event listener setting.

        Parameters
        ----------
        handler : Handler
            Callable that called when mouse is moved on this instance.
        options : dict or None, default None
            Optional arguments dictionary to be passed to handler.

        Returns
        -------
        name : str
            Handler's name.
        """
        from apysc import EventType
        from apysc import MouseEvent
        from apysc.event.handler import append_handler_expression
        from apysc.event.handler import get_handler_name
        from apysc.type.variable_name_interface import VariableNameInterface
        self_instance: VariableNameInterface = \
            self._validate_self_is_variable_name_interface()
        self._initialize_mouse_move_handlers_if_not_initialized()
        name: str = get_handler_name(handler=handler, instance=self)
        self._set_handler_data(
            handler=handler, handlers_dict=self._mouse_move_handlers,
            options=options)
        self._append_event_binding_expression(
            name=name, event_type=EventType.MOUSEMOVE)
        e: MouseEvent = MouseEvent(this=self_instance)
        append_handler_expression(
            handler_data=self._mouse_move_handlers[name],
            handler_name=name, e=e)
        return name

    def _initialize_mouse_move_handlers_if_not_initialized(self) -> None:
        """
        Initialize _mouse_move_handlers attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_mouse_move_handlers'):
            return
        self._mouse_move_handlers = {}

    def unbind_mousemove(self, handler: Handler) -> None:
        """
        Unbind specified handler's mouse move event.

        Parameters
        ----------
        handler : Handler
            Callable to be unbinded.
        """
        from apysc import EventType
        self._initialize_mouse_move_handlers_if_not_initialized()
        self._unbind_event(
            handler=handler, event_type=EventType.MOUSEMOVE,
            handlers_dict=self._mouse_move_handlers)

    def unbind_mousemove_all(self) -> None:
        """
        Unbind all mouse move events.
        """
        from apysc import EventType
        self._initialize_mouse_move_handlers_if_not_initialized()
        self._unbind_all_events(
            event_type=EventType.MOUSEMOVE,
            handlers_dict=self._mouse_move_handlers)
