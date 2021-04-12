"""Class implementation for handler.
"""

from typing import Any
from typing import Dict
from typing import List

from typing_extensions import Protocol
from typing_extensions import TypedDict

_Event = Any


class Handler(Protocol):

    def __call__(self, e: _Event, kwargs: Dict[str, Any]) -> None:
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
        e: _Event) -> None:
    """
    Append handler's expression to file.

    Parameters
    ----------
    handler_data : HandlerData
        Target handler's data to append.
    handler_name : str
        Target Handler's name.
    e : Event
        Created event instance.
    """
    from apysc import Event
    from apysc.expression import expression_file_util
    from apysc.expression import indent_num
    from apysc.expression.event_handler_scope import HandlerScope
    from apysc.type import revert_interface
    from apysc.validation.event_validation import validate_event
    e_: Event = validate_event(e=e)
    variables: List[Any] = [*handler_data['kwargs'].values()]
    snapshot_name: str = revert_interface.make_variables_snapshots(
        variables=variables)

    with HandlerScope():
        expression: str = (
            f'function {handler_name}({e_.variable_name}) {{'
        )
        expression_file_util.append_js_expression(expression=expression)
        indent_num.increment()
        handler_data['handler'](e=e_, kwargs=handler_data['kwargs'])
        indent_num.decrement()
        expression_file_util.append_js_expression(expression='}')

    revert_interface.revert_variables(
        snapshot_name=snapshot_name, variables=variables)
