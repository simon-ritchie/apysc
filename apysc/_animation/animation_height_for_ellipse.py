"""Class implementation for the ellipse-height animation value.
"""

from typing import Generic
from typing import TypeVar
from typing import Union

import apysc as ap
from apysc._animation.animation_base import AnimationBase
from apysc._animation.easing import Easing
from apysc._type.variable_name_interface import VariableNameInterface

_T = TypeVar('_T', bound=VariableNameInterface)


class AnimationHeightForEllipse(AnimationBase[_T], Generic[_T]):
    """
    The animation class for a ellipse-height.
    """

    _height: ap.Int

    def __init__(
            self,
            target: _T,
            height: Union[int, ap.Int],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> None:
        """
        The animation class for a ellipse-height.

        Parameters
        ----------
        target : VariableNameInterface
            A target instance of the animation target
            (e.g., `Ellipse` instance).
        height : int or Int
            The final ellipse-height of the animation.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.
        """
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=AnimationHeightForEllipse):
            from apysc._converter import to_apysc_val_from_builtin
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            variable_name: str = expression_variables_util.\
                get_next_variable_name(
                    type_name=var_names.ANIMATION_HEIGHT_FOR_ELLIPSE)
            self._height = to_apysc_val_from_builtin.\
                get_copied_int_from_builtin_val(integer=height)
            self._set_basic_animation_settings(
                target=target,
                duration=duration,
                delay=delay,
                easing=easing)
            super(AnimationHeightForEllipse, self).__init__(
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
        height_str: str = value_util.get_value_str_for_expression(
            value=self._height)
        return f'\n  .attr({{ry: parseInt({height_str} / 2)}});'

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
        from apysc._display.width_and_height_interfaces_for_ellipse import \
            WidthAndHeightInterfacesForEllipse
        expression: str = ''
        if isinstance(self._target, WidthAndHeightInterfacesForEllipse):
            self._target._initialize_width_and_height_if_not_initialized()
            expression = (
                f'{self._target._height.variable_name} = '
                f'{self._height.variable_name};'
            )
        return expression
