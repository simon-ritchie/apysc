"""Class implementation for the animation_radius interface.
"""

from typing import Union

import apysc as ap
from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_radius import AnimationRadius
from apysc._animation.easing import Easing


class AnimationRadiusInterface(AnimationInterfaceBase):

    def animation_radius(
            self,
            radius: Union[int, ap.Int],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
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
        - Each animation interface return value document
            - https://bit.ly/2XOoa8w
        - Easing enum document
            - https://simon-ritchie.github.io/apysc/easing_enum.html
        """
        animation_radius: AnimationRadius = AnimationRadius(
            target=self,
            radius=radius,
            duration=duration,
            delay=delay,
            easing=easing)
        return animation_radius
