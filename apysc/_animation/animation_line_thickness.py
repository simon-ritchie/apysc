"""Class implementation for the line thickness animation value.
"""

from typing import Generic
from typing import TypeVar
from typing import Union

from apysc._animation.animation_base import AnimationBase
from apysc._animation.easing import Easing
from apysc._type.int import Int
from apysc._type.variable_name_interface import VariableNameInterface

_T = TypeVar('_T', bound=VariableNameInterface)


class AnimationLineThickness(AnimationBase[_T], Generic[_T]):
    """
    The animation class for a line thickness.

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.begin_fill(color='#0af')
    >>> sprite.graphics.line_style(
    ...     color='#fff', thickness=1)
    >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    ...     x=50, y=50, width=50, height=50)
    >>> animation: ap.AnimationLineThickness
    >>> animation = rectangle.animation_line_thickness(
    ...     thickness=6,
    ...     duration=1500,
    ...     easing=ap.Easing.EASE_OUT_QUINT,
    ... )
    >>> _ = animation.start()
    """

    _line_thickness: Int

    def __init__(
            self,
            *,
            target: _T,
            thickness: Union[int, Int],
            duration: Union[int, Int] = 3000,
            delay: Union[int, Int] = 0,
            easing: Easing = Easing.LINEAR) -> None:
        """
        The animation class for a line thickness.

        Parameters
        ----------
        target : VariableNameInterface
            A target instance of the animation target
            (e.g., `Rectangle` instance).
        thickness : int or Int
            The final line thickness of the animation.
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
                module_name=__name__, class_=AnimationLineThickness):
            from apysc._converter import to_apysc_val_from_builtin
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            variable_name: str = expression_variables_util.\
                get_next_variable_name(
                    type_name=var_names.ANIMATION_LINE_THICKNESS)
            self._line_thickness = to_apysc_val_from_builtin.\
                get_copied_int_from_builtin_val(integer=thickness)
            self._set_basic_animation_settings(
                target=target,
                duration=duration,
                delay=delay,
                easing=easing)
            super(AnimationLineThickness, self).__init__(
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
        line_thickness_str: str = value_util.get_value_str_for_expression(
            value=self._line_thickness)
        return f'\n  .attr({{"stroke-width": {line_thickness_str}}});'

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
        from apysc._display.line_thickness_interface import \
            LineThicknessInterface
        expression: str = ''
        if isinstance(self._target, LineThicknessInterface):
            self._target._initialize_line_thickness_if_not_initialized()
            expression = (
                f'{self._target._line_thickness.variable_name} = '
                f'{self._line_thickness.variable_name};'
            )
        return expression
