"""Class implementation for the animation_scale_x_from_point
interface.
"""

from typing import Union

import apysc as ap
from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_scale_x_from_point import \
    AnimationScaleXFromPoint
from apysc._animation.easing import Easing


class AnimationScaleXFromPointInterface(AnimationInterfaceBase):

    def animation_scale_x_from_point(
            self,
            scale_x_from_point: Union[float, ap.Number],
            x: Union[int, ap.Int],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationScaleXFromPoint:
        """
        Set the scale-x from the given point animation setting.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        scale_x_from_point : float or Number
            The final scale-x from the given point of the animation.
        x : int or Int
            X-coordinate.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_scale_x_from_point : AnimationScaleXFromPoint
            Created animation setting instance.

        References
        ----------
        - animation_scale_x_from_point interface document
            - https://bit.ly/3j3It9o
        - Animation interfaces duration setting document
            - https://simon-ritchie.github.io/apysc/animation_duration.html
        - Each animation interface return value document
            - https://bit.ly/2XOoa8w
        - Easing enum document
            - https://simon-ritchie.github.io/apysc/easing_enum.html
        """
        animation_scale_x_from_point: AnimationScaleXFromPoint = \
            AnimationScaleXFromPoint(
                target=self,
                scale_x_from_point=scale_x_from_point,
                x=x,
                duration=duration,
                delay=delay,
                easing=easing)
        return animation_scale_x_from_point
