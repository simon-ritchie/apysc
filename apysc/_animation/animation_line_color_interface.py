"""Class implementation for the animation_line_color interface.
"""

from typing import TypeVar
from typing import Union

import apysc as ap
from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_line_color import AnimationLineColor
from apysc._animation.easing import Easing

StrOrString = TypeVar('StrOrString', str, ap.String)


class AnimationLineColorInterface(AnimationInterfaceBase):

    def animation_line_color(
            self,
            line_color: StrOrString,
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationLineColor:
        """
        Set the line color animation setting.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        line_color : str or string
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
        - Each animation interface return value document
            - https://bit.ly/2XOoa8w
        - Easing enum document
            - https://simon-ritchie.github.io/apysc/easing_enum.html
        """
        animation_line_color: AnimationLineColor = AnimationLineColor(
            target=self,
            line_color=line_color,
            duration=duration,
            delay=delay,
            easing=easing)
        return animation_line_color
