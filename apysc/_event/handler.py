"""Class implementation for handler.
"""

from typing import Any
from typing import Callable
from typing import List

from typing_extensions import TypedDict

from apysc._event.event import Event
from apysc._event.mouse_event_type import MouseEventType
from apysc._type.variable_name_interface import VariableNameInterface

Event_ = Any
_Handler = Callable[[Any, Any], None]


class HandlerData(TypedDict):
    handler: Callable[[Event_, Any], None]
    options: Any


def get_handler_name(
        handler: _Handler, instance: Any) -> str:
    """
    Get a handler name.

    Parameters
    ----------
    handler : _Handler
        Target handler.
    instance : VariableNameInterface
        Instance to bind target handler.

    Returns
    -------
    handler_name : str
        Handler name (method path + class name (if handler is method)
        + function or method name) + instance's variable name.
    """
    from apysc._callable import callable_util
    from apysc._event import handler_circular_calling_util as circ_util
    from apysc._validation.variable_name_validation import \
        validate_variable_name_interface_type
    class_name: str = callable_util.get_method_class_name(method=handler)
    if class_name != '':
        class_name = f'{class_name}_'
    handler_name: str = (
        f'{handler.__module__}{class_name}{handler.__name__}'  # type: ignore
    )
    handler_name = handler_name.replace('.', '_')
    instance_: VariableNameInterface = validate_variable_name_interface_type(
        instance=instance)
    handler_name += f'_{instance_.variable_name}'
    if circ_util.is_handler_circular_calling(handler_name=handler_name):
        return circ_util.get_prev_handler_name(handler_name=handler_name)
    return handler_name


def append_handler_expression(
        handler_data: HandlerData,
        handler_name: str,
        e: Event,
        in_handler_head_expression: str = '') -> None:
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
    in_handler_head_expression : str, default ''
        Optional expression to be added at the handler function's
        head position.
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=append_handler_expression, locals_=locals(),
            module_name=__name__):
        from apysc._event.handler_circular_calling_util import \
            is_handler_circular_calling
        from apysc._expression.event_handler_scope import HandlerScope
        from apysc._expression.indent_num import Indent
        from apysc._type import revert_interface
        from apysc._validation.event_validation import validate_event
        from apysc._validation.variable_name_validation import \
            validate_variable_name_interface_type
        validate_event(e=e)
        variables: List[Any] = [*handler_data['options'].values()]
        snapshot_name: str = revert_interface.make_variables_snapshots(
            variables=variables)
        instance: VariableNameInterface = \
            validate_variable_name_interface_type(instance=e.this)

        with HandlerScope(handler_name=handler_name, instance=instance):
            is_handler_circular_calling_: bool = is_handler_circular_calling(
                handler_name=handler_name)
            if not is_handler_circular_calling_:
                expression: str = (
                    f'function {handler_name}({e.variable_name}) {{'
                )
                ap.append_js_expression(expression=expression)
                with Indent():
                    _append_in_handler_head_expression(
                        in_handler_head_expression=in_handler_head_expression)
                    handler_data['handler'](
                        e, handler_data['options'])
                ap.append_js_expression(expression='}')

        revert_interface.revert_variables(
            snapshot_name=snapshot_name, variables=variables)


def _append_in_handler_head_expression(
        in_handler_head_expression: str) -> None:
    """
    Append an in-handler head expression if it is not blank.

    Parameters
    ----------
    in_handler_head_expression : str
        Optional expression to be added at the handler function's
        head position if it is not blank.
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=_append_in_handler_head_expression, locals_=locals(),
            module_name=__name__):
        if in_handler_head_expression == '':
            return
        ap.append_js_expression(expression=in_handler_head_expression)


def append_unbinding_expression(
        this: VariableNameInterface, handler_name: str,
        mouse_event_type: MouseEventType) -> None:
    """
    Append event unbinding expression.

    Parameters
    ----------
    this : VariableNameInterface
        Instance that event is binded.
    handler_name : str
        Target handler's name.
    mouse_event_type : MouseEventType
        Event type to unbind.
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=append_unbinding_expression, locals_=locals(),
            module_name=__name__):
        from apysc._validation import event_validation
        event_validation.validate_event_type(
            mouse_event_type=mouse_event_type)
        expression: str = (
            f'{this.variable_name}.off("{mouse_event_type.value}", '
            f'{handler_name});'
        )
        ap.append_js_expression(expression=expression)


def append_unbinding_all_expression(
        this: VariableNameInterface,
        mouse_event_type: MouseEventType) -> None:
    """
    Append all events unbinding expression.

    Parameters
    ----------
    this : VariableNameInterface
        Instance that events are binded.
    mouse_event_type : MouseEventType
        Event type to unbind.
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=append_unbinding_all_expression, locals_=locals(),
            module_name=__name__):
        from apysc._validation import event_validation
        event_validation.validate_event_type(
            mouse_event_type=mouse_event_type)
        expression: str = (
            f'{this.variable_name}.off("{mouse_event_type.value}");'
        )
        ap.append_js_expression(expression=expression)
