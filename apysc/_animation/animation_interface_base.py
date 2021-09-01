"""Base class for each animation interface.
"""

from apysc._animation.animation_pause_interface import AnimationPauseInterface
from apysc._animation.animation_play_interface import AnimationPlayInterface
from apysc._animation.animation_reset_interface import AnimationResetInterface


class AnimationInterfaceBase(
        AnimationPauseInterface, AnimationPlayInterface,
        AnimationResetInterface):
    """Base class for each animation interface.
    """
