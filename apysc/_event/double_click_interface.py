"""Class implementation for double click interface.
"""

from typing import Any
from typing import Dict
from typing import Optional

from apysc._event.handler import Handler
from apysc._event.handler import HandlerData
from apysc._event.mouse_event_interface_base import MouseEventInterfaceBase


class DoubleClickInterface(MouseEventInterfaceBase):

    _dblclick_handlers: Dict[str, HandlerData]

    def dblclick(
            self, handler: Handler,
            options: Optional[Dict[str, Any]] = None) -> str:
        """
        Add double click event listener setting.

        Parameters
        ----------
        handler : Handler
            Callable that called when this instance is double clicked.
        options : dict or None, default None
            Optional arguments dictionary to be passed to handler.

        Returns
        -------
        name : str
            Handler's name.
        """
        import apysc as ap
        from apysc._validation.variable_name_validation import \
            validate_variable_name_interface_type
        with ap.DebugInfo(
                callable_=self.dblclick, locals_=locals(),
                module_name=__name__, class_=DoubleClickInterface):
            from apysc._event.handler import append_handler_expression
            from apysc._event.handler import get_handler_name
            from apysc._type.variable_name_interface import \
                VariableNameInterface
            self_instance: VariableNameInterface = \
                validate_variable_name_interface_type(instance=self)
            self._initialize_dblclick_handlers_if_not_initialized()
            name: str = get_handler_name(handler=handler, instance=self)
            self._set_mouse_event_handler_data(
                handler=handler, handlers_dict=self._dblclick_handlers,
                options=options)
            self._append_mouse_event_binding_expression(
                name=name, mouse_event_type=ap.MouseEventType.DBLCLICK)
            e: ap.MouseEvent = ap.MouseEvent(this=self_instance)
            append_handler_expression(
                handler_data=self._dblclick_handlers[name],
                handler_name=name, e=e)
            return name

    def _initialize_dblclick_handlers_if_not_initialized(self) -> None:
        """
        Initialize _dblclick_handlers attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_dblclick_handlers'):
            return
        self._dblclick_handlers = {}

    def unbind_dblclick(self, handler: Handler) -> None:
        """
        Unbind specified handler's double click event.

        Parameters
        ----------
        handler : Handler
            Callable to be unbinded.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.unbind_dblclick, locals_=locals(),
                module_name=__name__, class_=DoubleClickInterface):
            self._initialize_dblclick_handlers_if_not_initialized()
            self._unbind_mouse_event(
                handler=handler, mouse_event_type=ap.MouseEventType.DBLCLICK,
                handlers_dict=self._dblclick_handlers)

    def unbind_dblclick_all(self) -> None:
        """
        Unbind all double click events.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.unbind_dblclick_all, locals_=locals(),
                module_name=__name__, class_=DoubleClickInterface):
            self._initialize_dblclick_handlers_if_not_initialized()
            self._unbind_all_mouse_events(
                mouse_event_type=ap.MouseEventType.DBLCLICK,
                handlers_dict=self._dblclick_handlers)
