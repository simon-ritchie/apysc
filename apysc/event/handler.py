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
