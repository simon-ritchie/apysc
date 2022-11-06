"""Class implementation for the animation_fill_alpha interface.
"""

from typing import Union

from typing_extensions import final

from apysc._animation.animation_fill_alpha import AnimationFillAlpha
from apysc._animation.animation_mixins import AnimationMixIns
from apysc._animation.easing import Easing
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._validation import arg_validation_decos


class AnimationFillAlphaMixIn(AnimationMixIns):
    @final
    @arg_validation_decos.is_num(arg_position_index=1)
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=1)
    @arg_validation_decos.is_integer(arg_position_index=2)
    @arg_validation_decos.num_is_gt_zero(arg_position_index=2)
    @arg_validation_decos.is_integer(arg_position_index=3)
    @arg_validation_decos.is_easing(arg_position_index=4)
    def animation_fill_alpha(
        self,
        *,
        alpha: Union[float, Number],
        duration: Union[int, Int] = 3000,
        delay: Union[int, Int] = 0,
        easing: Easing = Easing.LINEAR
    ) -> AnimationFillAlpha:
        """
        Set the fill alpha (opacity) animation setting.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        alpha : Number or float
            The final alpha (opacity) of the animation.
        duration : Int or int, default 3000
            Milliseconds before an animation ends.
        delay : Int or int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_fill_alpha : AnimationFillAlpha
            Created animation setting instance.

        References
        ----------
        - animation_fill_alpha interface
            - https://simon-ritchie.github.io/apysc/en/animation_fill_alpha.html
        - Animation interfaces duration setting
            - https://simon-ritchie.github.io/apysc/en/animation_duration.html
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
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=50)
        >>> _ = circle.animation_y(
        ...     y=100,
        ...     duration=1500,
        ...     easing=ap.Easing.EASE_OUT_QUINT,
        ... ).start()
        """
        animation_fill_alpha: AnimationFillAlpha = AnimationFillAlpha(
            target=self, alpha=alpha, duration=duration, delay=delay, easing=easing
        )
        return animation_fill_alpha
