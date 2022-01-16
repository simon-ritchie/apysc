"""Class implementation for the parallel animation interface.
"""

from typing import List
from typing import Union

from apysc._animation.animation_base import AnimationBase
from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_parallel import AnimationParallel
from apysc._animation.easing import Easing
from apysc._type.int import Int


class AnimationParallelInterface(AnimationInterfaceBase):

    def animation_parallel(
            self,
            animations: List[AnimationBase],
            *,
            duration: Union[int, Int] = 3000,
            delay: Union[int, Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationParallel:
        """
        Set the parallel animation setting.

        Notes
        -----
        - To start this animation, you need to call the `start` method of
            the returned instance.
        - The `animations` argument can't contains the `AnimationParallel`
            instance.
        - The `duration`, `delay`, and `easing` arguments in the
            `animations` argument will be ignored (this interface's
            arguments will be refered instead).

        Raises
        ------
        ValueError
            - If the animations's target is not this instance.
            - If there are changed `duration`, `delay`, or
                `easing` animation settings in the `animations`
                list.

        Parameters
        ----------
        animations : list of AnimationBase
            Target animation settings.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_parallel : AnimationParallel
            Created animation setting instance.

        References
        ----------
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
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> _ = rectangle.animation_parallel(
        ...     animations=[
        ...         rectangle.animation_x(x=100),
        ...         rectangle.animation_fill_color(fill_color='#f0a'),
        ...         rectangle.animation_fill_alpha(alpha=0.5),
        ...     ],
        ...     duration=1500,
        ...     easing=ap.Easing.EASE_OUT_QUINT,
        ... ).start()
        """
        animation_parallel: AnimationParallel = AnimationParallel(
            target=self,
            animations=animations,
            duration=duration,
            delay=delay,
            easing=easing)
        return animation_parallel
