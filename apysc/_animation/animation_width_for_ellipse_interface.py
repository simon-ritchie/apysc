"""Class implementation for the animation_width (for ellipse) interface.
"""

from typing import Union

from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_width_for_ellipse import \
    AnimationWidthForEllipse
from apysc._animation.easing import Easing
from apysc._type.int import Int


class AnimationWidthForEllipseInterface(AnimationInterfaceBase):

    def animation_width(
            self,
            width: Union[int, Int],
            *,
            duration: Union[int, Int] = 3000,
            delay: Union[int, Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationWidthForEllipse:
        """
        Set the ellipse-width animation setting.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        width : int or Int
            The final ellipse-width of the animation.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_width_for_ellipse : AnimationWidthForEllipse
            Created animation setting instance.

        References
        ----------
        - animation_width and animation_height interfaces document
            - https://bit.ly/39XPUdq
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
        >>> ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
        ...     x=50, y=50, width=50, height=50)
        >>> _ = ellipse.animation_width(
        ...     width=100,
        ...     duration=1500,
        ...     easing=ap.Easing.EASE_OUT_QUINT,
        ... ).start()
        """
        animation_width_for_ellipse: AnimationWidthForEllipse = \
            AnimationWidthForEllipse(
                target=self,
                width=width,
                duration=duration,
                delay=delay,
                easing=easing)
        return animation_width_for_ellipse
