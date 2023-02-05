"""Class implementation for the scale-x from the given point
animation value.
"""

from typing import Generic
from typing import TypeVar
from typing import Union

from typing_extensions import final

from apysc._animation.animation_base import AnimationBase
from apysc._animation.easing import Easing
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.variable_name_mixin import VariableNameMixIn

_Target = TypeVar("_Target", bound=VariableNameMixIn)


class AnimationScaleXFromPoint(AnimationBase[_Target], Generic[_Target]):
    """
    The animation class for a scale-x from the given point.

    References
    ----------
    - animation_scale_x_from_point interface
        - https://simon-ritchie.github.io/apysc/en/animation_scale_x_and_y_from_point.html  # noqa
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
    >>> animation: ap.AnimationScaleXFromPoint
    >>> animation = rectangle.animation_scale_x_from_point(
    ...     scale_x_from_point=0.5,
    ...     x=ap.Number(100),
    ...     duration=1500,
    ...     easing=ap.Easing.EASE_OUT_QUINT,
    ... )
    >>> _ = animation.start()
    """

    _scale_x_from_point: Number
    _x: Number
    _before_scale_x_from_point: Number
    _scale_x_from_point_diff_ratio: Number

    @final
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        *,
        target: _Target,
        scale_x_from_point: Union[float, Number],
        x: Union[float, Number],
        duration: Union[int, Int] = 3000,
        delay: Union[int, Int] = 0,
        easing: Easing = Easing.LINEAR,
    ) -> None:
        """
        The animation class for a scale-x from the given point.

        Parameters
        ----------
        target : ScaleXFromPointMixIn
            A target instance of the animation target
            (e.g., `Rectangle` instance).
        scale_x_from_point : float or Number
            The final scale-x from the given point of the animation.
        x : float or Number
            X-coordinate.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Raises
        ------
        TypeError
            If a specified target is not a ScaleXFromPointMixIn
            instance.
        """
        import apysc as ap
        from apysc._converter import to_apysc_val_from_builtin
        from apysc._display.scale_x_from_point_mixin import ScaleXFromPointMixIn
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.ANIMATION_SCALE_X_FROM_POINT
        )
        self._x = to_apysc_val_from_builtin.get_copied_number_from_builtin_val(
            float_or_num=x
        )
        target_: VariableNameMixIn = target
        if isinstance(target_, ScaleXFromPointMixIn):
            target_._initialize_scale_x_from_point_if_not_initialized()
            self._before_scale_x_from_point = target_.get_scale_x_from_point(x=self._x)
        else:
            raise TypeError(
                "Specified `target` argument is not a "
                f"ScaleXFromPointMixIn: {type(target_)}"
            )
        self._scale_x_from_point = (
            to_apysc_val_from_builtin.get_copied_number_from_builtin_val(
                float_or_num=scale_x_from_point
            )
        )
        one: ap.Number = ap.Number(1.0)
        self._scale_x_from_point_diff_ratio = (
            one / self._before_scale_x_from_point * self._scale_x_from_point
        )
        self._set_basic_animation_settings(
            target=target, duration=duration, delay=delay, easing=easing
        )
        super(AnimationScaleXFromPoint, self).__init__(variable_name=variable_name)

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

        diff_ratio_str: str = value_util.get_value_str_for_expression(
            value=self._scale_x_from_point_diff_ratio
        )
        x_str: str = value_util.get_value_str_for_expression(value=self._x)
        return f"\n  .scale({diff_ratio_str}, 1, {x_str}, 0);"

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
        from apysc._display import scale_interface_helper
        from apysc._display.scale_x_from_point_mixin import ScaleXFromPointMixIn
        from apysc._type import value_util

        expression: str = ""
        if isinstance(self._target, ScaleXFromPointMixIn):
            self._target._initialize_scale_x_from_point_if_not_initialized()
            key_exp_str: str = scale_interface_helper.get_coordinate_key_for_expression(
                coordinate=self._x
            ).value
            target_scale_x_str: str = value_util.get_value_str_for_expression(
                value=self._target._scale_x_from_point
            )
            scale_x_str: str = value_util.get_value_str_for_expression(
                value=self._scale_x_from_point
            )
            expression = f"{target_scale_x_str}[{key_exp_str}] = " f"{scale_x_str};"
        return expression
