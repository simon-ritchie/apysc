"""Class implementation for line thickness interface.
"""

from typing import Dict
from typing import Union

import apysc as ap
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class LineThicknessInterface(VariableNameInterface, RevertInterface):

    _line_thickness: ap.Int

    def _initialize_line_thickness_if_not_initialized(self) -> None:
        """
        Initialize _line_thickness attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_line_thickness'):
            return
        self._line_thickness = ap.Int(1)

    @property
    def line_thickness(self) -> ap.Int:
        """
        Get this instance's line thickness.

        Returns
        -------
        line_thickness : Int
            Current line thickness.
        """
        with ap.DebugInfo(
                callable_='line_thickness', locals_=locals(),
                module_name=__name__, class_=LineThicknessInterface):
            from apysc._type import value_util
            return value_util.get_copy(value=self._line_thickness)

    @line_thickness.setter
    def line_thickness(self, value: ap.Int) -> None:
        """
        Update this instance's line thickness.

        Parameters
        ----------
        value : Int
            Line thickness to set.
        """
        with ap.DebugInfo(
                callable_='line_thickness', locals_=locals(),
                module_name=__name__, class_=LineThicknessInterface):
            self._update_line_thickness_and_skip_appending_exp(value=value)
            self._line_thickness.\
                _append_incremental_calc_substitution_expression()
            self._append_line_thickness_update_expression()

    def _append_line_thickness_update_expression(self) -> None:
        """
        Append line thickness update expression.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_line_thickness_update_expression,
                locals_=locals(),
                module_name=__name__, class_=LineThicknessInterface):
            expression: str = (
                f'{self.variable_name}.attr({{"stroke-width": '
                f'{self.line_thickness}}});'
            )
            ap.append_js_expression(expression=expression)

    def _update_line_thickness_and_skip_appending_exp(
            self, value: Union[int, ap.Int]) -> None:
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
            value = ap.Int(value)
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
