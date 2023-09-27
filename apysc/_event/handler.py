"""Class implementation for a handler.
"""

from dataclasses import dataclass
from typing import Any
from typing import Callable
from typing import Generic
from typing import List
from typing import TypeVar

from apysc._event.event import Event
from apysc._event.mouse_event_type import MouseEventType
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos

_Handler = Callable[[Any, Any], None]
_EventType = TypeVar("_EventType", bound=Event)


@dataclass
class HandlerData(Generic[_EventType]):
    handler: Callable[[_EventType, Any], None]
    options: Any


def get_handler_name(*, handler: _Handler, instance: Any) -> str:
    """
    Get a handler name.

    Parameters
    ----------
    handler : _Handler
        Target handler.
    instance : VariableNameMixIn
        Instance to bind target handler.

    Returns
    -------
    handler_name : str
        Handler name (method path + class name (if handler is method)
        + function or method name) + instance's variable name.
    """
    from apysc._callable import callable_util
    from apysc._event import handler_circular_calling_util as circ_util
    from apysc._validation.variable_name_validation import (
        validate_variable_name_mixin_type,
    )

    class_name: str = callable_util.get_method_class_name(method=handler)
    if class_name != "":
        class_name = f"{class_name}_"
    handler_name: str = (
        f"{handler.__module__}{class_name}{handler.__name__}"  # type: ignore
    )
    handler_name = handler_name.replace(".", "_")
    instance_: VariableNameMixIn = validate_variable_name_mixin_type(instance=instance)
    handler_name += f"_{instance_.variable_name}"
    if circ_util.is_handler_circular_calling(handler_name=handler_name):
        return circ_util.get_prev_handler_name(handler_name=handler_name)
    return handler_name


@arg_validation_decos.is_event(arg_position_index=2)
@add_debug_info_setting(module_name=__name__)
def append_handler_expression(
    *,
    handler_data: HandlerData,
    handler_name: str,
    e: Event,
    in_handler_head_expression: str = "",
) -> None:
    """
    Append a handler's expression.

    Parameters
    ----------
    handler_data : HandlerData
        Target handler's data to append.
    handler_name : str
        Target handler's name.
    e : Event
        Created event instance.
    in_handler_head_expression : str, default ""
        Optional expression to be added at the handler function's
        head position.
    """
    from apysc._event.handler_circular_calling_util import is_handler_circular_calling
    from apysc._expression import expression_data_util
    from apysc._expression.event_handler_scope import HandlerScope
    from apysc._expression.indent_num import Indent
    from apysc._type import revert_mixin
    from apysc._validation.variable_name_validation import (
        validate_variable_name_mixin_type,
    )

    variables: List[Any] = [*handler_data.options.values()]
    snapshot_name: str = revert_mixin.make_variables_snapshots(variables=variables)
    instance: VariableNameMixIn = validate_variable_name_mixin_type(instance=e.this)

    with HandlerScope(handler_name=handler_name, instance=instance):
        is_handler_circular_calling_: bool = is_handler_circular_calling(
            handler_name=handler_name
        )
        if not is_handler_circular_calling_:
            expression: str = f"function {handler_name}({e.variable_name}) {{"
            expression_data_util.append_js_expression(expression=expression)
            with Indent():
                _append_in_handler_head_expression(
                    in_handler_head_expression=in_handler_head_expression
                )
                handler_data.handler(e, handler_data.options)
            expression_data_util.append_js_expression(expression="}")

    revert_mixin.revert_variables(snapshot_name=snapshot_name, variables=variables)


@add_debug_info_setting(module_name=__name__)
def _append_in_handler_head_expression(*, in_handler_head_expression: str) -> None:
    """
    Append an in-handler head expression if it is not blank.

    Parameters
    ----------
    in_handler_head_expression : str
        Optional expression to be added at the handler function's
        head position if it is not blank.
    """
    from apysc._expression import expression_data_util

    if in_handler_head_expression == "":
        return
    expression_data_util.append_js_expression(expression=in_handler_head_expression)


@add_debug_info_setting(module_name=__name__)
def append_unbinding_expression(
    *, this: VariableNameMixIn, handler_name: str, mouse_event_type: MouseEventType
) -> None:
    """
    Append event unbinding expression.

    Parameters
    ----------
    this : VariableNameMixIn
        Instance that event is binded.
    handler_name : str
        Target handler's name.
    mouse_event_type : MouseEventType
        Event type to unbind.
    """
    from apysc._expression import expression_data_util
    from apysc._validation import event_validation

    event_validation.validate_event_type(mouse_event_type=mouse_event_type)
    expression: str = (
        f'{this.variable_name}.off("{mouse_event_type.value}", ' f"{handler_name});"
    )
    expression_data_util.append_js_expression(expression=expression)


@add_debug_info_setting(module_name=__name__)
def append_unbinding_all_expression(
    *, this: VariableNameMixIn, mouse_event_type: MouseEventType
) -> None:
    """
    Append all events unbinding expression.

    Parameters
    ----------
    this : VariableNameMixIn
        Instance that events are binded.
    mouse_event_type : MouseEventType
        Event type to unbind.
    """
    from apysc._expression import expression_data_util
    from apysc._validation import event_validation

    event_validation.validate_event_type(mouse_event_type=mouse_event_type)
    expression: str = f'{this.variable_name}.off("{mouse_event_type.value}");'
    expression_data_util.append_js_expression(expression=expression)
