"""Class implementation for mouse out interface.
"""

from typing import Callable
from typing import Dict
from typing import Optional
from typing import TypeVar

from apysc._event.handler import HandlerData
from apysc._event.mouse_event import MouseEvent
from apysc._event.mouse_event_interface_base import MouseEventInterfaceBase

_O = TypeVar('_O')
_Handler = Callable[[MouseEvent, _O], None]


class MouseOutInterface(MouseEventInterfaceBase):

    _mouse_out_handlers: Dict[str, HandlerData]

    def mouseout(
            self, handler: _Handler[_O], *,
            options: Optional[_O] = None) -> str:
        """
        Add mouse out event listener setting.

        Parameters
        ----------
        handler : _Handler
            Callable that called when mouse is outed on this instance.
        options : dict or None, default None
            Optional arguments dictionary to be passed to handler.

        Returns
        -------
        name : str
            Handler's name.

        References
        ----------
        - Mouseover and mouseout interfaces
            - https://bit.ly/3hOtaBl
        - About the handler options’ type document
            - https://bit.ly/39tnYxC

        Examples
        --------
        >>> import apysc as ap
        >>> def on_mouseout(
        ...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     rectangle: ap.Rectangle = e.this
        ...     rectangle.fill_color = ap.String('#f0a')
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> _ = rectangle.mouseout(on_mouseout)
        """
        import apysc as ap
        from apysc._validation.variable_name_validation import \
            validate_variable_name_interface_type
        with ap.DebugInfo(
                callable_=self.mouseout, locals_=locals(),
                module_name=__name__, class_=MouseOutInterface):
            from apysc._event.handler import append_handler_expression
            from apysc._event.handler import get_handler_name
            from apysc._type.variable_name_interface import \
                VariableNameInterface
            from apysc._validation.handler_options_validation import \
                validate_options_type
            self_instance: VariableNameInterface = \
                validate_variable_name_interface_type(instance=self)
            validate_options_type(options=options)
            self._initialize_mouse_out_handlers_if_not_initialized()
            name: str = get_handler_name(handler=handler, instance=self)
            self._set_mouse_event_handler_data(
                handler=handler, handlers_dict=self._mouse_out_handlers,
                options=options)
            self._append_mouse_event_binding_expression(
                name=name, mouse_event_type=ap.MouseEventType.MOUSEOUT)
            e: ap.MouseEvent = ap.MouseEvent(this=self_instance)
            append_handler_expression(
                handler_data=self._mouse_out_handlers[name],
                handler_name=name, e=e)
            return name

    def _initialize_mouse_out_handlers_if_not_initialized(self) -> None:
        """
        Initialize _mouse_out_handlers attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_mouse_out_handlers'):
            return
        self._mouse_out_handlers = {}

    def unbind_mouseout(self, handler: _Handler[_O]) -> None:
        """
        Unbind specified handler's mouse out event.

        Parameters
        ----------
        handler : _Handler
            Callable to be unbinded.

        References
        ----------
        - Mouseover and mouseout interfaces
            - https://bit.ly/3hOtaBl

        Examples
        --------
        >>> import apysc as ap
        >>> def on_mouseout(
        ...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     rectangle: ap.Rectangle = e.this
        ...     rectangle.fill_color = ap.String('#f0a')
        ...     rectangle.unbind_mouseout(on_mouseout)
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> _ = rectangle.mouseout(on_mouseout)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.unbind_mouseout, locals_=locals(),
                module_name=__name__, class_=MouseOutInterface):
            self._initialize_mouse_out_handlers_if_not_initialized()
            self._unbind_mouse_event(
                handler=handler, mouse_event_type=ap.MouseEventType.MOUSEOUT,
                handlers_dict=self._mouse_out_handlers)

    def unbind_mouseout_all(self) -> None:
        """
        Unbind all mouse out events.

        References
        ----------
        - Mouseover and mouseout interfaces
            - https://bit.ly/3hOtaBl

        Examples
        --------
        >>> import apysc as ap
        >>> def on_mouseout(
        ...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     rectangle: ap.Rectangle = e.this
        ...     rectangle.fill_color = ap.String('#f0a')
        ...     rectangle.unbind_mouseout_all()
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> _ = rectangle.mouseout(on_mouseout)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.unbind_mouseout_all, locals_=locals(),
                module_name=__name__, class_=MouseOutInterface):
            self._initialize_mouse_out_handlers_if_not_initialized()
            self._unbind_all_mouse_events(
                mouse_event_type=ap.MouseEventType.MOUSEOUT,
                handlers_dict=self._mouse_out_handlers)
