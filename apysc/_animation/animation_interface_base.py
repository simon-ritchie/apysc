"""Base class for each animation interface.
"""

from apysc._animation.animation_finish_interface import \
    AnimationFinishInterface
from apysc._animation.animation_pause_interface import AnimationPauseInterface
from apysc._animation.animation_play_interface import AnimationPlayInterface
from apysc._animation.animation_reset_interface import AnimationResetInterface
from apysc._animation.animation_reverse_interface import \
    AnimationReverseInterface
from apysc._animation.animation_time_interface import AnimationTimeInterface


class AnimationInterfaceBase(
        AnimationPauseInterface, AnimationPlayInterface,
        AnimationResetInterface, AnimationFinishInterface,
        AnimationReverseInterface, AnimationTimeInterface):
    """Base class for each animation interface.
    """
