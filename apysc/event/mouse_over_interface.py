"""Class implementation for mouse over interface.
"""

from typing import Any
from typing import Dict
from typing import Optional

from apysc.event.event_interface_base import EventInterfaceBase
from apysc.event.handler import Handler
from apysc.event.handler import HandlerData


class MouseOverInterface(EventInterfaceBase):

    _mouse_over_handlers: Dict[str, HandlerData]

    def mouseover(
            self, handler: Handler,
            options: Optional[Dict[str, Any]]) -> str:
        """
        Add mouse over event listener setting.

        Parameters
        ----------
        handler : Handler
            Callable that called when this instance is mouse overed.
        options : dict or None, default None
            Optional arguments dictionary to be passed to handler.

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
        self._initialize_mouse_over_handlers_if_not_initialized()

    def _initialize_mouse_over_handlers_if_not_initialized(self) -> None:
        """
        Initialize _mouse_over_handlers attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_mouse_over_handlers'):
            return
        self._mouse_over_handlers = {}
