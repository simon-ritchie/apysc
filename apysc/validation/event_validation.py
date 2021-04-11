"""Event validation implementation.

Mainly following interfaces are defined.

- validate_event
    Validate specified instance is Event.
"""

from typing import Any


def validate_event(e: Any) -> None:
    """
    Validate specified instance is Event.

    Parameters
    ----------
    e : Event
        Event instance to check.

    Raises
    ------
    ValueError
        If specified instance is not Event instance.
    """
    from apysc import Event
    if isinstance(e, Event):
        return
    raise ValueError(
        f'Specified instance is not Event type: {type(e)}')
