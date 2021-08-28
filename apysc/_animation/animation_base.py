"""Base class implementation for the animation.
"""

from typing import Dict, Optional, Union
from abc import ABC
from abc import abstractmethod

import apysc as ap
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface
from apysc._animation.easing import Easing


class AnimationBase(RevertInterface, ABC):

    _instance: VariableNameInterface
    _duration: ap.Int
    _delay: ap.Int
    _easing: Optional[Easing]

    @abstractmethod
    def _get_animation_func_expression(self) -> str:
        """
        Get a animation function expression.

        Returns
        -------
        expression : str
            Animation function expression.
            e.g., '\n  .move(100, 200);'
        """

    def _set_basic_animation_settings(
            self,
            instance: VariableNameInterface,
            duration: Union[int, ap.Int],
            delay: Union[int, ap.Int] = 0,
            easing: Optional[Easing] = None) -> None:
        """
        Set the basic animation settings.

        Parameters
        ----------
        instance : VariableNameInterface
            An instance of the animation target
            (e.g., `DisplayObject` instance).
        duration : int or Int
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing or None, default None
            Easing setting. If None, Linear calculation is used.
        """
        with ap.DebugInfo(
                callable_=self._set_basic_animation_settings,
                locals_=locals(),
                module_name=__name__, class_=AnimationBase):
            from apysc._converter import to_apysc_val_from_builtin
            self._instance = instance
            self._duration = to_apysc_val_from_builtin.\
                get_copied_int_from_builtin_val(integer=duration)
            self._delay = to_apysc_val_from_builtin.\
                get_copied_int_from_builtin_val(integer=delay)
            self._easing = easing

    def start(self) -> None:
        """
        Start an animation with current settings.
        """
        with ap.DebugInfo(
                callable_=self.start, locals_=locals(),
                module_name=__name__, class_=AnimationBase):
            expression: str = (
                f'{self._instance.variable_name}'
                '\n  .animate({'
                f'\n    duration: {self._duration.variable_name},'
                f'\n    delay: {self._delay.variable_name}}})'
            )
            if self._easing is not None:
                expression += (
                    f'\n  .ease({self._easing.value})'
                )
            animation_expresssion: str = self._get_animation_func_expression()
            expression += animation_expresssion
            ap.append_js_expression(expression=expression)

    _instance_snapshots: Dict[str, VariableNameInterface]
    _duration_snapshots: Dict[str, int]
    _delay_snapshots: Dict[str, int]
    _easing_snapshots: Dict[str, Optional[Easing]]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make values' snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_instance_snapshots'):
            self._instance_snapshots = {}
            self._duration_snapshots = {}
            self._delay_snapshots = {}
            self._easing_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._instance_snapshots[snapshot_name] = self._instance
        self._duration_snapshots[snapshot_name] = int(self._duration._value)
        self._delay_snapshots[snapshot_name] = int(self._delay._value)
        self._easing_snapshots[snapshot_name] = self._easing

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
        self._instance = self._instance_snapshots[snapshot_name]
        self._duration._value = self._duration_snapshots[snapshot_name]
        self._delay._value = self._delay_snapshots[
            snapshot_name]
        self._easing = self._easing_snapshots[snapshot_name]
