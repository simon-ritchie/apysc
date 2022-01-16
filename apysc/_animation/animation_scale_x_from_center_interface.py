"""Class implementation for the animation_scale_x_from_center
interface.
"""

from typing import Union

from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_scale_x_from_center import \
    AnimationScaleXFromCenter
from apysc._animation.easing import Easing
from apysc._type.int import Int
from apysc._type.number import Number


class AnimationScaleXFromCenterInterface(AnimationInterfaceBase):

    def animation_scale_x_from_center(
            self,
            scale_x_from_center: Union[float, Number],
            *,
            duration: Union[int, Int] = 3000,
            delay: Union[int, Int] = 0,
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
        >>> _ = rectangle.animation_scale_x_from_center(
        ...     scale_x_from_center=0.5,
        ...     duration=1500,
        ...     easing=ap.Easing.EASE_OUT_QUINT,
        ... ).start()
        """
        animation_scale_x_from_center: AnimationScaleXFromCenter = \
            AnimationScaleXFromCenter(
                target=self,
                scale_x_from_center=scale_x_from_center,
                duration=duration,
                delay=delay,
                easing=easing)
        return animation_scale_x_from_center
