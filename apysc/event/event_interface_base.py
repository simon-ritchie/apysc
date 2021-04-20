"""Class implementation for each event interfaces' base class.
"""

from typing import Any, Dict, Optional
from typing_extensions import Final

from apysc.type.variable_name_interface import VariableNameInterface
from apysc.event.handler import Handler
from apysc.event.handler import HandlerData


class EventInterfaceBase:

    VARIABLE_NAME_INTERFACE_TYPE_ERR_MSG: Final[str] = (
        'This interface can only be used that inheriting '
        'VariableNameInterface.'
    )

    def validate_self_is_variable_name_interface(
            self) -> VariableNameInterface:
        """
        Validate whether this instance is a VariableNameInterface
        instance or not.

        Returns
        -------
        self_instance : VariableNameInterface
            This instance.

        Raises
        ------
        TypeError
            If this instance is not a VariableNameInterface.
        """
        if not isinstance(self, VariableNameInterface):
            raise TypeError(self.VARIABLE_NAME_INTERFACE_TYPE_ERR_MSG)
        return self

    def _set_handler_data(
            self, handler: Handler,
            handlers_dict: Dict[str, HandlerData],
            kwargs: Optional[Dict[str, Any]]) -> None:
        """
        Set handler's data to the given dictionary.

        Parameters
        ----------
        handler : Handler
            Callable that called when this instance is clicked.
        handlers_dict : dict
            Dictionary to be set handler's data.
        kwargs : dict or None, default None
            Keyword arguments to be passed to handler's callable.
        """
        from apysc.event.handler import get_handler_name
        name: str = get_handler_name(handler=handler)
        if kwargs is None:
            kwargs = {}
        handlers_dict[name] = {
            'handler': handler,
            'kwargs': kwargs,
        }
