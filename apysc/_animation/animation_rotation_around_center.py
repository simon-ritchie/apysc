"""Class implementation for the rotation around the center
point animation value.
"""

from typing import Generic
from typing import TypeVar
from typing import Union

import apysc as ap
from apysc._animation.animation_base import AnimationBase
from apysc._animation.easing import Easing
from apysc._type.variable_name_interface import VariableNameInterface

_T = TypeVar('_T', bound=VariableNameInterface)


class AnimationRotationAroundCenter(AnimationBase[_T], Generic[_T]):
    """
    The animation class for a rotation around the center point.
    """

    _rotation_around_center: ap.Int
    _before_rotation_around_center: ap.Int
    _rotation_around_center_diff: ap.Int

    def __init__(
            self,
            target: _T,
            rotation_around_center: Union[int, ap.Int],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> None:
        """
        The animation class for a rotation around the center point.

        Parameters
        ----------
        target : SkewXInterface
            A target instance of the animation target
            (e.g., `Rectangle` instance).
        rotation_around_center : int or Int
            The final rotation around the center point of the animation.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Raises
        ------
        TypeError
            If a specified target is not a RotationAroundCenterInterface
            instance.
        """
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=AnimationRotationAroundCenter):
            from apysc._converter import to_apysc_val_from_builtin
            from apysc._display.rotation_around_center_interface import \
                RotationAroundCenterInterface
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            variable_name: str = expression_variables_util.\
                get_next_variable_name(
                    type_name=var_names.ANIMATION_ROTATION_AROUND_CENTER)
            target_: VariableNameInterface = target
            if isinstance(target_, RotationAroundCenterInterface):
                target_.\
                    _initialize_rotation_around_center_if_not_initialized()
                self._before_rotation_around_center = \
                    target_._rotation_around_center
            else:
                raise TypeError(
                    'Specified `target` argument is not a '
                    'RotationAroundCenterInterface instance: '
                    f'{type(target_)}')
            self._rotation_around_center = to_apysc_val_from_builtin.\
                get_copied_int_from_builtin_val(
                    integer=rotation_around_center)
            self._rotation_around_center_diff = self._rotation_around_center \
                - self._before_rotation_around_center
            self._set_basic_animation_settings(
                target=target,
                duration=duration,
                delay=delay,
                easing=easing)
            super(AnimationRotationAroundCenter, self).__init__(
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
        diff_str: str = value_util.get_value_str_for_expression(
            value=self._rotation_around_center_diff)
        return f'\n  .rotate({diff_str});'

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
        from apysc._display.rotation_around_center_interface import \
            RotationAroundCenterInterface
        expression: str = ''
        if isinstance(self._target, RotationAroundCenterInterface):
            self._target.\
                _initialize_rotation_around_center_if_not_initialized()
            expression = (
                f'{self._target._rotation_around_center.variable_name} = '
                f'{self._rotation_around_center.variable_name};'
            )
        return expression
