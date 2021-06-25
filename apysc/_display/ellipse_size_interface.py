"""Class implementation for the ellipse size interface.
"""

from typing import Dict

from apysc import Int
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class EllipseSizeInterface(VariableNameInterface, RevertInterface):

    _ellipse_size: Int
    _ellipse_width: Int
    _ellipse_height: Int

    def _initialize_ellipse_size_if_not_initialized(self) -> None:
        """
        Initialize _ellipse_size attribute if it is not initialized yet.
        """
        if hasattr(self, '_ellipse_size'):
            return
        self._ellipse_size = Int(0)

    @property
    def ellipse_size(self) -> Int:
        """
        Get a ellipse size value.

        Returns
        -------
        ellipse_size : Int
            Ellipse size value.
        """
        from apysc._type import value_util
        self._initialize_ellipse_size_if_not_initialized()
        return value_util.get_copy(value=self._ellipse_size)

    @ellipse_size.setter
    def ellipse_size(self, value: Int) -> None:
        """
        Update a ellipse size value. This inteface will updates
        both of the ellipse width and ellipse height attributes.

        Parameters
        ----------
        value : int or Int
            Ellipse size value.
        """
        from apysc._validation import number_validation
        if not isinstance(value, Int):
            number_validation.validate_integer(integer=value)
            value = Int(value)
        self._ellipse_size = value
        self._ellipse_width = value
        self._ellipse_height = value
        self._ellipse_size._append_incremental_calc_substitution_expression()
        self._ellipse_width._append_incremental_calc_substitution_expression()
        self._ellipse_height.\
            _append_incremental_calc_substitution_expression()
        self._append_ellipse_size_update_expression()

    def _append_ellipse_size_update_expression(self) -> None:
        """
        Append an ellipse size updating expression.
        """
        from apysc import append_js_expression
        from apysc._type import value_util
        self._initialize_ellipse_size_if_not_initialized()
        value_str: str = value_util.get_value_str_for_expression(
            value=self._ellipse_size)
        expression: str = (
            f'{self.variable_name}.radius({value_str});'
        )
        append_js_expression(expression=expression)

    _ellipse_size_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make the value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_ellipse_size_snapshots'):
            self._ellipse_size_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_ellipse_size_if_not_initialized()
        self._ellipse_size_snapshots[snapshot_name] = int(
            self._ellipse_size._value)

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert the value if the snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._ellipse_size._value = self._ellipse_size_snapshots[
            snapshot_name]
