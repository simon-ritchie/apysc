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

from apysc import WheelEvent


class WheelHandler(Protocol):

    def __call__(self, e: WheelEvent, options: Dict[str, Any]) -> None:
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
    from apysc import append_js_expression
    from apysc import document
    from apysc._event.handler import HandlerData
    from apysc._event.handler import append_handler_expression
    from apysc._event.handler import get_handler_name
    name: str = get_handler_name(handler=handler, instance=document)
    expression: str = (
        f'$({document.variable_name}).on("mousewheel", {name});'
    )
    append_js_expression(expression=expression)

    if options is None:
        options = {}
    handler_data: HandlerData = {  # type: ignore
        'handler': handler,
        'options': options,
    }
    e: WheelEvent = WheelEvent()
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
    from apysc import append_js_expression
    from apysc import document
    from apysc._event.handler import get_handler_name
    name: str = get_handler_name(handler=handler, instance=document)
    expression: str = (
        f'$({document.variable_name}).off("mousewheel", {name});'
    )
    append_js_expression(expression=expression)


def unbind_wheel_event_all_from_document() -> None:
    """
    Unbind all wheel event from document (overall window).
    """
    from apysc import append_js_expression
    from apysc import document
    expression: str = (
        f'$({document.variable_name}).off("mousewheel");'
    )
    append_js_expression(expression=expression)
