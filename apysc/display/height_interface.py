"""Class implementation for height interface.
"""

from typing import Dict
from typing import Union

from apysc import Int
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface


class HeightInterface(VariableNameInterface, RevertInterface):

    _height: Int

    def _initialize_height_if_not_initialized(self) -> None:
        """
        Initialize _height attribute if it is not initialized yet.
        """
        if hasattr(self, '_height'):
            return
        self._height = Int(0)

    @property
    def height(self) -> Int:
        """
        Get this instance's height.

        Returns
        -------
        height : Int
            This instance's height.
        """
        from apysc.type import value_util
        self._initialize_height_if_not_initialized()
        return value_util.get_copy(value=self._height)

    @height.setter
    def height(self, value: Int) -> None:
        """
        Update this instance's height.

        Parameters
        ----------
        value : int
            Height value to set.
        """
        self._update_height_and_skip_appending_exp(value=value)
        self._append_height_update_expression()

    def _append_height_update_expression(self) -> None:
        """
        Append height updating expression.
        """
        from apysc.expression import expression_file_util
        expression: str = (
            f'{self.variable_name}.height({self.height});'
        )
        expression_file_util.append_js_expression(expression=expression)

    def _update_height_and_skip_appending_exp(
            self, value: Union[int, Int]) -> None:
        """
        Update height value and skip appending expression to file.

        Parameters
        ----------
        value : int or Int
            Height value to set.
        """
        from apysc.converter import cast
        from apysc.validation import size_validation
        self._initialize_height_if_not_initialized()
        value = cast.to_int_from_float(int_or_float=value)
        size_validation.validate_size_is_int(size=value)
        size_validation.validate_size_is_gte_zero(size=value)
        if isinstance(value, int):
            value = Int(value)
        self._height = value

    _height_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_height_snapshots'):
            self._height_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_height_if_not_initialized()
        self._height_snapshots[snapshot_name] = int(self._height._value)

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._height._value = self._height_snapshots[snapshot_name]
