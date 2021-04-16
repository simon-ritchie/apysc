"""Event validation implementation.

Mainly following interfaces are defined.

- validate_event
    Validate specified instance is Event.
"""

from typing import Any

from apysc import Event
from apysc import EventType


def validate_event(e: Any) -> Event:
    """
    Validate whether specified instance is Event or not.

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
    if isinstance(e, Event):
        return e
    raise ValueError(
        f'Specified instance is not Event type: {type(e)}')


def validate_event_type(event_type: Any) -> EventType:
    """
    Validate whether specified value is EventType one or not.

    Parameters
    ----------
    event_type : EventType
        EventType value to check.

    Returns
    -------
    event_type : EventType
        EventType value.
    """
    if isinstance(event_type, EventType):
        return event_type
    raise ValueError(
        f'Specified value is not EventType: {type(event_type)}')
