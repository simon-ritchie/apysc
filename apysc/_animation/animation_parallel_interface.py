"""Class implementation for the parallel animation interface.
"""

import apysc as ap
from typing import List, Union

from apysc._animation.animation_base import AnimationBase
from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.easing import Easing
from apysc._animation.animation_parallel import AnimationParallel


class AnimationParallelInterface(AnimationInterfaceBase):

    def animation_parallel(
            self,
            animations: List[AnimationBase],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationParallel:
        """
        Set the parallel animation setting.

        Notes
        -----
        - To start this animation, you need to call the `start` method of
            the returned instance.
        - The `animations` argument can't contains the `AnimationParallel`
            instance.
        - The `duration`, `delay`, and `easing` arguments in the
            `animations` argument will be ignored (this interface's
            arguments will be refered instead).

        Raises
        ------
        ValueError
            If the animations's target is not this instance.

        Parameters
        ----------
        animations : list of AnimationBase
            Target animation settings.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.
        """
        animation_parallel: AnimationParallel = AnimationParallel(
            target=self,
            animations=animations,
            duration=duration,
            delay=delay,
            easing=easing)
        return animation_parallel
