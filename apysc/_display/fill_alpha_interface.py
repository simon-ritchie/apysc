"""Class implementation for fill alpha interface.
"""

from typing import Any
from typing import Dict

import apysc as ap
from apysc._type.number_value_interface import NumberValueInterface
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class FillAlphaInterface(VariableNameInterface, RevertInterface):

    _fill_alpha: ap.Number

    def _initialize_fill_alpha_if_not_initialized(self) -> None:
        """
        Initialize _fill_alpha attribute it hasn't been initialized yet.
        """
        if hasattr(self, '_fill_alpha'):
            return
        self._fill_alpha = ap.Number(1.0)

    @property
    def fill_alpha(self) -> ap.Number:
        """
        Get this instance's fill opacity.

        Returns
        -------
        fill_alpha : Number
            Current fill opacity (0.0 to 1.0).
        """
        with ap.DebugInfo(
                callable_='fill_alpha', locals_=locals(),
                module_name=__name__, class_=FillAlphaInterface):
            from apysc._type import value_util
            self._initialize_fill_alpha_if_not_initialized()
            fill_alpha: ap.Number = value_util.get_copy(
                value=self._fill_alpha)
            return fill_alpha

    @fill_alpha.setter
    def fill_alpha(
            self, value: ap.Number) -> None:
        """
        Update this instance's fill opacity.

        Parameters
        ----------
        value : float or Number
            Fill opacity to set.
        """
        with ap.DebugInfo(
                callable_='fill_alpha', locals_=locals(),
                module_name=__name__, class_=FillAlphaInterface):
            if not isinstance(value, NumberValueInterface):
                value = ap.Number(value=value)
            self._update_fill_alpha_and_skip_appending_exp(value=value)
            self._fill_alpha._append_incremental_calc_substitution_expression()
            self._append_fill_alpha_update_expression()

    def _append_fill_alpha_update_expression(self) -> None:
        """
        Append fill alpha updating expression.
        """
        with ap.DebugInfo(
                callable_=self._append_fill_alpha_update_expression,
                locals_=locals(),
                module_name=__name__, class_=FillAlphaInterface):
            from apysc._type import value_util
            value_str: str = value_util.get_value_str_for_expression(
                value=self._fill_alpha)
            expression: str = (
                f'{self.variable_name}.fill({{opacity: {value_str}}});'
            )
            ap.append_js_expression(expression=expression)

    def _update_fill_alpha_and_skip_appending_exp(
            self, value: Any) -> None:
        """
        Update fill opacity and skip appending expression to file.

        Parameters
        ----------
        value : float or Number
            Fill opacity to set.
        """
        from apysc._converter import cast
        from apysc._validation import color_validation
        from apysc._validation import number_validation
        self._initialize_fill_alpha_if_not_initialized()
        number_validation.validate_num(num=value)
        if not isinstance(value, ap.Number):
            value = cast.to_float_from_int(int_or_float=value)
            color_validation.validate_alpha_range(alpha=value)
            value = ap.Number(value=value)
        color_validation.validate_alpha_range(alpha=value.value)
        self._fill_alpha = value

    _fill_alpha_snapshots: Dict[str, float]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_fill_alpha_snapshots'):
            self._fill_alpha_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_fill_alpha_if_not_initialized()
        self._fill_alpha_snapshots[snapshot_name] = self._fill_alpha._value

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
        self._fill_alpha._value = self._fill_alpha_snapshots[snapshot_name]
