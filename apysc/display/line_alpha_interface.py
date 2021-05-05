"""Class implementation for line alpha interface.
"""

from typing import Dict
from typing import Union

from apysc import Number
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface


class LineAlphaInterface(VariableNameInterface, RevertInterface):

    _line_alpha: Number

    def _initialize_line_alpha_if_not_initialized(self) -> None:
        """
        Initialize _line_alpha attribute if it is not initialized yet.
        """
        if hasattr(self, '_line_alpha'):
            return
        self._line_alpha = Number(1.0)

    @property
    def line_alpha(self) -> Number:
        """
        Get this instance's line alpha (opacity).

        Returns
        -------
        line_alpha : Number
            Current line alpha (opacity. 0.0 to 1.0).
        """
        from apysc.type import value_util
        return value_util.get_copy(value=self._line_alpha)

    @line_alpha.setter
    def line_alpha(self, value: Number) -> None:
        """
        Update this instance's line alpha (opacity).

        Parameters
        ----------
        value : Number
            Line alpha (opacity) to set.
        """
        self._update_line_alpha_and_skip_appending_exp(value=value)
        self._append_line_alpha_update_expression()

    def _append_line_alpha_update_expression(self) -> None:
        """
        Append line alpha updating expression.
        """
        from apysc.expression import expression_file_util
        expression: str = (
            f'{self.variable_name}.stroke({{opacity: {self.line_alpha}}});'
        )
        expression_file_util.append_js_expression(expression=expression)

    def _update_line_alpha_and_skip_appending_exp(
            self, value: Union[float, Number]) -> None:
        """
        Update line alpha and skip appending expression to file.

        Parameters
        ----------
        value : float or Number
            Line alpha (opacity) to set.
        """
        from apysc.validation import color_validation
        from apysc.validation import number_validation
        number_validation.validate_num(num=value)
        color_validation.validate_alpha_range(alpha=value)
        if isinstance(value, float):
            value = Number(value)
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
