"""Class implementation for the rotation around the given
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

_T = TypeVar("_T", bound=VariableNameMixIn)


class AnimationRotationAroundPoint(AnimationBase[_T], Generic[_T]):
    """
    The animation class for a rotation around the given point.

    References
    ----------
    - animation_rotation_around_point interface
        - https://simon-ritchie.github.io/apysc/en/animation_rotation_around_point.html  # noqa
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
    >>> sprite.graphics.begin_fill(color="#0af")
    >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    ...     x=50, y=50, width=50, height=50
    ... )
    >>> animation: ap.AnimationRotationAroundPoint
    >>> animation = rectangle.animation_rotation_around_point(
    ...     rotation_around_point=90,
    ...     x=ap.Int(100),
    ...     y=ap.Int(100),
    ...     duration=1500,
    ...     easing=ap.Easing.EASE_OUT_QUINT,
    ... )
    >>> _ = animation.start()
    """

    _rotation_around_point: Int
    _x: Int
    _y: Int
    _before_rotation_around_point: Int
    _rotation_around_point_diff: Int

    @final
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        *,
        target: _T,
        rotation_around_point: Union[int, Int],
        x: Union[int, Int],
        y: Union[int, Int],
        duration: Union[int, Int] = 3000,
        delay: Union[int, Int] = 0,
        easing: Easing = Easing.LINEAR,
    ) -> None:
        """
        The animation class for a rotation around the given point.

        Parameters
        ----------
        target : RotationAroundPointMixIn
            A target instance of the animation target
            (e.g., `Rectangle` instance).
        rotation_around_point : int or Int
            The final rotation around the given point of the animation.
        x : int or Int
            X-coordinate.
        y : int or Int
            Y-coordinate.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Raises
        ------
        TypeError
            If a specified target is not a RotationAroundPointMixIn
            instance.
        """
        from apysc._converter import to_apysc_val_from_builtin
        from apysc._display.rotation_around_point_mixin import RotationAroundPointMixIn
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.ANIMATION_ROTATION_AROUND_POINT
        )
        self._x = to_apysc_val_from_builtin.get_copied_int_from_builtin_val(integer=x)
        self._y = to_apysc_val_from_builtin.get_copied_int_from_builtin_val(integer=y)
        target_: VariableNameMixIn = target
        if isinstance(target_, RotationAroundPointMixIn):
            target_._initialize_rotation_around_point_if_not_initialized()
            self._before_rotation_around_point = target_.get_rotation_around_point(
                x=self._x, y=self._y
            )
        else:
            raise TypeError(
                "Specified `target` argument is not a "
                f"RotationAroundPointMixIn instance: {type(target_)}"
            )
        self._rotation_around_point = (
            to_apysc_val_from_builtin.get_copied_int_from_builtin_val(
                integer=rotation_around_point
            )
        )
        self._rotation_around_point_diff = (
            self._rotation_around_point - self._before_rotation_around_point
        )
        self._set_basic_animation_settings(
            target=target, duration=duration, delay=delay, easing=easing
        )
        super(AnimationRotationAroundPoint, self).__init__(variable_name=variable_name)

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
            value=self._rotation_around_point_diff
        )
        x_str: str = value_util.get_value_str_for_expression(value=self._x)
        y_str: str = value_util.get_value_str_for_expression(value=self._y)
        return f"\n  .rotate({diff_str}, {x_str}, {y_str});"

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
        from apysc._display import rotation_interface_helper
        from apysc._display.rotation_around_point_mixin import RotationAroundPointMixIn
        from apysc._type import value_util

        expression: str = ""
        if isinstance(self._target, RotationAroundPointMixIn):
            self._target._initialize_rotation_around_point_if_not_initialized()
            key_exp_str: str = (
                rotation_interface_helper.get_coordinates_key_for_expression(
                    x=self._x, y=self._y
                ).value
            )
            target_rotation_around_point_value_str: str = (
                value_util.get_value_str_for_expression(
                    value=self._target._rotation_around_point
                )
            )
            rotation_around_point_value_str: str = (
                value_util.get_value_str_for_expression(
                    value=self._rotation_around_point
                )
            )
            expression = (
                f"{target_rotation_around_point_value_str}"
                f"[{key_exp_str}] = "
                f"{rotation_around_point_value_str};"
            )
        return expression
