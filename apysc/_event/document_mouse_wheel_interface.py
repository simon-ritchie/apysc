"""Implementation of mouse wheel event interfaces.

Notes
-----
Not supported each SVG elements' mouse wheel event currently, only
supported document (overall screen) mouse wheel.
"""

from typing import Callable
from typing import Optional
from typing import TypeVar

import apysc as ap

_O = TypeVar('_O')
_Handler = Callable[[ap.WheelEvent, _O], None]


def bind_wheel_event_to_document(
        handler: _Handler[_O],
        options: Optional[_O] = None) -> str:
    """
    Bind wheel event to document (overall window).

    Parameters
    ----------
    handler : _Handler
        Callable that handle wheel event.
    options : dict or None, default None
        Optional arguments dictionary to pass to.

    Returns
    -------
    name : str
        Handler's name.

    References
    ----------
    - About the handler options’ type document
        - https://bit.ly/39tnYxC
    """
    with ap.DebugInfo(
            callable_=bind_wheel_event_to_document, locals_=locals(),
            module_name=__name__):
        from apysc._event.handler import HandlerData
        from apysc._event.handler import append_handler_expression
        from apysc._event.handler import get_handler_name
        from apysc._validation.handler_options_validation import \
            validate_options_type
        validate_options_type(options=options)
        name: str = get_handler_name(handler=handler, instance=ap.document)
        expression: str = (
            f'$({ap.document.variable_name}).on("mousewheel", {name});'
        )
        ap.append_js_expression(expression=expression)

        if options is None:
            options = {}  # type: ignore
        handler_data: HandlerData = {
            'handler': handler,
            'options': options,
        }
        e: ap.WheelEvent = ap.WheelEvent(this=ap.document)
        append_handler_expression(
            handler_data=handler_data, handler_name=name, e=e)
        return name


def unbind_wheel_event_from_document(handler: _Handler[_O]) -> None:
    """
    Unbind specified handler's wheel event from document (overall window).

    Parameters
    ----------
    handler : _Handler
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
