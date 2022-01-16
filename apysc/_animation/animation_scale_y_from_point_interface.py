"""Class implementation for the animation_scale_y_from_point
interface.
"""

from typing import Union

from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_scale_y_from_point import \
    AnimationScaleYFromPoint
from apysc._animation.easing import Easing
from apysc._type.int import Int
from apysc._type.number import Number


class AnimationScaleYFromPointInterface(AnimationInterfaceBase):

    def animation_scale_y_from_point(
            self,
            scale_y_from_point: Union[float, Number],
            y: Union[int, Int],
            *,
            duration: Union[int, Int] = 3000,
            delay: Union[int, Int] = 0,
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
        >>> _ = rectangle.animation_scale_y_from_point(
        ...     scale_y_from_point=0.5,
        ...     y=ap.Int(100),
        ...     duration=1500,
        ...     easing=ap.Easing.EASE_OUT_QUINT,
        ... ).start()
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
