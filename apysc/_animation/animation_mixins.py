"""Base class for each animation mix-in.
"""

from apysc._animation.animation_finish_interface import AnimationFinishInterface
from apysc._animation.animation_pause_mixin import AnimationPauseMixIn
from apysc._animation.animation_play_mixin import AnimationPlayMixIn
from apysc._animation.animation_reset_mixin import AnimationResetMixIn
from apysc._animation.animation_reverse_interface import AnimationReverseInterface
from apysc._animation.animation_time_mixin import AnimationTimeMixIn


class AnimationMixIns(
    AnimationPauseMixIn,
    AnimationPlayMixIn,
    AnimationResetMixIn,
    AnimationFinishInterface,
    AnimationReverseInterface,
    AnimationTimeMixIn,
):
    """Base class for each animation mix-in."""
