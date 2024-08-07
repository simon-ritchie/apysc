"""Class implementation for the skew x interface.
"""

from typing import Dict

import apysc as ap
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class SkewXInterface(
        VariableNameInterface, RevertInterface, AttrLinkingInterface):

    _skew_x: ap.Int

    def _initialize_skew_x_if_not_initialized(self) -> None:
        """
        Initialize the _skew_x attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_skew_x'):
            return
        self._skew_x = ap.Int(0)

        self._append_skew_x_attr_linking_setting()

    def _append_skew_x_attr_linking_setting(self) -> None:
        """
        Append a skew-x attribute linking setting.
        """
        with ap.DebugInfo(
                callable_='skew_x', locals_=locals(),
                module_name=__name__, class_=SkewXInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._skew_x, attr_name='skew_x')
            self._append_attr_to_linking_stack(
                attr=self._skew_x, attr_name='skew_x')

    @property
    def skew_x(self) -> ap.Int:
        """
        Get a current skew x value of the instance.

        Returns
        -------
        skew_x : Int
            Current skew x value of this instance.
        """
        with ap.DebugInfo(
                callable_='skew_x', locals_=locals(),
                module_name=__name__, class_=SkewXInterface):
            from apysc._type import value_util
            self._initialize_skew_x_if_not_initialized()
            return value_util.get_copy(value=self._skew_x)

    @skew_x.setter
    def skew_x(self, value: ap.Int) -> None:
        """
        Update a skew x value of this instance.

        Parameters
        ----------
        value : Int
            Skew x value to set.
        """
        with ap.DebugInfo(
                callable_='skew_x', locals_=locals(),
                module_name=__name__, class_=SkewXInterface):
            from apysc._validation import number_validation
            self._initialize_skew_x_if_not_initialized()
            number_validation.validate_integer(integer=value)
            before_value: ap.Int = self._skew_x
            self._skew_x = value
            self._append_skew_x_update_expression(before_value=before_value)

            self._append_skew_x_attr_linking_setting()

    def _append_skew_x_update_expression(self, before_value: ap.Int) -> None:
        """
        Append the skew x updating expression.

        Parameters
        ----------
        before_value : ap.Int
            Before updating value.
        """
        with ap.DebugInfo(
                callable_=self._append_skew_x_update_expression,
                locals_=locals(),
                module_name=__name__, class_=SkewXInterface):
            from apysc._type import value_util
            before_value_str: str = value_util.get_value_str_for_expression(
                value=before_value)
            after_value_str: str = value_util.get_value_str_for_expression(
                value=self._skew_x)
            expression: str = (
                f'{self.variable_name}.skew(-{before_value_str}, 0);'
                f'\n{self.variable_name}.skew({after_value_str}, 0);'
                f'\n{before_value_str} = {after_value_str};'
            )
            ap.append_js_expression(expression=expression)

    _skew_x_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_skew_x_snapshots'):
            self._skew_x_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_skew_x_if_not_initialized()
        self._skew_x_snapshots[snapshot_name] = int(self._skew_x._value)

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
        self._skew_x._value = self._skew_x_snapshots[snapshot_name]
