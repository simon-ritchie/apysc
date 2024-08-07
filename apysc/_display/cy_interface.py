"""Class implementation for the center y-coordinate interface.
"""

from typing import Dict

import apysc as ap
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class CyInterface(
        VariableNameInterface, RevertInterface, AttrLinkingInterface):

    _cy: ap.Int

    def _initialize_cy_if_not_initialized(self) -> None:
        """
        Initialize _cy attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_cy'):
            return
        self._cy = ap.Int(0)

        self._append_cy_attr_linking_setting()

    def _append_cy_attr_linking_setting(self) -> None:
        """
        Append a cy attribute linking setting.
        """
        with ap.DebugInfo(
                callable_=self._append_cy_attr_linking_setting,
                locals_=locals(),
                module_name=__name__, class_=CyInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._cy, attr_name='cy')
            self._append_attr_to_linking_stack(attr=self._cy, attr_name='cy')

    @property
    def y(self) -> ap.Int:
        """
        Get a center y-coordinate.

        Returns
        -------
        y : Int
            Center y-coordinate.
        """
        with ap.DebugInfo(
                callable_='y', locals_=locals(),
                module_name=__name__, class_=CyInterface):
            from apysc._type import value_util
            self._initialize_cy_if_not_initialized()
            y: ap.Int = value_util.get_copy(value=self._cy)
            return y

    @y.setter
    def y(self, value: ap.Int) -> None:
        """
        Update a center y-coordinate.

        Parameters
        ----------
        value : int or Int
            Center y-coordinate value.
        """
        with ap.DebugInfo(
                callable_='y', locals_=locals(),
                module_name=__name__, class_=CyInterface):
            from apysc._validation import number_validation
            number_validation.validate_integer(integer=value)
            if not isinstance(value, ap.Int):
                value = ap.Int(value)
            self._cy = value
            self._cy._append_incremental_calc_substitution_expression()
            self._append_cy_update_expression()

            self._append_cy_attr_linking_setting()

    def _append_cy_update_expression(self) -> None:
        """
        Append cy position updating expression.
        """
        with ap.DebugInfo(
                callable_=self._append_cy_update_expression, locals_=locals(),
                module_name=__name__, class_=CyInterface):
            from apysc._type import value_util
            self._initialize_cy_if_not_initialized()
            value_str: str = value_util.get_value_str_for_expression(
                value=self._cy)
            expression: str = (
                f'{self.variable_name}.cy({value_str});'
            )
            ap.append_js_expression(expression=expression)

    _cy_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_cy_snapshots'):
            self._cy_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_cy_if_not_initialized()
        self._cy_snapshots[snapshot_name] = int(self._cy._value)

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
        self._cy._value = self._cy_snapshots[snapshot_name]
