"""Implementation of mouse wheel event interfaces.

Notes
-----
Not supported each SVG elements' mouse wheel event currently, only
supported document (overall screen) mouse wheel.
"""

from typing import Callable
from typing import Optional
from typing import TypeVar

from apysc._event.wheel_event import WheelEvent
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos

_Options = TypeVar("_Options")
_Handler = Callable[[WheelEvent, _Options], None]


@arg_validation_decos.handler_args_num(arg_position_index=0)
@arg_validation_decos.handler_options_type(arg_position_index=1)
@add_debug_info_setting(module_name=__name__)
def bind_wheel_event_to_document(
    *, handler: _Handler[_Options], options: Optional[_Options] = None
) -> str:
    """
    Bind wheel event to document (overall window).

    Parameters
    ----------
    handler : _Handler
        Callable that handles wheel event.
    options : dict or None, default None
        Optional arguments dictionary to pass.

    Returns
    -------
    name : str
        Handler's name.

    References
    ----------
    - About the handler options' type
        - https://simon-ritchie.github.io/apysc/en/about_handler_options_type.html  # noqa
    """
    from apysc._display._document import document
    from apysc._event.handler import HandlerData
    from apysc._event.handler import append_handler_expression
    from apysc._event.handler import get_handler_name
    from apysc._event.wheel_event import WheelEvent
    from apysc._expression import expression_data_util

    name: str = get_handler_name(handler=handler, instance=document)
    expression: str = f'$({document.variable_name}).on("mousewheel", {name});'
    expression_data_util.append_js_expression(expression=expression)

    if options is None:
        options = {}  # type: ignore
    handler_data: HandlerData[WheelEvent] = HandlerData(
        handler=handler, options=options
    )
    e: WheelEvent = WheelEvent(this=document)
    append_handler_expression(handler_data=handler_data, handler_name=name, e=e)
    return name


@arg_validation_decos.handler_args_num(arg_position_index=0)
@add_debug_info_setting(module_name=__name__)
def unbind_wheel_event_from_document(*, handler: _Handler[_Options]) -> None:
    """
    Unbind a specified handler's wheel event from a document
    (overall window).

    Parameters
    ----------
    handler : _Handler
        Callable to unbind.
    """
    from apysc._display._document import document
    from apysc._event.handler import get_handler_name
    from apysc._expression import expression_data_util

    name: str = get_handler_name(handler=handler, instance=document)
    expression: str = f'$({document.variable_name}).off("mousewheel", {name});'
    expression_data_util.append_js_expression(expression=expression)


@add_debug_info_setting(module_name=__name__)
def unbind_wheel_event_all_from_document() -> None:
    """
    Unbind all wheels event from the document (overall window).
    """
    from apysc._display._document import document
    from apysc._expression import expression_data_util

    expression: str = f'$({document.variable_name}).off("mousewheel");'
    expression_data_util.append_js_expression(expression=expression)
