"""Class implementation for the ellipse-width animation value.
"""

from typing import Dict
from typing import Generic
from typing import TypeVar
from typing import Union

import apysc as ap
from apysc._animation.animation_base import AnimationBase
from apysc._animation.easing import Easing
from apysc._type.variable_name_interface import VariableNameInterface

_T = TypeVar('_T', bound=VariableNameInterface)


class AnimationWidthForEllipse(AnimationBase[_T], Generic[_T]):
    """
    The animation class for a ellipse-width.
    """

    _ellipse_width: ap.Int

    def __init__(
            self,
            target: _T,
            ellipse_width: Union[int, ap.Int],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> None:
        """
        The animation class for a ellipse-width.

        Parameters
        ----------
        target : VariableNameInterface
            A target instance of the animation target
            (e.g., `Ellipse` instance).
        ellipse_width : int or Int
            The final ellipse-width of the animation.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.
        """
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=AnimationWidthForEllipse):
            from apysc._converter import to_apysc_val_from_builtin
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            variable_name: str = expression_variables_util.\
                get_next_variable_name(
                    type_name=var_names.ANIMATION_WIDTH_FOR_ELLIPSE)
            self._ellipse_width = to_apysc_val_from_builtin.\
                get_copied_int_from_builtin_val(integer=ellipse_width)
            self._set_basic_animation_settings(
                target=target,
                duration=duration,
                delay=delay,
                easing=easing)
            super(AnimationWidthForEllipse, self).__init__(
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
        ellipse_width_str: str = value_util.get_value_str_for_expression(
            value=self._ellipse_width)
        return f'\n  .attr({{rx: {ellipse_width_str}}});'

    _ellipse_width_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_ellipse_width_snapshots'):
            self._ellipse_width_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._ellipse_width_snapshots[snapshot_name] = int(
            self._ellipse_width._value)

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._ellipse_width._value = self._ellipse_width_snapshots[
            snapshot_name]
