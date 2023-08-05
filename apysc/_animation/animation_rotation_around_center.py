"""Class implementation for the rotation around the center
point animation value.
"""

from typing import Generic
from typing import TypeVar
from typing import Union

from typing_extensions import final

from apysc._animation.animation_base import AnimationBase
from apysc._animation.easing import Easing
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.variable_name_mixin import VariableNameMixIn

_Target = TypeVar("_Target", bound=VariableNameMixIn)


class AnimationRotationAroundCenter(AnimationBase[_Target], Generic[_Target]):
    """
    The animation class for a rotation around the center point.

    References
    ----------
    - animation_rotation_around_center interface
        - https://simon-ritchie.github.io/apysc/en/animation_rotation_around_center.html  # noqa
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
    >>> animation: ap.AnimationRotationAroundCenter
    >>> animation = rectangle.animation_rotation_around_center(
    ...     rotation_around_center=90,
    ...     duration=1500,
    ...     easing=ap.Easing.EASE_OUT_QUINT,
    ... )
    >>> _ = animation.start()
    """

    _rotation_around_center: Int
    _before_rotation_around_center: Int
    _rotation_around_center_diff: Int

    @final
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        *,
        target: _Target,
        rotation_around_center: Union[int, Int],
        duration: Union[int, Int] = 3000,
        delay: Union[int, Int] = 0,
        easing: Easing = Easing.LINEAR,
    ) -> None:
        """
        The animation class for a rotation around the center point.

        Parameters
        ----------
        target : SkewXMixIn
            A target instance of the animation target
            (e.g., `Rectangle` instance).
        rotation_around_center : Int or int
            The final rotation around the center point of the animation.
        duration : Int or int, default 3000
            Milliseconds before an animation ends.
        delay : Int or int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Raises
        ------
        TypeError
            If a specified target is not a RotationAroundCenterMixIn
            instance.
        """
        from apysc._converter import to_apysc_val_from_builtin
        from apysc._display.rotation_around_center_mixin import (
            RotationAroundCenterMixIn,
        )
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.ANIMATION_ROTATION_AROUND_CENTER
        )
        target_: VariableNameMixIn = target
        if isinstance(target_, RotationAroundCenterMixIn):
            target_._initialize_rotation_around_center_if_not_initialized()
            self._before_rotation_around_center = target_._rotation_around_center
        else:
            raise TypeError(
                "Specified `target` argument is not a "
                "RotationAroundCenterMixIn instance: "
                f"{type(target_)}"
            )
        self._rotation_around_center = (
            to_apysc_val_from_builtin.get_copied_int_from_builtin_val(
                integer=rotation_around_center
            )
        )
        self._rotation_around_center_diff = (
            self._rotation_around_center - self._before_rotation_around_center
        )
        self._set_basic_animation_settings(
            target=target, duration=duration, delay=delay, easing=easing
        )
        super(AnimationRotationAroundCenter, self).__init__(variable_name=variable_name)

    @final
    def _get_animation_func_expression(self) -> str:
        """
        Get a animation function expression.

        Returns
        -------
        expression : str
            Animation function expression.
        """
        from apysc._type import value_util

        diff_str: str = value_util.get_value_str_for_expression(
            value=self._rotation_around_center_diff
        )
        return f"\n  .rotate({diff_str});"

    @final
    def _get_complete_event_in_handler_head_expression(self) -> str:
        """
        Get an expression to be inserted into the complete event
        handler's head.

        Returns
        -------
        expression : str
            An expression to insert into the complete event
            handler's head.
        """
        from apysc._display.rotation_around_center_mixin import (
            RotationAroundCenterMixIn,
        )

        expression: str = ""
        if isinstance(self._target, RotationAroundCenterMixIn):
            self._target._initialize_rotation_around_center_if_not_initialized()
            expression = (
                f"{self._target._rotation_around_center.variable_name} = "
                f"{self._rotation_around_center.variable_name};"
            )
        return expression
