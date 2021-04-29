"""Implementation of mouse wheel event interfaces.

Notes
-----
Not supported each SVG elements' mouse wheel event currently, only
supported document (overall screen) mouse wheel.
"""

from typing import Any, Dict, Optional
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
    from apysc.event.handler import get_handler_name
    from apysc.expression import expression_file_util
    from apysc.event.handler import HandlerData
    from apysc.event.handler import append_handler_expression
    name: str = get_handler_name(handler=handler)
    expression: str = (
        f'$(document).on("mousewheel", {name});'
    )
    expression_file_util.append_js_expression(expression=expression)

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
    from apysc.event.handler import get_handler_name
    from apysc.expression import expression_file_util
    name: str = get_handler_name(handler=handler)
    expression: str = (
        f'$(document).off("mousewheel", {name});'
    )
    expression_file_util.append_js_expression(expression=expression)


def unbind_wheel_event_all_from_document() -> None:
    """
    Unbind all wheel event from document (overall window).
    """
    from apysc.expression import expression_file_util
    expression: str = (
        '$(document).off("mousewheel");'
    )
    expression_file_util.append_js_expression(expression=expression)
