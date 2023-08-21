"""Class implementation for the SVG text's delta-y mix-in.
"""

from typing import Dict
from typing import Optional

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos


class SVGTextDeltaYMixIn(
    VariableNameMixIn,
    RevertMixIn,
):
    _delta_y: float = 0.0

    @property
    @add_debug_info_setting(module_name=__name__)
    def delta_y(self) -> Number:
        """
        Get a current position's delta-y value.

        Returns
        -------
        delta_y : Number
            A current position's delta-y value.
        """
        from apysc._expression import expression_data_util
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        suffix: str = get_attr_or_variable_name_suffix(
            instance=self,
            value_identifier="delta_y",
        )
        delta_y: Number = Number(self._delta_y, variable_name_suffix=suffix)
        expression: str = f"{delta_y.variable_name} = {self.variable_name}.dy();"
        expression_data_util.append_js_expression(expression=expression)
        return delta_y

    @delta_y.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def delta_y(self, value: Number) -> None:
        """
        Set a position's delta-y value.

        Parameters
        ----------
        value : Number
            A delta-y value.

        Notes
        -----
        This setting also changes a coordinate of subsequent
        `SVGTextSpan`'s instance.
        """
        from apysc._expression import expression_data_util

        self._delta_y = value._value
        expression: str = f"{self.variable_name}.dy({value.variable_name});"
        expression_data_util.append_js_expression(expression=expression)

    _delta_y_snapshots: Optional[Dict[str, float]] = None

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._set_single_snapshot_val_to_dict(
            dict_name="_delta_y_snapshots",
            value=self._delta_y,
            snapshot_name=snapshot_name,
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._delta_y = self._get_snapshot_val_if_exists(
            current_value=self._delta_y,
            snapshot_dict=self._delta_y_snapshots,
            snapshot_name=snapshot_name,
        )
