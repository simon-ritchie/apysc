"""Class implementation for the animation_fill_alpha interface.
"""

from typing import Union

import apysc as ap
from apysc._animation.animation_fill_alpha import AnimationFillAlpha
from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.easing import Easing


class AnimationFillAlphaInterface(AnimationInterfaceBase):

    def animation_fill_alpha(
            self,
            alpha: Union[float, ap.Number],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationFillAlpha:
        """
        Set the fill alpha (opacity) animation setting.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        alpha : float or Number
            The final alpha (opacity) of the animation.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_fill_alpha : AnimationFillAlpha
            Created animation setting instance.

        References
        ----------
        - animation_fill_alpha interface document
            - https://simon-ritchie.github.io/apysc/animation_fill_alpha.html
        - Animation interfaces duration setting document
            - https://simon-ritchie.github.io/apysc/animation_duration.html
        - Each animation interface return value document
            - https://bit.ly/2XOoa8w
        - Easing enum document
            - https://simon-ritchie.github.io/apysc/easing_enum.html
        """
        animation_fill_alpha: AnimationFillAlpha = AnimationFillAlpha(
            target=self,
            alpha=alpha,
            duration=duration,
            delay=delay,
            easing=easing)
        return animation_fill_alpha
