"""Class implementation for the animation_fill_alpha interface.
"""

from typing import Union

from apysc._animation.animation_fill_alpha import AnimationFillAlpha
from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.easing import Easing
from apysc._type.int import Int
from apysc._type.number import Number


class AnimationFillAlphaInterface(AnimationInterfaceBase):

    def animation_fill_alpha(
            self,
            alpha: Union[float, Number],
            *,
            duration: Union[int, Int] = 3000,
            delay: Union[int, Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationFillAlpha:
        """
        Set the fill alpha (opacity) animation setting.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        alpha : float or Number
            The final alpha (opacity) of the animation.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_fill_alpha : AnimationFillAlpha
            Created animation setting instance.

        References
        ----------
        - animation_fill_alpha interface document
            - https://simon-ritchie.github.io/apysc/animation_fill_alpha.html
        - Animation interfaces duration setting document
            - https://simon-ritchie.github.io/apysc/animation_duration.html
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
        >>> circle: ap.Circle = sprite.graphics.draw_circle(
        ...     x=100, y=100, radius=50)
        >>> _ = circle.animation_y(
        ...     y=100,
        ...     duration=1500,
        ...     easing=ap.Easing.EASE_OUT_QUINT,
        ... ).start()
        """
        animation_fill_alpha: AnimationFillAlpha = AnimationFillAlpha(
            target=self,
            alpha=alpha,
            duration=duration,
            delay=delay,
            easing=easing)
        return animation_fill_alpha
