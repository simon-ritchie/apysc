"""Class implementation for click interface.
"""

from typing import Any, Callable, Dict, List, Optional
import hashlib

from apysc.type.variable_name_interface import VariableNameInterface
from apysc.event.handler import Handler, HandlerData
from apysc import Boolean


class ClickInterface:

    _click_handlers: Dict[str, HandlerData]

    def click(
            self, handler: Handler,
            name: Optional[str] = None,
            kwargs: Optional[Dict[str, Any]] = None) -> str:
        """
        Add click event listener setting.

        Parameters
        ----------
        handler : Handler
            Callable that called when this instance is clicked.
        name : str or None, default None
            Handler's name. This will be necessary when unbinding
            event separately.
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
        if name is None:
            name = str(handler)
        self._click_handlers[name] = {
            'handler': handler,
            'kwargs': kwargs,
        }
        return name

    def _initialize_click_handlers_if_not_initialized(self) -> None:
        """
        Initialize _click_handlers attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_click_handlers'):
            return
        self._click_handlers = {}
