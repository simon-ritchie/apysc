"""Class implementation for the skew-x animation value.
"""

from typing import Generic
from typing import TypeVar
from typing import Union

from apysc._animation.animation_base import AnimationBase
from apysc._animation.easing import Easing
from apysc._type.int import Int
from apysc._type.variable_name_interface import VariableNameInterface

_T = TypeVar('_T', bound=VariableNameInterface)


class AnimationSkewX(AnimationBase[_T], Generic[_T]):
    """
    The animation class for a skew-x.

    References
    ----------
    - animation_skew_x interface document
        - https://simon-ritchie.github.io/apysc/animation_skew_x.html
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
    >>> animation: ap.AnimationSkewX = rectangle.animation_skew_x(
    ...     skew_x=50,
    ...     duration=1500,
    ...     easing=ap.Easing.EASE_OUT_QUINT,
    ... )
    >>> _ = animation.start()
    """

    _skew_x: Int
    _before_skew_x: Int
    _skew_x_diff: Int

    def __init__(
            self,
            *,
            target: _T,
            skew_x: Union[int, Int],
            duration: Union[int, Int] = 3000,
            delay: Union[int, Int] = 0,
            easing: Easing = Easing.LINEAR) -> None:
        """
        The animation class for a skew-x.

        Parameters
        ----------
        target : SkewXInterface
            A target instance of the animation target
            (e.g., `Rectangle` instance).
        skew_x : int or Int
            The final skew-x of the animation.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Raises
        ------
        TypeError
            If a specified target is not a SkewXInterface instance.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=AnimationSkewX):
            from apysc._converter import to_apysc_val_from_builtin
            from apysc._display.skew_x_interface import SkewXInterface
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            variable_name: str = expression_variables_util.\
                get_next_variable_name(type_name=var_names.ANIMATION_SKEW_X)
            target_: VariableNameInterface = target
            if isinstance(target_, SkewXInterface):
                target_._initialize_skew_x_if_not_initialized()
                self._before_skew_x = target_._skew_x
            else:
                raise TypeError(
                    'Specified `target` argument is not a SkewXInterface '
                    f'instance: {type(target_)}')
            self._skew_x = to_apysc_val_from_builtin.\
                get_copied_int_from_builtin_val(integer=skew_x)
            self._skew_x_diff = self._skew_x - self._before_skew_x
            self._set_basic_animation_settings(
                target=target,
                duration=duration,
                delay=delay,
                easing=easing)
            super(AnimationSkewX, self).__init__(variable_name=variable_name)

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
            value=self._skew_x_diff)
        return f'\n  .skew({diff_str}, 0);'

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
        from apysc._display.skew_x_interface import SkewXInterface
        expression: str = ''
        if isinstance(self._target, SkewXInterface):
            self._target._initialize_skew_x_if_not_initialized()
            expression = (
                f'{self._target._skew_x.variable_name} = '
                f'{self._skew_x.variable_name};'
            )
        return expression
