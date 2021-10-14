"""Class implementation for the animation_width interface.
"""

from typing import Union

import apysc as ap
from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_width import AnimationWidth
from apysc._animation.easing import Easing


class AnimationWidthInterface(AnimationInterfaceBase):

    def animation_width(
            self,
            width: Union[int, ap.Int],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationWidth:
        """
        Set the width animation setting.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        width : int or Int
            The final width of the animation.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_width : AnimationWidth
            Created animation setting instance.

        References
        ----------
        - animation_width and animation_height interfaces document
            - https://bit.ly/39XPUdq
        - Animation interfaces duration setting document
            - https://simon-ritchie.github.io/apysc/animation_duration.html
        - Each animation interface return value document
            - https://bit.ly/2XOoa8w
        - Easing enum document
            - https://simon-ritchie.github.io/apysc/easing_enum.html
        """
        animation_width: AnimationWidth = AnimationWidth(
            target=self,
            width=width,
            duration=duration,
            delay=delay,
            easing=easing)
        return animation_width
