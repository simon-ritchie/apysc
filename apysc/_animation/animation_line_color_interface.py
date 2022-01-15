"""Class implementation for the animation_line_color interface.
"""

from typing import TypeVar
from typing import Union

from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_line_color import AnimationLineColor
from apysc._animation.easing import Easing
from apysc._type.int import Int
from apysc._type.string import String

StrOrString = TypeVar('StrOrString', str, String)


class AnimationLineColorInterface(AnimationInterfaceBase):

    def animation_line_color(
            self,
            line_color: StrOrString,
            *,
            duration: Union[int, Int] = 3000,
            delay: Union[int, Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationLineColor:
        """
        Set the line color animation setting.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        line_color : str or String
            The final line color (hex color code) of the animation.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_line_color : AnimationLineColor
            Created animation setting instance.

        References
        ----------
        - animation_line_color interface document
            - https://simon-ritchie.github.io/apysc/animation_line_color.html
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
        >>> sprite.graphics.line_style(
        ...     color='#fff', thickness=5)
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> _ = rectangle.animation_line_color(
        ...     line_color='#0af',
        ...     duration=1500,
        ...     easing=ap.Easing.EASE_OUT_QUINT,
        ... ).start()
        """
        animation_line_color: AnimationLineColor = AnimationLineColor(
            target=self,
            line_color=line_color,
            duration=duration,
            delay=delay,
            easing=easing)
        return animation_line_color
