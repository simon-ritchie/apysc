"""Class implementation for the radius animation value.
"""

from typing import Generic
from typing import TypeVar
from typing import Union

from apysc._animation.animation_base import AnimationBase
from apysc._animation.easing import Easing
from apysc._type.int import Int
from apysc._type.variable_name_interface import VariableNameInterface

_T = TypeVar('_T', bound=VariableNameInterface)


class AnimationRadius(AnimationBase[_T], Generic[_T]):
    """
    The animation class for a radius.

    References
    ----------
    - animation_radius interface document
        - https://simon-ritchie.github.io/apysc/animation_radius.html
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
    >>> circle: ap.Circle = sprite.graphics.draw_circle(
    ...     x=100, y=100, radius=50)
    >>> animation: ap.AnimationRadius = circle.animation_radius(
    ...     radius=100,
    ...     duration=1500,
    ...     easing=ap.Easing.EASE_OUT_QUINT,
    ... )
    >>> _ = animation.start()
    """

    _radius: Int

    def __init__(
            self,
            *,
            target: _T,
            radius: Union[int, Int],
            duration: Union[int, Int] = 3000,
            delay: Union[int, Int] = 0,
            easing: Easing = Easing.LINEAR) -> None:
        """
        The animation class for a radius.

        Parameters
        ----------
        target : VariableNameInterface
            A target instance of the animation target
            (e.g., `Circle` instance).
        radius : int or Int
            The final radius of the animation.
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
                module_name=__name__, class_=AnimationRadius):
            from apysc._converter import to_apysc_val_from_builtin
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            variable_name: str = expression_variables_util.\
                get_next_variable_name(type_name=var_names.ANIMATION_RADIUS)
            self._radius = to_apysc_val_from_builtin.\
                get_copied_int_from_builtin_val(integer=radius)
            self._set_basic_animation_settings(
                target=target,
                duration=duration,
                delay=delay,
                easing=easing)
            super(AnimationRadius, self).__init__(variable_name=variable_name)

    def _get_animation_func_expression(self) -> str:
        """
        Get a animation function expression.

        Returns
        -------
        expression : str
            Animation function expression.
        """
        from apysc._type import value_util
        radius_str: str = value_util.get_value_str_for_expression(
            value=self._radius)
        return f'\n  .attr({{"r": {radius_str}}});'

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
        from apysc._display.radius_interface import RadiusInterface
        expression: str = ''
        if isinstance(self._target, RadiusInterface):
            self._target._initialize_radius_if_not_initialized()
            expression = (
                f'{self._target._radius.variable_name} = '
                f'{self._radius.variable_name};'
            )
        return expression
