"""Base class for each animation mix-in.
"""

from apysc._animation.animation_finish_mixin import AnimationFinishMixIn
from apysc._animation.animation_pause_mixin import AnimationPauseMixIn
from apysc._animation.animation_play_mixin import AnimationPlayMixIn
from apysc._animation.animation_reset_mixin import AnimationResetMixIn
from apysc._animation.animation_reverse_mixin import AnimationReverseMixIn
from apysc._animation.animation_time_mixin import AnimationTimeMixIn


class AnimationMixIns(
    AnimationPauseMixIn,
    AnimationPlayMixIn,
    AnimationResetMixIn,
    AnimationFinishMixIn,
    AnimationReverseMixIn,
    AnimationTimeMixIn,
):
    """Base class for each animation mix-in."""
