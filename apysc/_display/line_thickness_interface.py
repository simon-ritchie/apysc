"""Class implementation for line thickness interface.
"""

from typing import Dict
from typing import Union

from apysc import Int
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class LineThicknessInterface(VariableNameInterface, RevertInterface):

    _line_thickness: Int

    def _initialize_line_thickness_if_not_initialized(self) -> None:
        """
        Initialize _line_thickness attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_line_thickness'):
            return
        self._line_thickness = Int(1)

    @property
    def line_thickness(self) -> Int:
        """
        Get this instance's line thickness.

        Returns
        -------
        line_thickness : Int
            Current line thickness.
        """
        from apysc._type import value_util
        return value_util.get_copy(value=self._line_thickness)

    @line_thickness.setter
    def line_thickness(self, value: Int) -> None:
        """
        Update this instance's line thickness.

        Parameters
        ----------
        value : Int
            Line thickness to set.
        """
        self._update_line_thickness_and_skip_appending_exp(value=value)
        self._line_thickness.\
            _append_incremental_calc_substitution_expression()
        self._append_line_thickness_update_expression()

    def _append_line_thickness_update_expression(self) -> None:
        """
        Append line thickness update expression.
        """
        from apysc import append_js_expression
        expression: str = (
            f'{self.variable_name}.attr({{"stroke-width": '
            f'{self.line_thickness}}});'
        )
        append_js_expression(expression=expression)

    def _update_line_thickness_and_skip_appending_exp(
            self, value: Union[int, Int]) -> None:
        """
        Update line thickness and skip appending expression to file.

        Parameters
        ----------
        value : int or Int
            Line thickness to set.
        """
        from apysc._validation import number_validation
        number_validation.validate_integer(integer=value)
        number_validation.validate_num_is_gte_zero(num=value)
        if isinstance(value, int):
            value = Int(value)
        self._line_thickness = value

    _line_thickness_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_line_thickness_snapshots'):
            self._line_thickness_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_line_thickness_if_not_initialized()
        self._line_thickness_snapshots[snapshot_name] = int(
            self._line_thickness._value)

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
        self._line_thickness._value = self._line_thickness_snapshots[
            snapshot_name]
