"""Class implementation for line alpha interface.
"""

from typing import Dict
from typing import Union

import apysc as ap
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class LineAlphaInterface(VariableNameInterface, RevertInterface):

    _line_alpha: ap.Number

    def _initialize_line_alpha_if_not_initialized(self) -> None:
        """
        Initialize _line_alpha attribute it hasn't been initialized yet.
        """
        if hasattr(self, '_line_alpha'):
            return
        self._line_alpha = ap.Number(1.0)

    @property
    def line_alpha(self) -> ap.Number:
        """
        Get this instance's line alpha (opacity).

        Returns
        -------
        line_alpha : Number
            Current line alpha (opacity. 0.0 to 1.0).
        """
        with ap.DebugInfo(
                callable_='line_alpha', locals_=locals(),
                module_name=__name__, class_=LineAlphaInterface):
            from apysc._type import value_util
            return value_util.get_copy(value=self._line_alpha)

    @line_alpha.setter
    def line_alpha(self, value: ap.Number) -> None:
        """
        Update this instance's line alpha (opacity).

        Parameters
        ----------
        value : Number
            Line alpha (opacity) to set.
        """
        with ap.DebugInfo(
                callable_='line_alpha', locals_=locals(),
                module_name=__name__, class_=LineAlphaInterface):
            self._update_line_alpha_and_skip_appending_exp(value=value)
            self._line_alpha._append_incremental_calc_substitution_expression()
            self._append_line_alpha_update_expression()

    def _append_line_alpha_update_expression(self) -> None:
        """
        Append line alpha updating expression.
        """
        with ap.DebugInfo(
                callable_=self._append_line_alpha_update_expression,
                locals_=locals(),
                module_name=__name__, class_=LineAlphaInterface):
            expression: str = (
                f'{self.variable_name}.stroke({{opacity: {self.line_alpha}}});'
            )
            ap.append_js_expression(expression=expression)

    def _update_line_alpha_and_skip_appending_exp(
            self, value: Union[float, ap.Number]) -> None:
        """
        Update line alpha and skip appending expression to file.

        Parameters
        ----------
        value : float or Number
            Line alpha (opacity) to set.
        """
        from apysc._validation import color_validation
        from apysc._validation import number_validation
        number_validation.validate_num(num=value)
        color_validation.validate_alpha_range(alpha=value)
        if isinstance(value, float):
            value = ap.Number(value)
        self._line_alpha = value

    _line_alpha_snapshots: Dict[str, float]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_line_alpha_snapshots'):
            self._line_alpha_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_line_alpha_if_not_initialized()
        self._line_alpha_snapshots[snapshot_name] = self._line_alpha._value

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
        self._line_alpha._value = self._line_alpha_snapshots[snapshot_name]
