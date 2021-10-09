"""Class implementation for the scale-x from the given point
animation value.
"""

from typing import Generic
from typing import TypeVar
from typing import Union

import apysc as ap
from apysc._animation.animation_base import AnimationBase
from apysc._animation.easing import Easing
from apysc._type.variable_name_interface import VariableNameInterface

_T = TypeVar('_T', bound=VariableNameInterface)


class AnimationScaleXFromPoint(AnimationBase[_T], Generic[_T]):
    """
    The animation class for a scale-x from the given point.
    """

    _scale_x_from_point: ap.Number
    _x: ap.Int
    _before_scale_x_from_point: ap.Number
    _scale_x_from_point_diff_ratio: ap.Number

    def __init__(
            self,
            target: _T,
            scale_x_from_point: Union[float, ap.Number],
            x: Union[int, ap.Int],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> None:
        """
        The animation class for a scale-x from the given point.

        Parameters
        ----------
        target : ScaleXFromPointInterface
            A target instance of the animation target
            (e.g., `Rectangle` instance).
        scale_x_from_point : float or Number
            The final scale-x from the given point of the animation.
        x : int or Int
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
            If a specified target is not a ScaleXFromPointInterface
            instance.
        """
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=AnimationScaleXFromPoint):
            from apysc._converter import to_apysc_val_from_builtin
            from apysc._display.scale_x_from_point_interface import \
                ScaleXFromPointInterface
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            variable_name: str = expression_variables_util.\
                get_next_variable_name(
                    type_name=var_names.ANIMATION_SCALE_X_FROM_POINT)
            self._x = to_apysc_val_from_builtin.\
                get_copied_int_from_builtin_val(integer=x)
            target_: VariableNameInterface = target
            if isinstance(target_, ScaleXFromPointInterface):
                target_._initialize_scale_x_from_point_if_not_initialized()
                self._before_scale_x_from_point = target_.\
                    get_scale_x_from_point(x=self._x)
            else:
                raise TypeError(
                    'Specified `target` argument is not a '
                    f'ScaleXFromPointInterface: {type(target_)}')
            self._scale_x_from_point = to_apysc_val_from_builtin.\
                get_copied_number_from_builtin_val(
                    float_or_num=scale_x_from_point)
            one: ap.Number = ap.Number(1.0)
            self._scale_x_from_point_diff_ratio = (
                one / self._before_scale_x_from_point
                * self._scale_x_from_point)
            self._set_basic_animation_settings(
                target=target,
                duration=duration,
                delay=delay,
                easing=easing)
            super(AnimationScaleXFromPoint, self).__init__(
                variable_name=variable_name)

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
            value=self._scale_x_from_point_diff_ratio)
        x_str: str = value_util.get_value_str_for_expression(value=self._x)
        return f'\n  .scale({diff_ratio_str}, 1, {x_str}, 0);'

    def _get_complete_event_in_handler_head_expression(self) -> str:
        """
        Get an expression to be inserted into the complete event
        handler's head.

        Returns
        -------
        expression : str
            An expression to be inserted into the complete event
            handler's head.
        """
        from apysc._display import scale_interface_helper
        from apysc._display.scale_x_from_point_interface import \
            ScaleXFromPointInterface
        from apysc._type import value_util
        expression: str = ''
        if isinstance(self._target, ScaleXFromPointInterface):
            self._target._initialize_scale_x_from_point_if_not_initialized()
            key_exp_str: str = scale_interface_helper.\
                get_coordinate_key_for_expression(coordinate=self._x).value
            target_scale_x_str: str = value_util.get_value_str_for_expression(
                value=self._target._scale_x_from_point)
            scale_x_str: str = value_util.get_value_str_for_expression(
                value=self._scale_x_from_point)
            expression = (
                f'{target_scale_x_str}[{key_exp_str}] = '
                f'{scale_x_str};'
            )
        return expression
