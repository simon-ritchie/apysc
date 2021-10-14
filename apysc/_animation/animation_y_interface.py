"""Class implementation for the animation_y interface.
"""

from typing import Union

import apysc as ap
from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_y import AnimationY
from apysc._animation.easing import Easing


class AnimationYInterface(AnimationInterfaceBase):

    def animation_y(
            self,
            y: Union[int, ap.Int],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationY:
        """
        Set the y-coordinate animation setting.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        y : int or Int
            Destination of the y-coordinate.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_y : AnimationY
            Created animation setting instance.

        References
        ----------
        - animation_y interface document
            - https://simon-ritchie.github.io/apysc/animation_y.html
        - Animation interfaces duration setting document
            - https://simon-ritchie.github.io/apysc/animation_duration.html
        - Each animation interface return value document
            - https://bit.ly/2XOoa8w
        - Easing enum document
            - https://simon-ritchie.github.io/apysc/easing_enum.html
        """
        animation_y: AnimationY = AnimationY(
            target=self,
            y=y,
            duration=duration,
            delay=delay,
            easing=easing)
        return animation_y
