"""Class implementation for the center y-coordinate interface.
"""

from typing import Dict

from apysc import Int
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class CyInterface(VariableNameInterface, RevertInterface):

    _cy: Int

    def _initialize_cy_if_not_initialized(self) -> None:
        """
        Initialize _cy attribute if it is not initialized yet.
        """
        if hasattr(self, '_cy'):
            return
        self._cy = Int(0)

    @property
    def y(self) -> Int:
        """
        Get a center y-coordinate.

        Returns
        -------
        y : Int
            Center y-coordinate.
        """
        from apysc._type import value_util
        self._initialize_cy_if_not_initialized()
        return value_util.get_copy(value=self._cy)

    @y.setter
    def y(self, value: Int) -> None:
        """
        Update a center y-coordinate.

        Parameters
        ----------
        value : int or Int
            Center y-coordinate value.
        """
        from apysc._validation import number_validation
        number_validation.validate_integer(integer=value)
        if not isinstance(value, Int):
            value = Int(value)
        self._cy = value
        self._cy._append_incremental_calc_substitution_expression()
        self._append_cy_update_expression()

    def _append_cy_update_expression(self) -> None:
        """
        Append cy position updating expression.
        """
        from apysc import append_js_expression
        from apysc._type import value_util
        self._initialize_cy_if_not_initialized()
        value_str: str = value_util.get_value_str_for_expression(
            value=self._cy)
        expression: str = (
            f'{self.variable_name}.cy({value_str});'
        )
        append_js_expression(expression=expression)

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
