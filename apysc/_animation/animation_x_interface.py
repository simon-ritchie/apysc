"""Class implementation for the animation_x interface.
"""

from typing import Union

import apysc as ap
from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_x import AnimationX
from apysc._animation.easing import Easing


class AnimationXInterface(AnimationInterfaceBase):

    def animation_x(
            self,
            x: Union[int, ap.Int],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationX:
        """
        Set the x-coordinate animation setting.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        x : int or Int
            Destination of the x-coordinate.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_x : AnimationX
            Created animation setting instance.

        References
        ----------
        - animation_x interface document
            - https://simon-ritchie.github.io/apysc/animation_x.html
        - Animation interfaces duration setting document
            - https://simon-ritchie.github.io/apysc/animation_duration.html
        - Each animation interface return value document
            - https://bit.ly/2XOoa8w
        - Easing enum document
            - https://simon-ritchie.github.io/apysc/easing_enum.html
        """
        animation_x: AnimationX = AnimationX(
            target=self,
            x=x,
            duration=duration,
            delay=delay,
            easing=easing)
        return animation_x
