"""Class implementation for click interface.
"""

from typing import Any
from typing import Dict
from typing import Optional

from apysc.event.handler import Handler
from apysc.event.handler import HandlerData

_VARIABLE_NAME_INTERFACE_TYPE_ERR_MSG: str = (
    'This interface can only be used that inheriting '
    'VariableNameInterface.'
)


class ClickInterface:

    _click_handlers: Dict[str, HandlerData]

    def click(
            self, handler: Handler,
            kwargs: Optional[Dict[str, Any]] = None) -> str:
        """
        Add click event listener setting.

        Parameters
        ----------
        handler : Handler
            Callable that called when this instance is clicked.
        kwargs : dict or None, default None
            Keyword arguments to be passed to handler's callable.

        Returns
        -------
        name : str
            Handler's name.
        """
        from apysc import Event
        from apysc.event.handler import append_handler_expression
        from apysc.event.handler import get_handler_name
        from apysc.type.variable_name_interface import VariableNameInterface
        if not isinstance(self, VariableNameInterface):
            raise TypeError(_VARIABLE_NAME_INTERFACE_TYPE_ERR_MSG)
        self._initialize_click_handlers_if_not_initialized()
        if kwargs is None:
            kwargs = {}
        name: str = get_handler_name(handler=handler)

        self._click_handlers[name] = {
            'handler': handler,
            'kwargs': kwargs,
        }
        self._append_click_expression(name=name)
        e: Event = Event(this=self)
        append_handler_expression(
            handler_data=self._click_handlers[name],
            handler_name=name,
            e=e)
        return name

    def _append_click_expression(self, name: str) -> None:
        """
        Append click expression to file.

        Parameters
        ----------
        name : str
            Handler's name.

        Raises
        ------
        ValueError
            If this instance is not subclass of VariableNameInterface.
        """
        from apysc.expression import expression_file_util
        from apysc.type.variable_name_interface import VariableNameInterface
        if not isinstance(self, VariableNameInterface):
            raise TypeError(_VARIABLE_NAME_INTERFACE_TYPE_ERR_MSG)
        expression: str = (
            f'{self.variable_name}.click({name});'
        )
        expression_file_util.append_js_expression(expression=expression)

    def _initialize_click_handlers_if_not_initialized(self) -> None:
        """
        Initialize _click_handlers attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_click_handlers'):
            return
        self._click_handlers = {}
