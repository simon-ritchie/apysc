"""Implementation of mouse wheel event interfaces.

Notes
-----
Not supported each SVG elements' mouse wheel event currently, only
supported document (overall screen) mouse wheel.
"""

from typing import Any
from typing import Dict
from typing import Optional

from typing_extensions import Protocol

import apysc as ap


class WheelHandler(Protocol):

    def __call__(self, e: ap.WheelEvent, options: Dict[str, Any]) -> None:
        """
        Wheel event handler's callable interface.

        Parameters
        ----------
        e : WheelEvent
            Created wheel event instance.
        options : dict
            Optional arguments dictionary to pass to.
        """


def bind_wheel_event_to_document(
        handler: WheelHandler,
        options: Optional[Dict[str, Any]] = None) -> str:
    """
    Bind wheel event to document (overall window).

    Parameters
    ----------
    handler : WheelHandler
        Callable that handle wheel event.
    options : dict or None, default None
        Optional arguments dictionary to pass to.

    Returns
    -------
    name : str
        Handler's name.
    """
    with ap.DebugInfo(
            callable_=bind_wheel_event_to_document, locals_=locals(),
            module_name=__name__):
        from apysc._event.handler import HandlerData
        from apysc._event.handler import append_handler_expression
        from apysc._event.handler import get_handler_name
        name: str = get_handler_name(handler=handler, instance=ap.document)
        expression: str = (
            f'$({ap.document.variable_name}).on("mousewheel", {name});'
        )
        ap.append_js_expression(expression=expression)

        if options is None:
            options = {}
        handler_data: HandlerData = {  # type: ignore
            'handler': handler,
            'options': options,
        }
        e: ap.WheelEvent = ap.WheelEvent()
        append_handler_expression(
            handler_data=handler_data, handler_name=name, e=e)
        return name


def unbind_wheel_event_from_document(handler: WheelHandler) -> None:
    """
    Unbind specified handler's wheel event from document (overall window).

    Parameters
    ----------
    handler : WheelHandler
        Callable to unbind.
    """
    with ap.DebugInfo(
            callable_=unbind_wheel_event_from_document, locals_=locals(),
            module_name=__name__):
        from apysc._event.handler import get_handler_name
        name: str = get_handler_name(handler=handler, instance=ap.document)
        expression: str = (
            f'$({ap.document.variable_name}).off("mousewheel", {name});'
        )
        ap.append_js_expression(expression=expression)


def unbind_wheel_event_all_from_document() -> None:
    """
    Unbind all wheel event from document (overall window).
    """
    with ap.DebugInfo(
            callable_=unbind_wheel_event_all_from_document, locals_=locals(),
            module_name=__name__):
        expression: str = (
            f'$({ap.document.variable_name}).off("mousewheel");'
        )
        ap.append_js_expression(expression=expression)
