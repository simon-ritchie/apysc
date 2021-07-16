"""Event validation implementation.

Mainly following interfaces are defined.

- validate_event
    Validate specified instance is Event.
"""

from typing import Any

import apysc as ap


def validate_event(e: Any) -> ap.Event:
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
    if isinstance(e, ap.Event):
        return e
    raise ValueError(
        f'Specified instance is not Event type: {type(e)}')


def validate_event_type(mouse_event_type: Any) -> ap.MouseEventType:
    """
    Validate whether specified value is MouseEventType one or not.

    Parameters
    ----------
    mouse_event_type : MouseEventType
        EventTMouseEventTypeype value to check.

    Returns
    -------
    mouse_event_type : MouseEventType
        MouseEventType value.
    """
    if isinstance(mouse_event_type, ap.MouseEventType):
        return mouse_event_type
    raise ValueError(
        f'Specified value is not a MouseEventType: {type(mouse_event_type)}')
