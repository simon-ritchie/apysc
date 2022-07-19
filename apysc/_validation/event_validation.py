"""Event validation implementation.

Mainly following interfaces are defined.

- validate_event
    Validate specified instance is Event.
"""

from typing import Any

from apysc._event.event import Event
from apysc._event.mouse_event_type import MouseEventType


def validate_event(*, e: Any, additional_err_msg: str = "") -> Event:
    """
    Validate whether a specified instance is the
    `Event` class or not.

    Parameters
    ----------
    e : Event
        Event instance to check.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        If a specified instance is not the `Event`
        class instance.

    Returns
    -------
    e : Event
        Event instance.
    """
    if isinstance(e, Event):
        return e
    if additional_err_msg != "":
        additional_err_msg = f"\n{additional_err_msg}"
    raise ValueError(
        f"Specified instance is not Event type: {type(e)}" f"{additional_err_msg}"
    )


def validate_event_type(*, mouse_event_type: Any) -> MouseEventType:
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
    if isinstance(mouse_event_type, MouseEventType):
        return mouse_event_type
    raise ValueError(
        f"Specified value is not a MouseEventType: {type(mouse_event_type)}"
    )
