"""Class implementation for the SVG text's leading mix-in.
"""

from typing import Dict
from typing import Optional

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos


class SvgTextLeadingMixIn(
    VariableNameMixIn,
    RevertMixIn,
):
    _leading: float = 1.5

    @property
    @add_debug_info_setting(module_name=__name__)
    def leading(self) -> Number:
        """
        Get a current leading setting.

        Returns
        -------
        leading : Number
            A current leading setting.
        """
        from apysc._expression import expression_data_util
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        suffix: str = get_attr_or_variable_name_suffix(
            instance=self,
            value_identifier="leading",
        )
        leading: Number = Number(self._leading, variable_name_suffix=suffix)
        expression: str = (
            f'{leading.variable_name} = {self.variable_name}.font("leading");'
        )
        expression_data_util.append_js_expression(expression=expression)
        return leading

    @leading.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def leading(self, value: Number) -> None:
        """
        Set a leading setting.

        Parameters
        ----------
        value : Number
            A leading setting.
        """
        from apysc._expression import expression_data_util

        self._leading = value._value
        expression: str = (
            f'{self.variable_name}.font("leading", {value.variable_name});'
        )
        expression_data_util.append_js_expression(expression=expression)

    _leading_snapshots: Optional[Dict[str, float]] = None

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._set_single_snapshot_val_to_dict(
            dict_name="_leading_snapshots",
            value=self._leading,
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
        self._leading = self._get_snapshot_val_if_exists(
            current_value=self._leading,
            snapshot_dict=self._leading_snapshots,
            snapshot_name=snapshot_name,
        )
