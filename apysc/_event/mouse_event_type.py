"""Definitions of the mouse event type.
"""

from enum import Enum


class MouseEventType(Enum):
    """
    Mouse event type definitions.
    """

    CLICK = 'click'
    DBLCLICK = 'dblclick'
    MOUSEDOWN = 'mousedown'
    MOUSEUP = 'mouseup'
    MOUSEOVER = 'mouseover'
    MOUSEOUT = 'mouseout'
    MOUSEMOVE = 'mousemove'
