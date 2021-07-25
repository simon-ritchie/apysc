"""Class implementation for handler.
"""

from typing import Any
from typing import Dict
from typing import List
from typing import Union

from typing_extensions import Protocol
from typing_extensions import TypedDict

from apysc._event.event import Event
from apysc._event.mouse_event_type import MouseEventType
from apysc._type.variable_name_interface import VariableNameInterface

Event_ = Any


class Handler(Protocol):
    """
    Event handler's callable interface.
    """

    def __call__(
            self, e: Event_,
            options: Dict[str, Any]) -> None:
        """
        Event handler's callable interface.

        Parameters
        ----------
        e : Event
            Created event instance.
        options : dict
            Optional arguments dictionary to pass to.
        """


class HandlerData(TypedDict):
    handler: Union[Handler]
    options: Dict[str, Any]


def get_handler_name(
        handler: Handler, instance: Any) -> str:
    """
    Get a handler name.

    Parameters
    ----------
    handler : Handler
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
    return handler_name


def append_handler_expression(
        handler_data: HandlerData, handler_name: str,
        e: Event) -> None:
    """
    Append a handler's expression to the file.

    Parameters
    ----------
    handler_data : HandlerData
        Target handler's data to append.
    handler_name : str
        Target handler's name.
    e : Event
        Created event instance.
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=append_handler_expression, locals_=locals(),
            module_name=__name__):
        from apysc._expression.event_handler_scope import HandlerScope
        from apysc._expression.indent_num import Indent
        from apysc._type import revert_interface
        from apysc._validation.event_validation import validate_event
        validate_event(e=e)
        variables: List[Any] = [*handler_data['options'].values()]
        snapshot_name: str = revert_interface.make_variables_snapshots(
            variables=variables)

        with HandlerScope():
            expression: str = (
                f'function {handler_name}({e.variable_name}) {{'
            )
            ap.append_js_expression(expression=expression)
            with Indent():
                handler_data['handler'](e=e, options=handler_data['options'])
            ap.append_js_expression(expression='}')

        revert_interface.revert_variables(
            snapshot_name=snapshot_name, variables=variables)


def append_unbinding_expression(
        this: VariableNameInterface, handler_name: str,
        mouse_event_type: MouseEventType) -> None:
    """
    Append event unbinding expression to file.

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
    Append all events unbinding expression to file.

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
