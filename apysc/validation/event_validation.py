"""Event validation implementation.

Mainly following interfaces are defined.

- validate_event
    Validate specified instance is Event.
"""

from typing import Any

from apysc import Event


def validate_event(e: Any) -> Event:
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

    Returns
    -------
    e : Event
        Event instance.
    """
    from apysc import Event
    if isinstance(e, Event):
        return e
    raise ValueError(
        f'Specified instance is not Event type: {type(e)}')
