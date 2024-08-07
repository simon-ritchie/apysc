"""Class implementations for the animation_move interface.
"""

from typing import Optional
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
            easing: Optional[Easing] = None) -> AnimationMove:
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
        easing : Easing or None, default None
            Easing setting. If None, Linear calculation is used.

        Returns
        -------
        animation_move : AnimationMove
            Created animation setting instance.
        """
        animation_move: AnimationMove = AnimationMove(
            target=self,
            x=x,
            y=y,
            duration=duration,
            delay=delay,
            easing=easing)
        return animation_move
