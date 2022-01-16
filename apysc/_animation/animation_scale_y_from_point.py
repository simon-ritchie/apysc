"""Class implementation for the scale-y from the given point
animation value.
"""

from typing import Generic
from typing import TypeVar
from typing import Union

from apysc._animation.animation_base import AnimationBase
from apysc._animation.easing import Easing
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.variable_name_interface import VariableNameInterface

_T = TypeVar('_T', bound=VariableNameInterface)


class AnimationScaleYFromPoint(AnimationBase[_T], Generic[_T]):
    """
    The animation class for a scale-y from the given point.

    References
    ----------
    - animation_scale_from_point interfaces document
        - https://bit.ly/3j3It9o
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
    >>> animation: ap.AnimationScaleYFromPoint
    >>> animation = rectangle.animation_scale_y_from_point(
    ...     scale_y_from_point=0.5,
    ...     y=ap.Int(100),
    ...     duration=1500,
    ...     easing=ap.Easing.EASE_OUT_QUINT,
    ... )
    >>> _ = animation.start()
    """

    _scale_y_from_point: Number
    _y: Int
    _before_scale_y_from_point: Number
    _scale_y_from_point_diff_ratio: Number

    def __init__(
            self,
            *,
            target: _T,
            scale_y_from_point: Union[float, Number],
            y: Union[int, Int],
            duration: Union[int, Int] = 3000,
            delay: Union[int, Int] = 0,
            easing: Easing = Easing.LINEAR) -> None:
        """
        The animation class for a scale-y from the given point.

        Parameters
        ----------
        target : ScaleYFromPointInterface
            A target instance of the animation target
            (e.g., `Rectangle` instance).
        scale_y_from_point : float or Number
            The final scale-y from the given point of the animation.
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
            If a specified target is not a ScaleXFromPointInterface
            instance.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=AnimationScaleYFromPoint):
            from apysc._converter import to_apysc_val_from_builtin
            from apysc._display.scale_y_from_point_interface import \
                ScaleYFromPointInterface
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            variable_name: str = expression_variables_util.\
                get_next_variable_name(
                    type_name=var_names.ANIMATION_SCALE_Y_FROM_POINT)
            self._y = to_apysc_val_from_builtin.\
                get_copied_int_from_builtin_val(integer=y)
            target_: VariableNameInterface = target
            if isinstance(target_, ScaleYFromPointInterface):
                target_._initialize_scale_y_from_point_if_not_initialized()
                self._before_scale_y_from_point = target_.\
                    get_scale_y_from_point(y=self._y)
            else:
                raise TypeError(
                    'Specified `target` argument is not a '
                    f'ScaleYFromPointInterface: {type(target_)}')
            self._scale_y_from_point = to_apysc_val_from_builtin.\
                get_copied_number_from_builtin_val(
                    float_or_num=scale_y_from_point)
            one: ap.Number = ap.Number(1.0)
            self._scale_y_from_point_diff_ratio = (
                one / self._before_scale_y_from_point
                * self._scale_y_from_point)
            self._set_basic_animation_settings(
                target=target,
                duration=duration,
                delay=delay,
                easing=easing)
            super(AnimationScaleYFromPoint, self).__init__(
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
            value=self._scale_y_from_point_diff_ratio)
        y_str: str = value_util.get_value_str_for_expression(value=self._y)
        return f'\n  .scale(1, {diff_ratio_str}, 0, {y_str});'

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
        from apysc._display.scale_y_from_point_interface import \
            ScaleYFromPointInterface
        from apysc._type import value_util
        expression: str = ''
        if isinstance(self._target, ScaleYFromPointInterface):
            self._target._initialize_scale_y_from_point_if_not_initialized()
            key_exp_str: str = scale_interface_helper.\
                get_coordinate_key_for_expression(coordinate=self._y).value
            target_scale_y_str: str = value_util.get_value_str_for_expression(
                value=self._target._scale_y_from_point)
            scale_y_str: str = value_util.get_value_str_for_expression(
                value=self._scale_y_from_point)
            expression = (
                f'{target_scale_y_str}[{key_exp_str}] = '
                f'{scale_y_str};'
            )
        return expression
