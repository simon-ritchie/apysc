"""Class implementation for click interface.
"""

from typing import Any
from typing import Dict
from typing import Optional

from apysc._event.handler import Handler
from apysc._event.handler import HandlerData
from apysc._event.mouse_event_interface_base import MouseEventInterfaceBase


class ClickInterface(MouseEventInterfaceBase):

    _click_handlers: Dict[str, HandlerData]

    def click(
            self, handler: Handler,
            options: Optional[Dict[str, Any]] = None) -> str:
        """
        Add a click event listener setting.

        Parameters
        ----------
        handler : Handler
            A callable would be called when this instance is clicked.
        options : dict or None, default None
            Optional arguments dictionary to be passed to a handler.

        Returns
        -------
        name : str
            Handler's name.
        """
        from apysc import MouseEvent
        from apysc import MouseEventType
        from apysc._event.handler import append_handler_expression
        from apysc._event.handler import get_handler_name
        from apysc._type.variable_name_interface import VariableNameInterface
        self_instance: VariableNameInterface = \
            self._validate_self_is_variable_name_interface()
        self._initialize_click_handlers_if_not_initialized()
        name: str = get_handler_name(handler=handler, instance=self)
        self._set_mouse_event_handler_data(
            handler=handler, handlers_dict=self._click_handlers,
            options=options)
        self._append_mouse_event_binding_expression(
            name=name, mouse_event_type=MouseEventType.CLICK)
        e: MouseEvent = MouseEvent(this=self_instance)
        append_handler_expression(
            handler_data=self._click_handlers[name],
            handler_name=name, e=e)
        return name

    def _initialize_click_handlers_if_not_initialized(self) -> None:
        """
        Initialize _click_handlers attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_click_handlers'):
            return
        self._click_handlers = {}

    def unbind_click(self, handler: Handler) -> None:
        """
        Unbind specified handler's click event.

        Parameters
        ----------
        handler : Handler
            Callable to be unbinded.
        """
        from apysc import MouseEventType
        self._initialize_click_handlers_if_not_initialized()
        self._unbind_mouse_event(
            handler=handler, mouse_event_type=MouseEventType.CLICK,
            handlers_dict=self._click_handlers)

    def unbind_click_all(self) -> None:
        """
        Unbind all click events.
        """
        from apysc import MouseEventType
        self._initialize_click_handlers_if_not_initialized()
        self._unbind_all_mouse_events(
            mouse_event_type=MouseEventType.CLICK,
            handlers_dict=self._click_handlers)
