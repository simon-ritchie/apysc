"""Class implementation for the AnimationMove value.
"""

from typing import Dict
from typing import Optional
from typing import Union

import apysc as ap
from apysc._animation.animation_base import AnimationBase
from apysc._animation.easing import Easing
from apysc._type.variable_name_interface import VariableNameInterface


class AnimationMove(AnimationBase):

    _x: ap.Int
    _y: ap.Int

    def __init__(
            self,
            instance: VariableNameInterface,
            x: Union[int, ap.Int],
            y: Union[int, ap.Int],
            duration: Union[int, ap.Int],
            delay: Union[int, ap.Int] = 0,
            easing: Optional[Easing] = None) -> None:
        """
        The animation class for moving x and y coordinates.

        Parameters
        ----------
        instance : VariableNameInterface
            An instance of the animation target
            (e.g., `DisplayObject` instance).
        x : int or Int
            Destination of the x-coordinate.
        y : int or Int
            Destination of the y-coordinate.
        duration : int or Int
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing or None, default None
            Easing setting. If None, Linear calculation is used.
        """
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=AnimationMove):
            from apysc._converter import to_apysc_val_from_builtin
            self._x = to_apysc_val_from_builtin.\
                get_copied_int_from_builtin_val(integer=x)
            self._y = to_apysc_val_from_builtin.\
                get_copied_int_from_builtin_val(integer=y)
            self._set_basic_animation_settings(
                instance=instance,
                duration=duration,
                delay=delay,
                easing=easing)

    def _get_animation_func_expression(self) -> str:
        """
        Get a animation function expression.

        Returns
        -------
        expression : str
            Animation function expression.
        """
        from apysc._type import value_util
        x_str: str = value_util.get_value_str_for_expression(value=self._x)
        y_str: str = value_util.get_value_str_for_expression(value=self._y)
        return f'\n  .move({x_str}, {y_str});'

    _x_snapshots: Dict[str, int]
    _y_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make values' snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_x_snapshots'):
            self._x_snapshots = {}
            self._y_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._x_snapshots[snapshot_name] = int(self._x._value)
        self._y_snapshots[snapshot_name] = int(self._y._value)

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert values if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._x._value = self._x_snapshots[snapshot_name]
        self._y._value = self._y_snapshots[snapshot_name]
