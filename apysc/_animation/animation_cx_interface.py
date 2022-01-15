"""Class implementation for the animation_x interface
(using center-x coordinate internally).
"""

from typing import Union

from apysc._animation.animation_cx import AnimationCx
from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.easing import Easing
from apysc._type.int import Int


class AnimationCxInterface(AnimationInterfaceBase):

    def animation_x(
            self,
            x: Union[int, Int],
            *,
            duration: Union[int, Int] = 3000,
            delay: Union[int, Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationCx:
        """
        Set the center-x coordinate animation setting.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        x : int or Int
            Destination of the center-x coordinate.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_cx : AnimationCx
            Created animation setting instance.

        References
        ----------
        - animation_x interface document
            - https://simon-ritchie.github.io/apysc/animation_x.html
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
        >>> circle: ap.Circle = sprite.graphics.draw_circle(
        ...     x=100, y=100, radius=50)
        >>> _ = circle.animation_x(
        ...     x=100,
        ...     duration=1500,
        ...     easing=ap.Easing.EASE_OUT_QUINT,
        ... ).start()
        """
        animation_cx: AnimationCx = AnimationCx(
            target=self,
            x=x,
            duration=duration,
            delay=delay,
            easing=easing)
        return animation_cx
