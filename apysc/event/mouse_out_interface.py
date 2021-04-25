"""Class implementation for mouse out interface.
"""

from typing import Any
from typing import Dict
from typing import Optional

from apysc.event.event_interface_base import EventInterfaceBase
from apysc.event.handler import Handler
from apysc.event.handler import HandlerData


class MouseOutInterface(EventInterfaceBase):

    _mouse_out_handlers: Dict[str, HandlerData]

    def mouseout(
            self, handler: Handler,
            options: Optional[Dict[str, Any]]) -> str:
        """
        Add mouse out event listener setting.

        Parameters
        ----------
        handler : Handler
            Callable that called when this instance is mouse outed.
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
        self._initialize_mouse_out_handlers_if_not_initialized()
        name: str = get_handler_name(handler=handler)
        self._set_handler_data(
            handler=handler, handlers_dict=self._mouse_out_handlers,
            options=options)
        self._append_mouse_out_expression(name=name)
        return name

    def _append_mouse_out_expression(self, name: str) -> None:
        """
        Append mouse out expression to file.

        Parameters
        ----------
        name : str
            Handler's name.
        """
        from apysc.expression import expression_file_util
        from apysc.type.variable_name_interface import VariableNameInterface
        self_instance: VariableNameInterface = \
            self._validate_self_is_variable_name_interface()
        pass

    def _initialize_mouse_out_handlers_if_not_initialized(self) -> None:
        """
        Initialize _mouse_out_handlers attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_mouse_out_handlers'):
            return
        self._mouse_out_handlers = {}
