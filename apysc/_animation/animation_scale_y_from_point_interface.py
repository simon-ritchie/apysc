"""Class implementation for the animation_scale_y_from_point
interface.
"""

from typing import Union

import apysc as ap
from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_scale_y_from_point import \
    AnimationScaleYFromPoint
from apysc._animation.easing import Easing


class AnimationScaleYFromPointInterface(AnimationInterfaceBase):

    def animation_scale_y_from_point(
            self,
            scale_y_from_point: Union[float, ap.Number],
            y: Union[int, ap.Int],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationScaleYFromPoint:
        """
        Set the scale-y from the given point animation setting.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        scale_y_from_point : float or Number
            The final scale-y from the given point of the animation.
        y : int or Int
            Y-coordinate.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_scale_y_from_point : AnimationScaleYFromPoint
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
        animation_scale_y_from_point: AnimationScaleYFromPoint = \
            AnimationScaleYFromPoint(
                target=self,
                scale_y_from_point=scale_y_from_point,
                y=y,
                duration=duration,
                delay=delay,
                easing=easing)
        return animation_scale_y_from_point
