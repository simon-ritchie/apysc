"""Class implementation for the skew-y animation value.
"""

from typing import Generic
from typing import TypeVar
from typing import Union

import apysc as ap
from apysc._animation.animation_base import AnimationBase
from apysc._animation.easing import Easing
from apysc._type.variable_name_interface import VariableNameInterface

_T = TypeVar('_T', bound=VariableNameInterface)


class AnimationSkewY(AnimationBase[_T], Generic[_T]):
    """
    The animation class for a skew-y.
    """

    _skew_y: ap.Int
    _before_skew_y: ap.Int
    _skew_y_diff: ap.Int

    def __init__(
            self,
            target: _T,
            skew_y: Union[int, ap.Int],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> None:
        """
        The animation class for a skew-y.

        Parameters
        ----------
        target : SkewXInterface
            A target instance of the animation target
            (e.g., `Rectangle` instance).
        skew_y : int or Int
            The final skew-y of the animation.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Raises
        ------
        TypeError
            If a specified target is not a SkewYInterface instance.
        """
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=AnimationSkewY):
            from apysc._converter import to_apysc_val_from_builtin
            from apysc._display.skew_y_interface import SkewYInterface
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            variable_name: str = expression_variables_util.\
                get_next_variable_name(type_name=var_names.ANIMATION_SKEW_Y)
            target_: VariableNameInterface = target
            if isinstance(target_, SkewYInterface):
                target_._initialize_skew_y_if_not_initialized()
                self._before_skew_y = target_._skew_y
            else:
                raise TypeError(
                    'Specified `target` argument is not a SkewYInterface '
                    f'instance: {type(target_)}')
            self._skew_y = to_apysc_val_from_builtin.\
                get_copied_int_from_builtin_val(integer=skew_y)
            self._skew_y_diff = self._skew_y - self._before_skew_y
            self._set_basic_animation_settings(
                target=target,
                duration=duration,
                delay=delay,
                easing=easing)
            super(AnimationSkewY, self).__init__(variable_name=variable_name)

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
            value=self._skew_y_diff)
        return f'\n  .skew(0, {diff_str});'

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
        from apysc._display.skew_y_interface import SkewYInterface
        expression: str = ''
        if isinstance(self._target, SkewYInterface):
            self._target._initialize_skew_y_if_not_initialized()
            expression = (
                f'{self._target._skew_y.variable_name} = '
                f'{self._skew_y.variable_name};'
            )
        return expression
