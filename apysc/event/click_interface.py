"""Class implementation for click interface.
"""

from typing import Any, Dict, List, Optional

from apysc.event.handler import Handler, HandlerData
from apysc.event.handler import get_handler_name


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
        self._initialize_click_handlers_if_not_initialized()
        if kwargs is None:
            kwargs = {}
        name: str = get_handler_name(handler=handler)

        self._click_handlers[name] = {
            'handler': handler,
            'kwargs': kwargs,
        }
        self._append_click_expression(name=name)
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
        from apysc.type.variable_name_interface import VariableNameInterface
        from apysc.expression import expression_file_util
        if not isinstance(self, VariableNameInterface):
            raise TypeError(
                'This interface can only be used that inheriting '
                'VariableNameInterface.')
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
