"""Class implementation for the fill alpha animation value.
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


class AnimationFillAlpha(AnimationBase[_T], Generic[_T]):
    """
    The animation class for a fill alpha (opacity).

    References
    ----------
    - animation_fill_alpha interface document
        - https://simon-ritchie.github.io/apysc/animation_fill_alpha.html
    - Animation interfaces duration setting document
        - https://simon-ritchie.github.io/apysc/animation_duration.html
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
    >>> animation: ap.AnimationFillAlpha = rectangle.animation_fill_alpha(
    ...     alpha=0.5,
    ...     duration=1500,
    ...     easing=ap.Easing.EASE_OUT_QUINT,
    ... )
    >>> _ = animation.start()
    """

    _fill_alpha: Number

    def __init__(
            self,
            *,
            target: _T,
            alpha: Union[float, Number],
            duration: Union[int, Int] = 3000,
            delay: Union[int, Int] = 0,
            easing: Easing = Easing.LINEAR) -> None:
        """
        The animation class for a fill alpha (opacity).

        Parameters
        ----------
        target : VariableNameInterface
            A target instance of the animation target
            (e.g., `Rectangle` instance).
        alpha : float or Number
            The final fill alpha (opacity) of the animation.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=AnimationFillAlpha):
            from apysc._converter import to_apysc_val_from_builtin
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            variable_name: str = expression_variables_util.\
                get_next_variable_name(
                    type_name=var_names.ANIMATION_FILL_ALPHA)
            self._fill_alpha = to_apysc_val_from_builtin.\
                get_copied_number_from_builtin_val(float_or_num=alpha)
            self._set_basic_animation_settings(
                target=target,
                duration=duration,
                delay=delay,
                easing=easing)
            super(AnimationFillAlpha, self).__init__(
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
        fill_alpha_str: str = value_util.get_value_str_for_expression(
            value=self._fill_alpha)
        return f'\n  .attr({{"fill-opacity": {fill_alpha_str}}});'

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
        from apysc._display.fill_alpha_interface import FillAlphaInterface
        expression: str = ''
        if isinstance(self._target, FillAlphaInterface):
            self._target._initialize_fill_alpha_if_not_initialized()
            expression = (
                f'{self._target._fill_alpha.variable_name} = '
                f'{self._fill_alpha.variable_name};'
            )
        return expression
