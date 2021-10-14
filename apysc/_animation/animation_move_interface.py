"""Class implementations for the animation_move interface.
"""

from typing import Union

import apysc as ap
from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_move import AnimationMove
from apysc._animation.easing import Easing


class AnimationMoveInterface(AnimationInterfaceBase):

    def animation_move(
            self,
            x: Union[int, ap.Int],
            y: Union[int, ap.Int],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationMove:
        """
        Set the x and y coordinates animation settings.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        x : int or Int
            Destination of the x-coordinate.
        y : int or Int
            Destination of the y-coordinate.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_move : AnimationMove
            Created animation setting instance.

        References
        ----------
        - animation_move interface document
            - https://simon-ritchie.github.io/apysc/animation_move.html
        - Animation interfaces duration setting document
            - https://simon-ritchie.github.io/apysc/animation_duration.html
        - Each animation interface return value document
            - https://bit.ly/2XOoa8w
        - Easing enum document
            - https://simon-ritchie.github.io/apysc/easing_enum.html
        """
        animation_move: AnimationMove = AnimationMove(
            target=self,
            x=x,
            y=y,
            duration=duration,
            delay=delay,
            easing=easing)
        return animation_move
