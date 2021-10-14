"""Class implementation for the animation_rotation_aroound_center
interface.
"""

from typing import Union

import apysc as ap
from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_rotation_around_center import \
    AnimationRotationAroundCenter
from apysc._animation.easing import Easing


class AnimationRotationAroundCenterInterface(AnimationInterfaceBase):

    def animation_rotation_around_center(
            self,
            rotation_around_center: Union[int, ap.Int],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationRotationAroundCenter:
        """
        Set the rotation around the center animation setting.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        rotation_around_center : int or Int
            The final rotation of the animation.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_rotation_around_center : AnimationRotationAroundCenter
            Created animation setting instance.

        References
        ----------
        - animation_rotation_around_center interface document
            - https://bit.ly/3FLb6lK
        - Animation interfaces duration setting document
            - https://simon-ritchie.github.io/apysc/animation_duration.html
        - Each animation interface return value document
            - https://bit.ly/2XOoa8w
        - Easing enum document
            - https://simon-ritchie.github.io/apysc/easing_enum.html
        """
        animation_rotation_around_center: AnimationRotationAroundCenter = \
            AnimationRotationAroundCenter(
                target=self,
                rotation_around_center=rotation_around_center,
                duration=duration,
                delay=delay,
                easing=easing)
        return animation_rotation_around_center
