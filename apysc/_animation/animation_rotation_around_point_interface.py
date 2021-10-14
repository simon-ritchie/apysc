"""Class implementation for the animation_rotation_around_point
interface.
"""

from typing import Union

import apysc as ap
from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_rotation_around_point import \
    AnimationRotationAroundPoint
from apysc._animation.easing import Easing


class AnimationRotationAroundPointInterface(AnimationInterfaceBase):

    def animation_rotation_around_point(
            self,
            rotation_around_point: Union[int, ap.Int],
            x: Union[int, ap.Int],
            y: Union[int, ap.Int],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationRotationAroundPoint:
        """
        Set the rotation around the given point animation setting.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        rotation_around_point : int or Int
            The final rotation of the animation.
        x : int or int
            X-coordinate.
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
        animation_rotation_around_point : AnimationRotationAroundPoint
            Created animation setting instance.

        References
        ----------
        - animation_rotation_around_point interface document
            - https://bit.ly/3oWpy4i
        - Animation interfaces duration setting document
            - https://simon-ritchie.github.io/apysc/animation_duration.html
        - Each animation interface return value document
            - https://bit.ly/2XOoa8w
        - Easing enum document
            - https://simon-ritchie.github.io/apysc/easing_enum.html
        """
        animation_rotation_around_point: AnimationRotationAroundPoint = \
            AnimationRotationAroundPoint(
                target=self,
                rotation_around_point=rotation_around_point,
                x=x,
                y=y,
                duration=duration,
                delay=delay,
                easing=easing)
        return animation_rotation_around_point
