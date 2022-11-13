"""Class implementation for click mix-in.
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


class ClickMixIn(MouseEventUnbindingMixIn, MouseEventBindingExpressionMixin):

    _click_handlers: Dict[str, HandlerData[MouseEvent]]

    @final
    @arg_validation_decos.handler_args_num(arg_position_index=1)
    @arg_validation_decos.handler_options_type(arg_position_index=2)
    @add_debug_info_setting(module_name=__name__)
    def click(self, handler: _Handler[_O], *, options: Optional[_O] = None) -> str:
        """
        Add a click event listener setting.

        Parameters
        ----------
        handler : _Handler
            A callable would be called when clicking this instance.
        options : dict or None, default None
            Optional arguments dictionary to be passed to a handler.

        Returns
        -------
        name : str
            Handler's name.

        References
        ----------
        - Click interface
            - https://simon-ritchie.github.io/apysc/en/click.html
        - About the handler options' type
            - https://simon-ritchie.github.io/apysc/en/about_handler_options_type.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     rectangle: ap.Rectangle = e.this
        ...     rectangle.x += 10
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> _ = rectangle.click(on_click)
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
        self._initialize_click_handlers_if_not_initialized()
        name: str = get_handler_name(handler=handler, instance=self)
        self._set_handler_data(
            handler=handler, handlers_dict=self._click_handlers, options=options
        )
        self._append_mouse_event_binding_expression(
            name=name, mouse_event_type=ap.MouseEventType.CLICK
        )
        e: ap.MouseEvent = ap.MouseEvent(this=self_instance)
        append_handler_expression(
            handler_data=self._click_handlers[name], handler_name=name, e=e
        )
        return name

    @final
    def _initialize_click_handlers_if_not_initialized(self) -> None:
        """
        Initialize the _click_handlers attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, "_click_handlers"):
            return
        self._click_handlers = {}

    @final
    @arg_validation_decos.handler_args_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def unbind_click(self, handler: _Handler[_O]) -> None:
        """
        Unbind specified handler's click event.

        Parameters
        ----------
        handler : _Handler
            Unbinding target Callable.

        References
        ----------
        - Click interface
            - https://simon-ritchie.github.io/apysc/en/click.html

        Examples
        --------
        >>> import apysc as ap
        >>> def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     rectangle: ap.Rectangle = e.this
        ...     rectangle.fill_color = ap.String("#f0a")
        ...     rectangle.unbind_click(on_click)
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> _ = rectangle.click(on_click)
        """
        import apysc as ap

        self._initialize_click_handlers_if_not_initialized()
        self._unbind_mouse_event(
            handler=handler,
            mouse_event_type=ap.MouseEventType.CLICK,
            handlers_dict=self._click_handlers,
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def unbind_click_all(self) -> None:
        """
        Unbind all click events.

        References
        ----------
        - Click interface
            - https://simon-ritchie.github.io/apysc/en/click.html

        Examples
        --------
        >>> import apysc as ap
        >>> def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     rectangle: ap.Rectangle = e.this
        ...     rectangle.fill_color = ap.String("#f0a")
        ...     rectangle.unbind_click_all()
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> _ = rectangle.click(on_click)
        """
        import apysc as ap

        self._initialize_click_handlers_if_not_initialized()
        self._unbind_all_mouse_events(
            mouse_event_type=ap.MouseEventType.CLICK, handlers_dict=self._click_handlers
        )
