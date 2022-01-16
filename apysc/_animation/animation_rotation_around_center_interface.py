"""Class implementation for the animation_rotation_aroound_center
interface.
"""

from typing import Union

from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_rotation_around_center import \
    AnimationRotationAroundCenter
from apysc._animation.easing import Easing
from apysc._type.int import Int


class AnimationRotationAroundCenterInterface(AnimationInterfaceBase):

    def animation_rotation_around_center(
            self,
            rotation_around_center: Union[int, Int],
            *,
            duration: Union[int, Int] = 3000,
            delay: Union[int, Int] = 0,
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
        - Animation interfaces delay setting document
            - https://simon-ritchie.github.io/apysc/animation_delay.html
        - Each animation interface return value document
            - https://bit.ly/2XOoa8w
        - Sequential animation setting document
            - https://simon-ritchie.github.io/apysc/sequential_animation.html
        - animation_parallel interface document
            - https://simon-ritchie.github.io/apysc/animation_parallel.html
        - Easing enum document
            - https://simon-ritchie.github.io/apysc/easing_enum.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> _ = rectangle.animation_rotation_around_center(
        ...     rotation_around_center=90,
        ...     duration=1500,
        ...     easing=ap.Easing.EASE_OUT_QUINT,
        ... ).start()
        """
        animation_rotation_around_center: AnimationRotationAroundCenter = \
            AnimationRotationAroundCenter(
                target=self,
                rotation_around_center=rotation_around_center,
                duration=duration,
                delay=delay,
                easing=easing)
        return animation_rotation_around_center
