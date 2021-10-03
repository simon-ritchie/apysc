"""Class implementation for the line alpha value.
"""

from typing import Generic
from typing import TypeVar
from typing import Union

import apysc as ap
from apysc._animation.animation_base import AnimationBase
from apysc._animation.easing import Easing
from apysc._type.variable_name_interface import VariableNameInterface

_T = TypeVar('_T', bound=VariableNameInterface)


class AnimationLineAlpha(AnimationBase[_T], Generic[_T]):
    """
    The animation class for a line alpha.
    """

    _line_alpha: ap.Number

    def __init__(
            self,
            target: _T,
            alpha: Union[float, ap.Number],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> None:
        """
        The animation class for a line alpha.

        Parameters
        ----------
        target : VariableNameInterface
            A target instance of the animation target
            (e.g., `Rectangle` instance).
        alpha : float or Number
            The final line alpha of the animation.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.
        """
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=AnimationLineAlpha):
            from apysc._converter import to_apysc_val_from_builtin
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            variable_name: str = expression_variables_util.\
                get_next_variable_name(
                    type_name=var_names.ANIMATION_LINE_ALPHA)
            self._line_alpha = to_apysc_val_from_builtin.\
                get_copied_number_from_builtin_val(float_or_num=alpha)
            self._set_basic_animation_settings(
                target=target,
                duration=duration,
                delay=delay,
                easing=easing)
            super(AnimationLineAlpha, self).__init__(
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
        line_alpha_str: str = value_util.get_value_str_for_expression(
            value=self._line_alpha)
        return f'\n  .attr({{"stroke-opacity": {line_alpha_str}}});'

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
        from apysc._display.line_alpha_interface import LineAlphaInterface
        expression: str = ''
        if isinstance(self._target, LineAlphaInterface):
            self._target._initialize_line_alpha_if_not_initialized()
            expression = (
                f'{self._target._line_alpha.variable_name} = '
                f'{self._line_alpha.variable_name};'
            )
        return expression
