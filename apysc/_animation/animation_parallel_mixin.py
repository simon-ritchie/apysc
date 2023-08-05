"""Class implementation for the parallel animation mix-in.
"""

from typing import List
from typing import Union

from typing_extensions import final

from apysc._animation.animation_base import AnimationBase
from apysc._animation.animation_mixins import AnimationMixIns
from apysc._animation.animation_parallel import AnimationParallel
from apysc._animation.easing import Easing
from apysc._type.int import Int
from apysc._validation import arg_validation_decos


class AnimationParallelMixIn(AnimationMixIns):
    @final
    @arg_validation_decos.are_animations(arg_position_index=1)
    @arg_validation_decos.is_integer(arg_position_index=2, optional=False)
    @arg_validation_decos.num_is_gt_zero(arg_position_index=2, optional=False)
    @arg_validation_decos.is_integer(arg_position_index=3, optional=False)
    @arg_validation_decos.is_easing(arg_position_index=4)
    def animation_parallel(
        self,
        *,
        animations: List[AnimationBase],
        duration: Union[int, Int] = 3000,
        delay: Union[int, Int] = 0,
        easing: Easing = Easing.LINEAR
    ) -> AnimationParallel:
        """
        Set the parallel animation setting.

        Notes
        -----
        - To start this animation, you need to call the `start` method of
            the returned instance.
        - The `animations` argument can't contains the `AnimationParallel`
            instance.
        - This interface ignores the duration, delay, and easing
            arguments in the `animations` argument
            (this interface uses self-arguments instead).

        Raises
        ------
        ValueError
            - If the animations' target is not this instance.
            - If there are changed duration, delay, or easing
                animation settings in the `animations` list.

        Parameters
        ----------
        animations : list of AnimationBase
            Target animation settings.
        duration : Int or int, default 3000
            Milliseconds before an animation ends.
        delay : Int or int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_parallel : AnimationParallel
            Created animation setting instance.

        References
        ----------
        - Animation interfaces duration setting
            - https://simon-ritchie.github.io/apysc/en/animation_duration.html
        - Animation interfaces delay setting
            - https://simon-ritchie.github.io/apysc/en/animation_delay.html
        - Each animation interface return value
            - https://simon-ritchie.github.io/apysc/en/animation_return_value.html  # noqa
        - Sequential animation setting
            - https://simon-ritchie.github.io/apysc/en/sequential_animation.html
        - animation_parallel interface
            - https://simon-ritchie.github.io/apysc/en/animation_parallel.html
        - Easing enum
            - https://simon-ritchie.github.io/apysc/en/easing_enum.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> _ = rectangle.animation_parallel(
        ...     animations=[
        ...         rectangle.animation_x(x=100),
        ...         rectangle.animation_fill_color(fill_color=ap.Color("#f0a")),
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
            easing=easing,
        )
        return animation_parallel
