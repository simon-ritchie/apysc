"""Class implementation for double click interface.
"""

from typing import Any
from typing import Dict
from typing import Optional

from apysc.event.event_interface_base import EventInterfaceBase
from apysc.event.handler import Handler
from apysc.event.handler import HandlerData


class DoubleClickInterface(EventInterfaceBase):

    _dblclick_handlers: Dict[str, HandlerData]

    def dblclick(
            self, handler: Handler,
            kwargs: Optional[Dict[str, Any]] = None) -> str:
        """
        Add double click event listener setting.

        Parameters
        ----------
        handler : Handler
            Callable that called when this instance is double clicked.
        kwargs : dict or None, default None
            Keyword arguments to be passed to handler.

        Returns
        -------
        name : str
            Handler's name.
        """
        from apysc import MouseEvent
        from apysc.event.handler import append_handler_expression
        from apysc.event.handler import get_handler_name
        from apysc.type.variable_name_interface import VariableNameInterface
        self_instance: VariableNameInterface = \
            self._validate_self_is_variable_name_interface()
        self._initialize_dblclick_handlers_if_not_initialized()
        name: str = get_handler_name(handler=handler)
        self._set_handler_data(
            handler=handler, handlers_dict=self._dblclick_handlers,
            kwargs=kwargs)
        self._append_dblclick_expression(name=name)
        e: MouseEvent = MouseEvent(this=self_instance)
        append_handler_expression(
            handler_data=self._dblclick_handlers[name],
            handler_name=name, e=e)
        return name

    def _append_dblclick_expression(self, name: str) -> None:
        """
        Append double click expression to file.

        Parameters
        ----------
        name : str
            Handler's name.
        """
        from apysc.expression import expression_file_util
        from apysc.type.variable_name_interface import VariableNameInterface
        self_instance: VariableNameInterface = \
            self._validate_self_is_variable_name_interface()
        expression: str = (
            f'{self_instance.variable_name}.dblclick({name});'
        )
        expression_file_util.append_js_expression(expression=expression)

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
        from apysc import EventType
        self._initialize_dblclick_handlers_if_not_initialized()
        self._unbind_event(
            handler=handler, event_type=EventType.DBLCLICK,
            handlers_dict=self._dblclick_handlers)

    def unbind_dblclick_all(self) -> None:
        """
        Unbind all double click events.
        """
        from apysc import EventType
        self._initialize_dblclick_handlers_if_not_initialized()
        self._unbind_all_events(
            event_type=EventType.DBLCLICK,
            handlers_dict=self._dblclick_handlers)
