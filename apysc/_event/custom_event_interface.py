"""Class implementation for the custom event interface.
"""

from typing import Any
from typing import Dict
from typing import Optional
from typing import Union

from apysc._event.custom_event_type import CustomEventType
from apysc._event.event import Event
from apysc._event.handler import Handler
from apysc._event.handler import HandlerData
from apysc._type.blank_object_interface import BlankObjectInterface

_CustomEventType = str
_HandlerName = str


class CustomEventInterface(BlankObjectInterface):

    _custom_event_handlers: Dict[
        _CustomEventType, Dict[_HandlerName, HandlerData]]

    def _initialize_custom_event_handlers_if_not_initialized(
            self, custom_event_type_str: str) -> None:
        """
        Initialize the _custom_event_handlers data if it hasn't been
        initialized yet.

        Parameters
        ----------
        custom_event_type_str : str
            Target custom event type string.
        """
        if not hasattr(self, '_custom_event_handlers'):
            self._custom_event_handlers = {}
        if custom_event_type_str not in self._custom_event_handlers:
            self._custom_event_handlers[custom_event_type_str] = {}

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

    def _set_custom_event_handler_data(
            self, handler: Handler,
            custom_event_type_str: str,
            options: Optional[Dict[str, Any]]) -> None:
        """
        Set a handler's data to the dictionary.

        Parameters
        ----------
        handler : Handler
            Callable would be called when event is dispatched.
        custom_event_type_str : str
            Target custom event type string.
        options : dict or None
            Optional arguments dictionary to be passed to a handler.
        """
        from apysc._event.handler import get_handler_name
        name: str = get_handler_name(handler=handler, instance=self)
        if options is None:
            options = {}
        self._custom_event_handlers[custom_event_type_str][name] = {
            'handler': handler,
            'options': options,
        }

    def bind_custom_event(
            self, custom_event_type: Union[CustomEventType, str],
            handler: Handler,
            e: Event,
            options: Optional[Dict[str, Any]] = None) -> str:
        """
        Add a custom event listener setting.

        Parameters
        ----------
        custom_event_type : CustomEventType or str
            Target custom event type.
        handler : Handler
            A handler would be called when the custom event is triggered.
        e : Event
            Event instance.
        options : dict or None, default None
            Optional arguments dictionary to be passed to a handler.

        Returns
        -------
        name : str
            Handler's name.

        References
        ----------
        - Bind and trigger the custom event document
            - https://bit.ly/3rky7VI
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.bind_custom_event, locals_=locals(),
                module_name=__name__, class_=CustomEventInterface):
            from apysc._event.handler import append_handler_expression
            from apysc._event.handler import get_handler_name
            custom_event_type_str: str = self._get_custom_event_type_str(
                custom_event_type=custom_event_type)
            self._initialize_custom_event_handlers_if_not_initialized(
                custom_event_type_str=custom_event_type_str)
            self._set_custom_event_handler_data(
                handler=handler, custom_event_type_str=custom_event_type_str,
                options=options)
            name: str = get_handler_name(handler=handler, instance=self)
            self._append_custom_event_binding_expression(
                custom_event_type_str=custom_event_type_str, name=name)
            handler_data: HandlerData = self._custom_event_handlers[
                custom_event_type_str][name]
            append_handler_expression(
                handler_data=handler_data, handler_name=name, e=e)
            return name

    def _append_custom_event_binding_expression(
            self, custom_event_type_str: str, name: str) -> None:
        """
        Append a custom event binding expression to the file.

        Parameters
        ----------
        custom_event_type_str : str
            Target custom event type string.
        name : str
            Handler's name.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_custom_event_binding_expression,
                locals_=locals(),
                module_name=__name__, class_=CustomEventInterface):
            blank_object_variable_name: str = self.blank_object_variable_name
            expression: str = (
                f'$({blank_object_variable_name})'
                f'.on("{custom_event_type_str}", {name});'
            )
            ap.append_js_expression(expression=expression)

    def trigger_custom_event(
            self, custom_event_type: Union[CustomEventType, str]) -> None:
        """
        Add a custom event trigger setting.

        Parameters
        ----------
        custom_event_type : CustomEventType or str
            Target custom event type.

        References
        ----------
        - Bind and trigger the custom event document
            - https://bit.ly/3rky7VI
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.trigger_custom_event, locals_=locals(),
                module_name=__name__, class_=CustomEventInterface):
            blank_object_variable_name: str = self.blank_object_variable_name
            custom_event_type_str: str = self._get_custom_event_type_str(
                custom_event_type=custom_event_type)
            expression: str = (
                f'$({blank_object_variable_name})'
                f'.trigger("{custom_event_type_str}");'
            )
            ap.append_js_expression(expression=expression)
