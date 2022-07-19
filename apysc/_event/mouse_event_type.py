"""This module is for the definitions of the mouse
event types.
"""

from enum import Enum


class MouseEventType(Enum):
    """
    Mouse event type definitions.
    """

    CLICK = "click"
    DBLCLICK = "dblclick"
    MOUSEDOWN = "mousedown"
    MOUSEUP = "mouseup"
    MOUSEOVER = "mouseover"
    MOUSEOUT = "mouseout"
    MOUSEMOVE = "mousemove"
