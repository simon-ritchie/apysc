"""Class implementation for the animation_skew_x interface.
"""

from typing import Union

import apysc as ap
from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_skew_x import AnimationSkewX
from apysc._animation.easing import Easing


class AnimationSkewXInterface(AnimationInterfaceBase):

    def animation_skew_x(
            self,
            skew_x: Union[int, ap.Int],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationSkewX:
        """
        Set the skew-x animation setting.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        skew_x : int or Int
            The final skew-x of the animation.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_skew_x : AnimationSkewX
            Created animation setting instance.

        References
        ----------
        - animation_skew_x interface document
            - https://simon-ritchie.github.io/apysc/animation_skew_x.html
        - Animation interfaces duration setting document
            - https://simon-ritchie.github.io/apysc/animation_duration.html
        - Each animation interface return value document
            - https://bit.ly/2XOoa8w
        - Easing enum document
            - https://simon-ritchie.github.io/apysc/easing_enum.html
        """
        animation_skew_x: AnimationSkewX = AnimationSkewX(
            target=self,
            skew_x=skew_x,
            duration=duration,
            delay=delay,
            easing=easing)
        return animation_skew_x
