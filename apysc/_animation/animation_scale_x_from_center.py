"""Class implementation for the scale-x animation value.
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


class AnimationScaleXFromCenter(AnimationBase[_T], Generic[_T]):
    """
    The animation class for a scale-x.

    References
    ----------
    - animation_scale_x_from_center interface document
        - https://bit.ly/30qsD2m
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
    >>> animation: ap.AnimationScaleXFromCenter
    >>> animation = rectangle.animation_scale_x_from_center(
    ...     scale_x_from_center=0.5,
    ...     duration=1500,
    ...     easing=ap.Easing.EASE_OUT_QUINT,
    ... )
    >>> _ = animation.start()
    """

    _scale_x_from_center: Number
    _before_scale_x_from_center: Number
    _scale_x_from_center_diff_ratio: Number

    def __init__(
            self,
            *,
            target: _T,
            scale_x_from_center: Union[float, Number],
            duration: Union[int, Int] = 3000,
            delay: Union[int, Int] = 0,
            easing: Easing = Easing.LINEAR) -> None:
        """
        The animation class for a scale-x.

        Parameters
        ----------
        target : SkewXInterface
            A target instance of the animation target
            (e.g., `Rectangle` instance).
        scale_x_from_center : float or Number
            The final scale-x of the animation.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Raises
        ------
        TypeError
            If a specified target is not a ScaleXFromCenterInterface
            instance.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=AnimationScaleXFromCenter):
            from apysc._converter import to_apysc_val_from_builtin
            from apysc._display.scale_x_from_center_interface import \
                ScaleXFromCenterInterface
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            variable_name: str = expression_variables_util.\
                get_next_variable_name(
                    type_name=var_names.ANIMATION_SCALE_X_FROM_CENTER)
            target_: VariableNameInterface = target
            if isinstance(target_, ScaleXFromCenterInterface):
                target_._initialize_scale_x_from_center_if_not_initialized()
                self._before_scale_x_from_center = \
                    target_._scale_x_from_center
            else:
                raise TypeError(
                    'Specified `target` argument is not a '
                    f'ScaleXFromCenterInterface instance: {type(target_)}')
            self._scale_x_from_center = to_apysc_val_from_builtin.\
                get_copied_number_from_builtin_val(
                    float_or_num=scale_x_from_center)
            one: ap.Number = ap.Number(1.0)
            self._scale_x_from_center_diff_ratio = (
                one / self._before_scale_x_from_center
                * self._scale_x_from_center)
            self._set_basic_animation_settings(
                target=target,
                duration=duration,
                delay=delay,
                easing=easing)
            super(AnimationScaleXFromCenter, self).__init__(
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
            value=self._scale_x_from_center_diff_ratio)
        return f'\n  .scale({diff_ratio_str}, 1);'

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
        from apysc._display.scale_x_from_center_interface import \
            ScaleXFromCenterInterface
        expression: str = ''
        if isinstance(self._target, ScaleXFromCenterInterface):
            self._target._initialize_scale_x_from_center_if_not_initialized()
            expression = (
                f'{self._target._scale_x_from_center.variable_name} = '
                f'{self._scale_x_from_center.variable_name};'
            )
        return expression
