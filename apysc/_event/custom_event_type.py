"""Definitions of the custom event type.
"""

from enum import Enum


class CustomEventType(Enum):

    TIMER_COMPLETE = 'timer_complete'
    ANIMATION_COMPLETE = 'animation_complete'
