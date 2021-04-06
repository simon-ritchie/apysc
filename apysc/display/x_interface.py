"""Class implementation for x position interface.
"""

from typing import Dict

from apysc import Int
from apysc.type.number_value_interface import NumberValueInterface
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface


class XInterface(VariableNameInterface, RevertInterface):

    _x: Int

    def _initialize_x_if_not_initialized(self) -> None:
        """
        Initialize _x attribute if it is not initialized yet.
        """
        if hasattr(self, '_x'):
            return
        self._x = Int(0)

    @property
    def x(self) -> Int:
        """
        Get x position.

        Returns
        -------
        x : Int
            X position.
        """
        from apysc.type import value_util
        self._initialize_x_if_not_initialized()
        return value_util.get_copy(value=self._x)

    @x.setter
    def x(self, value: Int) -> None:
        """
        Update x position.

        Parameters
        ----------
        value : int or Int
            X potision value.
        """
        from apysc.validation import number_validation
        if not isinstance(value, NumberValueInterface):
            number_validation.validate_integer(integer=value)
            value = Int(value=value)
        self._x = value
        self._append_x_update_expression()

    def _append_x_update_expression(self) -> None:
        """
        Append x position updating expression.
        """
        from apysc.expression import expression_file_util
        from apysc.type import value_util
        self._initialize_x_if_not_initialized()
        value_str: str = value_util.get_value_str_for_expression(
            value=self._x)
        expression: str = (
            f'{self.variable_name}.x({value_str});'
        )
        expression_file_util.append_js_expression(expression=expression)

    _x_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make values snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_x_snapshots'):
            self._x_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_x_if_not_initialized()
        self._x_snapshots[snapshot_name] = int(self._x._value)

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
