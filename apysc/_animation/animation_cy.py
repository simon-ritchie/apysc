"""Class implementation for the center-y animation value.
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


class AnimationCy(AnimationBase[_T], Generic[_T]):
    """
    The animation class for a center-y coordinate.

    References
    ----------
    - animation_y interface
        - https://simon-ritchie.github.io/apysc/en/animation_y.html
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
    >>> circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=50)
    >>> animation: ap.AnimationCy = circle.animation_y(
    ...     y=100,
    ...     duration=1500,
    ...     easing=ap.Easing.EASE_OUT_QUINT,
    ... )
    >>> _ = animation.start()
    """

    _cy: Int

    @final
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        *,
        target: _T,
        y: Union[int, Int],
        duration: Union[int, Int] = 3000,
        delay: Union[int, Int] = 0,
        easing: Easing = Easing.LINEAR,
    ) -> None:
        """
        The animation class for a center-y coordinate.

        Parameters
        ----------
        target : VariableNameMixIn
            A target instance of the animation target
            (e.g., `Circle` instance).
        y : Int or int
            Destination of the y-coordinate.
        duration : Int or int, default 3000
            Milliseconds before an animation ends.
        delay : Int or int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.
        """
        from apysc._converter import to_apysc_val_from_builtin
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.ANIMATION_CY
        )
        self._cy = to_apysc_val_from_builtin.get_copied_int_from_builtin_val(integer=y)
        self._set_basic_animation_settings(
            target=target, duration=duration, delay=delay, easing=easing
        )
        super(AnimationCy, self).__init__(variable_name=variable_name)

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

        cy_str: str = value_util.get_value_str_for_expression(value=self._cy)
        return f"\n  .cy({cy_str});"

    @final
    def _get_complete_event_in_handler_head_expression(self) -> str:
        """
        Get an expression to insert into the heading of a complete
        event handler.

        Returns
        -------
        expression : str
            An expression to insert into the heading of a complete
            event handler.
        """
        from apysc._display.cy_mixin import CyMixIn

        expression: str = ""
        if isinstance(self._target, CyMixIn):
            self._target._initialize_y_if_not_initialized()
            expression = (
                f"{self._target._y.variable_name} = " f"{self._cy.variable_name};"
            )
        return expression
