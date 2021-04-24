"""Class implementation for mouse down interface.
"""

from typing import Any
from typing import Dict
from typing import Optional

from apysc.event.event_interface_base import EventInterfaceBase
from apysc.event.handler import Handler
from apysc.event.handler import HandlerData


class MouseDownInterface(EventInterfaceBase):

    _mouse_down_handlers: Dict[str, HandlerData]

    def mousedown(
            self, handler: Handler,
            kwargs: Optional[Dict[str, Any]] = None) -> str:
        """
        Add mouse down event listener setting.

        Parameters
        ----------
        handler : Handler
            Callable that called when this instance is mouse downed.

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
        self._initialize_mouse_down_handlers_if_not_initialized()
        pass

    def _initialize_mouse_down_handlers_if_not_initialized(self) -> None:
        """
        Initialize _mouse_down_handlers attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_mouse_down_handlers'):
            return
        self._mouse_down_handlers = {}
