"""Class implementation for the custom event interface.
"""

from typing import Any, Union
from typing import Dict
from typing import Optional

from apysc._event.handler import Handler
from apysc._event.handler import HandlerData
from apysc._type.variable_name_interface import VariableNameInterface
from apysc._event.custom_event_type import CustomEventType

_CustomEventType = str
_HandlerName = str


class CustomEventInterface:

    _custom_event_handlers: Dict[
        _CustomEventType, Dict[_HandlerName, HandlerData]]

    def _initialize_custom_event_handlers_if_not_initialized(
            self) -> None:
        """
        Initialize the _custom_event_handlers data if it hasn't been
        initialized yet.

        Parameters
        ----------
        """

    def _get_custom_event_type_str(
            self,
            custom_event_type: Union[CustomEventType, str]) -> str:
        """
        Get a custom event type string from a type value.

        Parameters
        ----------
        custom_event_type : CustomEventType or str
            Target custom event type or string.

        Returns
        -------
        custom_event_type_str : str
            A custom event type string.
        """
        if isinstance(custom_event_type, str):
            return custom_event_type
        custom_event_type_str: str = custom_event_type.value
        return custom_event_type_str

    def bind_custom_event(
            self, custom_event_type: Union[CustomEventType, str],
            handler: Handler,
            options: Optional[Dict[str, Any]]) -> None:
        """
        Add a custom event listener setting.

        Parameters
        ----------
        custom_event_type : CustomEventType or str
            Target custom event type.
        handler : Handler
            A handler would be called when the custom event is triggered.
        options : dict or None, default None
            Optional arguments dictionary to be passed to a handler.

        Returns
        -------
        name : str
            Handler's name.
        """
        from apysc._validation import variable_name_validation
        self_instance: VariableNameInterface = variable_name_validation.\
            validate_variable_name_interface_type(instance=self)
        custom_event_type_str: str = self._get_custom_event_type_str(
            custom_event_type=custom_event_type)
        pass
