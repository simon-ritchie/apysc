"""Base class for each animation interface.
"""

from apysc._animation.animation_pause_interface import AnimationPauseInterface
from apysc._animation.animation_play_interface import AnimationPlayInterface


class AnimationInterfaceBase(
        AnimationPauseInterface, AnimationPlayInterface):
    """Base class for each animation interface.
    """
