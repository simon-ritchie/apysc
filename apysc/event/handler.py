"""Class implementation for handler.
"""

from typing import Any, Dict

from typing_extensions import Protocol, TypedDict

Event = Any


class Handler(Protocol):

    def __call__(self, e: Event, kwargs: Dict[str, Any]) -> None:
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
    handler_name: str = (
        f'{handler.__module__}{class_name}{handler.__name__}'  # type: ignore
    )
    return handler_name
