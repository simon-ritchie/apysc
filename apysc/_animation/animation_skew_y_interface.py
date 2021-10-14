"""Class implementation for the animation_skew_y interface.
"""

import warnings
from typing import Union

import apysc as ap
from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_skew_y import AnimationSkewY
from apysc._animation.easing import Easing


class AnimationSkewYInterface(AnimationInterfaceBase):

    def _animation_skew_y(
            self,
            skew_y: Union[int, ap.Int],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationSkewY:
        """
        **Important notes**
        Currently this interface does not work correctly.
        For more details please see:
        https://github.com/svgdotjs/svg.js/issues/1222

        Set the skew-y animation animation.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        skew_y : int or Int
            The final skew-y of the animation.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_skew_y : AnimationSkewY
            Created animation setting instance.

        References
        ----------
        - Animation interfaces duration setting document
            - https://simon-ritchie.github.io/apysc/animation_duration.html
        - Each animation interface return value document
            - https://bit.ly/2XOoa8w
        - Easing enum document
            - https://simon-ritchie.github.io/apysc/easing_enum.html
        """
        warnings.warn(
            'Currently the `animation_skew_y` interface does not '
            'work correctly. Maybe this issue will be fixed in future '
            'versions. For more details, please see '
            'https://github.com/svgdotjs/svg.js/issues/1222')
        animation_skew_y: AnimationSkewY = AnimationSkewY(
            target=self,
            skew_y=skew_y,
            duration=duration,
            delay=delay,
            easing=easing)
        return animation_skew_y
