"""This module is for the definitions of the custom
event types.
"""

from enum import Enum


class CustomEventType(Enum):

    TIMER_COMPLETE = "timer_complete"
    ANIMATION_COMPLETE = "animation_complete"
