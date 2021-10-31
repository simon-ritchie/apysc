"""Class implementation for the parallel animation interface.
"""

from typing import List
from typing import Union

import apysc as ap
from apysc._animation.animation_base import AnimationBase
from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_parallel import AnimationParallel
from apysc._animation.easing import Easing


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
            - If the animations's target is not this instance.
            - If there are changed `duration`, `delay`, or
                `easing` animation settings in the `animations`
                list.

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

        Returns
        -------
        animation_parallel : AnimationParallel
            Created animation setting instance.
        """
        animation_parallel: AnimationParallel = AnimationParallel(
            target=self,
            animations=animations,
            duration=duration,
            delay=delay,
            easing=easing)
        return animation_parallel
