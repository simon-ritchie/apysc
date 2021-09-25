"""Class implementation for the center x-coordinate interface.
"""

from typing import Dict

import apysc as ap
from apysc._animation.animation_cx_interface import AnimationCxInterface
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.revert_interface import RevertInterface


class CxInterface(
        AnimationCxInterface, RevertInterface, AttrLinkingInterface):

    _cx: ap.Int

    def _initialize_cx_if_not_initialized(self) -> None:
        """
        Initialize _cx attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_cx'):
            return
        self._cx = ap.Int(0)

        self._append_cx_attr_linking_setting()

    def _append_cx_attr_linking_setting(self) -> None:
        """
        Append a cx attribute linking setting.
        """
        with ap.DebugInfo(
                callable_=self._append_cx_attr_linking_setting,
                locals_=locals(),
                module_name=__name__, class_=CxInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._cx, attr_name='cx')
            self._append_attr_to_linking_stack(attr=self._cx, attr_name='cx')

    @property
    def x(self) -> ap.Int:
        """
        Get a center x-coordinate.

        Returns
        -------
        x : Int
            Center x-coordinate.
        """
        with ap.DebugInfo(
                callable_='x', locals_=locals(),
                module_name=__name__, class_=CxInterface):
            from apysc._type import value_util
            self._initialize_cx_if_not_initialized()
            x: ap.Int = value_util.get_copy(value=self._cx)
            return x

    @x.setter
    def x(self, value: ap.Int) -> None:
        """
        Update a center x-coordinate.

        Parameters
        ----------
        value : int or Int
            Center x-coordinate value.
        """
        with ap.DebugInfo(
                callable_='x', locals_=locals(),
                module_name=__name__, class_=CxInterface):
            from apysc._validation import number_validation
            number_validation.validate_integer(integer=value)
            if not isinstance(value, ap.Int):
                value = ap.Int(value)
            self._cx = value
            self._cx._append_incremental_calc_substitution_expression()
            self._append_cx_update_expression()

            self._append_cx_attr_linking_setting()

    def _append_cx_update_expression(self) -> None:
        """
        Append cx position updating expression.
        """
        from apysc._type import value_util
        self._initialize_cx_if_not_initialized()
        value_str: str = value_util.get_value_str_for_expression(
            value=self._cx)
        expression: str = (
            f'{self.variable_name}.cx({value_str});'
        )
        ap.append_js_expression(expression=expression)

    _cx_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_cx_snapshots'):
            self._cx_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_cx_if_not_initialized()
        self._cx_snapshots[snapshot_name] = int(self._cx._value)

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert a value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._cx._value = self._cx_snapshots[snapshot_name]
