"""Class implementation for the animation_scale_x_from_center
interface.
"""

from typing import Union

import apysc as ap
from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_scale_x_from_center import \
    AnimationScaleXFromCenter
from apysc._animation.easing import Easing


class AnimationScaleXFromCenterInterface(AnimationInterfaceBase):

    def animation_scale_x_from_center(
            self,
            scale_x_from_center: Union[float, ap.Number],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationScaleXFromCenter:
        """
        Set the scale-x from the center point animation setting.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        scale_x_from_center : float or Number
            The final scale-x of the animation.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_scale_x_from_center : AnimationScaleXFromCenter
            Created animation setting instance.

        References
        ----------
        - animation_scale_x_from_center interface document
            - https://bit.ly/30qsD2m
        - Animation interfaces duration setting document
            - https://simon-ritchie.github.io/apysc/animation_duration.html
        - Each animation interface return value document
            - https://bit.ly/2XOoa8w
        - Easing enum document
            - https://simon-ritchie.github.io/apysc/easing_enum.html
        """
        animation_scale_x_from_center: AnimationScaleXFromCenter = \
            AnimationScaleXFromCenter(
                target=self,
                scale_x_from_center=scale_x_from_center,
                duration=duration,
                delay=delay,
                easing=easing)
        return animation_scale_x_from_center
