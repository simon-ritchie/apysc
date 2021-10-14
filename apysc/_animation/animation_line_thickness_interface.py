"""Class implementation for the animation_line_thickness interface.
"""

from typing import Union

import apysc as ap
from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_line_thickness import AnimationLineThickness
from apysc._animation.easing import Easing


class AnimationLineThicknessInterface(AnimationInterfaceBase):

    def animation_line_thickness(
            self,
            thickness: Union[int, ap.Int],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationLineThickness:
        """
        Set the line thickness animation setting.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        thickness : int or Int
            The final line thickness of the animation.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_line_thickness : AnimationLineThickness
            Created animation setting instance.

        References
        ----------
        - animation_line_thickness interface document
            - https://bit.ly/2YUc7XN
        - Animation interfaces duration setting document
            - https://simon-ritchie.github.io/apysc/animation_duration.html
        - Each animation interface return value document
            - https://bit.ly/2XOoa8w
        - Easing enum document
            - https://simon-ritchie.github.io/apysc/easing_enum.html
        """
        animation_line_thickness: AnimationLineThickness = \
            AnimationLineThickness(
                target=self,
                thickness=thickness,
                duration=duration,
                delay=delay,
                easing=easing)
        return animation_line_thickness
