"""Class implementation for the custom event mix-in.
"""

from typing import Any
from typing import Callable
from typing import Dict
from typing import Generic
from typing import Optional
from typing import TypeVar
from typing import Union

from typing_extensions import final

from apysc._event.custom_event_type import CustomEventType
from apysc._event.event import Event
from apysc._event.handler import HandlerData
from apysc._event.set_handler_data_mixin import SetHandlerDataMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.blank_object_mixin import BlankObjectMixIn
from apysc._validation import arg_validation_decos

_CustomEventType = str
_HandlerName = str
_Handler = Callable[[Any, Any], None]
_EventType = TypeVar("_EventType", bound=Event)


class CustomEventMixIn(
    BlankObjectMixIn,
    SetHandlerDataMixIn[_EventType],
    Generic[_EventType],
):

    _custom_event_handlers: Dict[
        _CustomEventType, Dict[_HandlerName, HandlerData[_EventType]]
    ]

    @final
    def _initialize_custom_event_handlers_if_not_initialized(
        self, *, custom_event_type_str: str
    ) -> None:
        """
        Initialize the _custom_event_handlers data if this instance
        does not initialize it yet.

        Parameters
        ----------
        custom_event_type_str : str
            Target custom event type string.
        """
        if not hasattr(self, "_custom_event_handlers"):
            self._custom_event_handlers = {}
        if custom_event_type_str not in self._custom_event_handlers:
            self._custom_event_handlers[custom_event_type_str] = {}

    @final
    def _get_custom_event_type_str(
        self, *, custom_event_type: Union[CustomEventType, str]
    ) -> str:
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

    @final
    def _unset_custom_event_handler_data(
        self, *, handler: _Handler, custom_event_type_str: str
    ) -> None:
        """
        Unset a handler's data from the dictionary.

        Parameters
        ----------
        handler : _Handler
            Callable that this instance calls when its
            event's dispatching.
        custom_event_type_str : str
            A target custom event type's string.
        """
        from apysc._event.handler import get_handler_name

        if custom_event_type_str not in self._custom_event_handlers:
            return
        name: str = get_handler_name(handler=handler, instance=self)
        if name not in self._custom_event_handlers[custom_event_type_str]:
            return
        del self._custom_event_handlers[custom_event_type_str][name]

    @final
    @arg_validation_decos.handler_args_num(arg_position_index=2)
    @arg_validation_decos.is_event(arg_position_index=3)
    @arg_validation_decos.handler_options_type(arg_position_index=4)
    @arg_validation_decos.is_builtin_string(arg_position_index=5, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def bind_custom_event(
        self,
        *,
        custom_event_type: Union[CustomEventType, str],
        handler: _Handler,
        e: Event,
        options: Optional[Any] = None,
        in_handler_head_expression: str = "",
    ) -> str:
        """
        Add a custom event listener setting.

        Parameters
        ----------
        custom_event_type : CustomEventType or str
            Target custom event type.
        handler : _Handler
            Callable that this instance calls when its
            event's dispatching.
        e : Event
            Event instance.
        options : dict or None, default None
            Optional arguments dictionary to be passed to a handler.
        in_handler_head_expression : str, default ''
            Optional expression to be added at the handler function's
            head position.

        Returns
        -------
        name : str
            Handler's name.

        References
        ----------
        - Bind and trigger the custom event
            - https://simon-ritchie.github.io/apysc/en/bind_and_trigger_custom_event.html  # noqa
        - About the handler options' type
            - https://simon-ritchie.github.io/apysc/en/about_handler_options_type.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> def on_custom_event(e: ap.Event[ap.Rectangle], options: dict) -> None:
        ...     rectangle: ap.Rectangle = e.this
        ...     rectangle.fill_color = ap.String("#f0a")
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> e: ap.Event = ap.Event(this=rectangle)
        >>> _ = rectangle.bind_custom_event(
        ...     custom_event_type="my_custom_event", handler=on_custom_event, e=e
        ... )
        >>> # Do something here and then trigger the custom event
        >>> rectangle.trigger_custom_event(custom_event_type="my_custom_event")
        """
        from apysc._event.handler import append_handler_expression
        from apysc._event.handler import get_handler_name

        custom_event_type_str: str = self._get_custom_event_type_str(
            custom_event_type=custom_event_type
        )
        self._initialize_custom_event_handlers_if_not_initialized(
            custom_event_type_str=custom_event_type_str
        )
        self._set_handler_data(
            handler=handler,
            handlers_dict=self._custom_event_handlers[custom_event_type_str],
            options=options,
        )
        name: str = get_handler_name(handler=handler, instance=self)
        self._append_custom_event_binding_expression(
            custom_event_type_str=custom_event_type_str, name=name
        )
        handler_data: HandlerData = self._custom_event_handlers[custom_event_type_str][
            name
        ]
        append_handler_expression(
            handler_data=handler_data,
            handler_name=name,
            e=e,
            in_handler_head_expression=in_handler_head_expression,
        )
        return name

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_custom_event_binding_expression(
        self, *, custom_event_type_str: str, name: str
    ) -> None:
        """
        Append a custom event binding expression.

        Parameters
        ----------
        custom_event_type_str : str
            Target custom event type string.
        name : str
            Handler's name.
        """
        import apysc as ap

        blank_object_variable_name: str = self.blank_object_variable_name
        expression: str = (
            f"$({blank_object_variable_name})"
            f'.off("{custom_event_type_str}", {name});'
            f"\n$({blank_object_variable_name})"
            f'.on("{custom_event_type_str}", {name});'
        )
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def trigger_custom_event(
        self, *, custom_event_type: Union[CustomEventType, str]
    ) -> None:
        """
        Add a custom event trigger setting.

        Parameters
        ----------
        custom_event_type : CustomEventType or str
            Target custom event type.

        References
        ----------
        - Bind and trigger the custom event
            - https://simon-ritchie.github.io/apysc/en/bind_and_trigger_custom_event.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> def on_custom_event(e: ap.Event[ap.Rectangle], options: dict) -> None:
        ...     rectangle: ap.Rectangle = e.this
        ...     rectangle.fill_color = ap.String("#f0a")
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> e: ap.Event = ap.Event(this=rectangle)
        >>> _ = rectangle.bind_custom_event(
        ...     custom_event_type="my_custom_event", handler=on_custom_event, e=e
        ... )
        >>> # Do something here and then trigger the custom event
        >>> rectangle.trigger_custom_event(custom_event_type="my_custom_event")
        """
        import apysc as ap

        blank_object_variable_name: str = self.blank_object_variable_name
        custom_event_type_str: str = self._get_custom_event_type_str(
            custom_event_type=custom_event_type
        )
        expression: str = (
            f"$({blank_object_variable_name})" f'.trigger("{custom_event_type_str}");'
        )
        ap.append_js_expression(expression=expression)

    @final
    @arg_validation_decos.handler_args_num(arg_position_index=2)
    @add_debug_info_setting(module_name=__name__)
    def unbind_custom_event(
        self, *, custom_event_type: Union[CustomEventType, str], handler: _Handler
    ) -> str:
        """
        Unbind (remove) a custom event listener setting.

        Parameters
        ----------
        custom_event_type : CustomEventType or str
            Target custom event type.
        handler : _Handler
            A handler for when the custom event is triggered.

        Returns
        -------
        name : str
            Handler's name.

        Examples
        --------
        >>> import apysc as ap
        >>> def on_custom_event(e: ap.Event[ap.Rectangle], options: dict) -> None:
        ...     rectangle: ap.Rectangle = e.this
        ...     rectangle.fill_color = ap.String("#f0a")
        ...     rectangle.unbind_custom_event(
        ...         custom_event_type="my_custom_event", handler=on_custom_event
        ...     )
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> e: ap.Event = ap.Event(this=rectangle)
        >>> _ = rectangle.bind_custom_event(
        ...     custom_event_type="my_custom_event", handler=on_custom_event, e=e
        ... )
        >>> # Do something here and then trigger the custom event
        >>> rectangle.trigger_custom_event(custom_event_type="my_custom_event")
        """
        from apysc._event.handler import get_handler_name

        custom_event_type_str: str = self._get_custom_event_type_str(
            custom_event_type=custom_event_type
        )
        self._initialize_custom_event_handlers_if_not_initialized(
            custom_event_type_str=custom_event_type_str
        )
        self._unset_custom_event_handler_data(
            handler=handler, custom_event_type_str=custom_event_type_str
        )
        name: str = get_handler_name(handler=handler, instance=self)
        self._append_custom_event_unbinding_expression(
            custom_event_type_str=custom_event_type_str, name=name
        )
        return name

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_custom_event_unbinding_expression(
        self, *, custom_event_type_str: str, name: str
    ) -> None:
        """
        Add a custom event unbinding expression.

        Parameters
        ----------
        custom_event_type_str : str
            Target custom event type string.
        name : str
            Handler's name.
        """
        import apysc as ap

        expression: str = (
            f"$({self.blank_object_variable_name})"
            f'.off("{custom_event_type_str}", {name});'
        )
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def unbind_custom_event_all(
        self, *, custom_event_type: Union[CustomEventType, str]
    ) -> None:
        """
        Unbind (remove) custom event listener settings.

        Parameters
        ----------
        custom_event_type : CustomEventType or str
            Target custom event type.

        Examples
        --------
        >>> import apysc as ap
        >>> def on_custom_event(e: ap.Event[ap.Rectangle], options: dict) -> None:
        ...     rectangle: ap.Rectangle = e.this
        ...     rectangle.fill_color = ap.String("#f0a")
        ...     rectangle.unbind_custom_event_all(custom_event_type="my_custom_event")
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> e: ap.Event = ap.Event(this=rectangle)
        >>> _ = rectangle.bind_custom_event(
        ...     custom_event_type="my_custom_event", handler=on_custom_event, e=e
        ... )
        >>> # Do something here and then trigger the custom event
        >>> rectangle.trigger_custom_event(custom_event_type="my_custom_event")
        """
        import apysc as ap

        custom_event_type_str: str = self._get_custom_event_type_str(
            custom_event_type=custom_event_type
        )
        self._initialize_custom_event_handlers_if_not_initialized(
            custom_event_type_str=custom_event_type_str
        )
        self._custom_event_handlers[custom_event_type_str] = {}
        expression: str = (
            f"$({self.blank_object_variable_name})" f'.off("{custom_event_type_str}");'
        )
        ap.append_js_expression(expression=expression)
