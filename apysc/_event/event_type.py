"""Definitions of event type.
"""

from enum import Enum


class EventType(Enum):

    CLICK = 'click'
    DBLCLICK = 'dblclick'
    MOUSEDOWN = 'mousedown'
    MOUSEUP = 'mouseup'
    MOUSEOVER = 'mouseover'
    MOUSEOUT = 'mouseout'
    MOUSEMOVE = 'mousemove'
