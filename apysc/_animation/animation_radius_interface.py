"""Class implementation for the animation_radius interface.
"""

from typing import Union

from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_radius import AnimationRadius
from apysc._animation.easing import Easing
from apysc._type.int import Int


class AnimationRadiusInterface(AnimationInterfaceBase):

    def animation_radius(
            self,
            radius: Union[int, Int],
            *,
            duration: Union[int, Int] = 3000,
            delay: Union[int, Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationRadius:
        """
        Set the radius animation setting.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        radius : int or Int
            The final radius of the animation.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_radius : AnimationRadius
            Created animation setting instance.

        References
        ----------
        - animation_radius interface document
            - https://simon-ritchie.github.io/apysc/animation_radius.html
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
        >>> _ = circle.animation_radius(
        ...     radius=100,
        ...     duration=1500,
        ...     easing=ap.Easing.EASE_OUT_QUINT,
        ... ).start()
        """
        animation_radius: AnimationRadius = AnimationRadius(
            target=self,
            radius=radius,
            duration=duration,
            delay=delay,
            easing=easing)
        return animation_radius
