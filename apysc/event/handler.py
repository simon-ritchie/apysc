"""Class implementation for handler.
"""

from typing import Any
from typing import Dict
from typing import List

from typing_extensions import Protocol
from typing_extensions import TypedDict

from apysc.event.event import Event
from apysc.event.event_type import EventType
from apysc.type.variable_name_interface import VariableNameInterface

Event_ = Any


class Handler(Protocol):

    def __call__(
            self, e: Event_,
            kwargs: Dict[str, Any]) -> None:
        """
        Event handler's callable interface.

        Parameters
        ----------
        e : Event
            Created event instance.
        kwargs : dict
            Keyword arguments to pass to.
        """


class HandlerData(TypedDict):
    handler: Handler
    kwargs: Dict[str, Any]


def get_handler_name(handler: Handler) -> str:
    """
    Get a handler name.

    Parameters
    ----------
    handler : Handler
        Target handler.

    Returns
    -------
    handler_name : str
        Handler name (method path + class name (if handler is method)
        + function or method name).
    """
    from apysc.callable import callable_util
    class_name: str = callable_util.get_method_class_name(method=handler)
    if class_name != '':
        class_name = f'{class_name}_'
    handler_name: str = (
        f'{handler.__module__}{class_name}{handler.__name__}'  # type: ignore
    )
    handler_name = handler_name.replace('.', '_')
    return handler_name


def append_handler_expression(
        handler_data: HandlerData, handler_name: str,
        e: Event) -> None:
    """
    Append handler's expression to file.

    Parameters
    ----------
    handler_data : HandlerData
        Target handler's data to append.
    handler_name : str
        Target handler's name.
    e : Event
        Created event instance.
    """
    from apysc.expression import expression_file_util
    from apysc.expression.event_handler_scope import HandlerScope
    from apysc.expression.indent_num import Indent
    from apysc.type import revert_interface
    from apysc.validation.event_validation import validate_event
    validate_event(e=e)
    variables: List[Any] = [*handler_data['kwargs'].values()]
    snapshot_name: str = revert_interface.make_variables_snapshots(
        variables=variables)

    with HandlerScope():
        expression: str = (
            f'function {handler_name}({e.variable_name}) {{'
        )
        expression_file_util.append_js_expression(expression=expression)
        with Indent():
            handler_data['handler'](e=e, kwargs=handler_data['kwargs'])
        expression_file_util.append_js_expression(expression='}')

    revert_interface.revert_variables(
        snapshot_name=snapshot_name, variables=variables)


def append_unbinding_expression(
        this: VariableNameInterface, handler_name: str,
        event_type: EventType) -> None:
    """
    Append event unbinding expression to file.

    Parameters
    ----------
    this : VariableNameInterface
        Instance that event is binded.
    handler_name : str
        Target handler's name.
    event_type : EventType
        Event type to unbind.
    """
    from apysc.expression import expression_file_util
    from apysc.validation import event_validation
    event_validation.validate_event_type(event_type=event_type)
    expression: str = (
        f'{this.variable_name}.off("{event_type.value}", {handler_name});'
    )
    expression_file_util.append_js_expression(expression=expression)


def append_unbinding_all_expression(
        this: VariableNameInterface,
        event_type: EventType) -> None:
    """
    Append all events unbinding expression to file.

    Parameters
    ----------
    this : VariableNameInterface
        Instance that events are binded.
    event_type : EventType
        Event type to unbind.
    """
    from apysc.expression import expression_file_util
    from apysc.validation import event_validation
    event_validation.validate_event_type(event_type=event_type)
    expression: str = (
        f'{this.variable_name}.off("{event_type.value}");'
    )
    expression_file_util.append_js_expression(expression=expression)
