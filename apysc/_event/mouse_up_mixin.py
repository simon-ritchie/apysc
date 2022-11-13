"""Class implementation for the mouse up mix-in.
"""

from typing import Callable
from typing import Dict
from typing import Optional
from typing import TypeVar

from typing_extensions import final

from apysc._event.handler import HandlerData
from apysc._event.mouse_event import MouseEvent
from apysc._event.mouse_event_binding_expression_mixin import (
    MouseEventBindingExpressionMixin,
)
from apysc._event.mouse_event_unbinding_mixin import MouseEventUnbindingMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos

_O = TypeVar("_O")
_Handler = Callable[[MouseEvent, _O], None]


class MouseUpMixIn(MouseEventUnbindingMixIn, MouseEventBindingExpressionMixin):

    _mouse_up_handlers: Dict[str, HandlerData[MouseEvent]]

    @final
    @arg_validation_decos.handler_args_num(arg_position_index=1)
    @arg_validation_decos.handler_options_type(arg_position_index=2)
    @add_debug_info_setting(module_name=__name__)
    def mouseup(self, handler: _Handler[_O], *, options: Optional[_O] = None) -> str:
        """
        Add mouse up event listener setting.

        Parameters
        ----------
        handler : _Handler
            Callable that would be called when mouse-up on this instance.
        options : dict or None, default None
            Optional arguments dictionary to be passed to a handler.

        Returns
        -------
        name : str
            Handler's name.

        References
        ----------
        - Mousedown and mouseup interfaces
            - https://simon-ritchie.github.io/apysc/en/mousedown_and_mouseup.html  # noqa
        - About the handler options' type
            - https://simon-ritchie.github.io/apysc/en/about_handler_options_type.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> def on_mouseup(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     rectangle: ap.Rectangle = e.this
        ...     rectangle.fill_color = ap.String("#f0a")
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> _ = rectangle.mouseup(on_mouseup)
        """
        import apysc as ap
        from apysc._event.handler import append_handler_expression
        from apysc._event.handler import get_handler_name
        from apysc._type.variable_name_mixin import VariableNameMixIn
        from apysc._validation.variable_name_validation import (
            validate_variable_name_interface_type,
        )

        self_instance: VariableNameMixIn = validate_variable_name_interface_type(
            instance=self
        )
        self._initialize_mouse_up_handlers_if_not_initialized()
        name: str = get_handler_name(handler=handler, instance=self)
        self._set_handler_data(
            handler=handler, handlers_dict=self._mouse_up_handlers, options=options
        )
        self._append_mouse_event_binding_expression(
            name=name, mouse_event_type=ap.MouseEventType.MOUSEUP
        )
        e: ap.MouseEvent = ap.MouseEvent(this=self_instance)
        append_handler_expression(
            handler_data=self._mouse_up_handlers[name], handler_name=name, e=e
        )
        return name

    @final
    def _initialize_mouse_up_handlers_if_not_initialized(self) -> None:
        """
        Initialize _mouse_up_handlers attribute if this instance
        does not initialize it yet.
        """
        if hasattr(self, "_mouse_up_handlers"):
            return
        self._mouse_up_handlers = {}

    @final
    @arg_validation_decos.handler_args_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def unbind_mouseup(self, handler: _Handler[_O]) -> None:
        """
        Unbind a specified handler's mouse-up event.

        Parameters
        ----------
        handler : _Handler
            Unbinding target Callable.

        References
        ----------
        - Mousedown and mouseup interfaces
            - https://simon-ritchie.github.io/apysc/en/mousedown_and_mouseup.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> def on_mouseup(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     rectangle: ap.Rectangle = e.this
        ...     rectangle.fill_color = ap.String("#f0a")
        ...     rectangle.unbind_mouseup(on_mouseup)
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> _ = rectangle.mouseup(on_mouseup)
        """
        import apysc as ap

        self._initialize_mouse_up_handlers_if_not_initialized()
        self._unbind_mouse_event(
            handler=handler,
            mouse_event_type=ap.MouseEventType.MOUSEUP,
            handlers_dict=self._mouse_up_handlers,
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def unbind_mouseup_all(self) -> None:
        """
        Unbind all mouse up events.

        References
        ----------
        - Mousedown and mouseup interfaces
            - https://simon-ritchie.github.io/apysc/en/mousedown_and_mouseup.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> def on_mouseup(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     rectangle: ap.Rectangle = e.this
        ...     rectangle.fill_color = ap.String("#f0a")
        ...     rectangle.unbind_mouseup_all()
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> _ = rectangle.mouseup(on_mouseup)
        """
        import apysc as ap

        self._initialize_mouse_up_handlers_if_not_initialized()
        self._unbind_all_mouse_events(
            mouse_event_type=ap.MouseEventType.MOUSEUP,
            handlers_dict=self._mouse_up_handlers,
        )
