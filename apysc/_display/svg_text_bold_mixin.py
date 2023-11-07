"""Class implementation for the SVG text's bold mix-in.
"""

from typing import Dict
from typing import Optional

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.boolean import Boolean
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn


class SvgTextBoldMixIn(
    VariableNameMixIn,
    RevertMixIn,
):
    _bold: bool = False

    @property
    @add_debug_info_setting(module_name=__name__)
    def bold(self) -> Boolean:
        """
        Get a boolean whether this text is a bold style or not.

        Returns
        -------
        bold_ : Boolean
            A boolean, whether this text is a bold style or not.
        """
        from apysc._expression import expression_data_util
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        suffix: str = get_attr_or_variable_name_suffix(
            instance=self,
            value_identifier="bold",
        )
        bold_: Boolean = Boolean(self._bold, variable_name_suffix=suffix)
        expression: str = (
            f'{bold_.variable_name} = {self.variable_name}.font("weight") === "bold";'
        )
        expression_data_util.append_js_expression(expression=expression)
        return bold_

    @bold.setter
    def bold(self, value: Boolean) -> None:
        """
        Set a boolean whether this text is a bold style or not.

        Parameters
        ----------
        value : Boolean
            A boolean, whether this text is a bold style or not.
        """
        from apysc._expression import expression_data_util

        self._bold = value._value
        expression: str = (
            f"if ({value.variable_name}) {{"
            f'\n  {self.variable_name}.font("weight", "bold");'
            "\n} else {"
            f'\n  {self.variable_name}.font("weight", "normal");'
            "\n}"
        )
        expression_data_util.append_js_expression(expression=expression)

    _bold_snapshots: Optional[Dict[str, bool]] = None

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._set_single_snapshot_val_to_dict(
            dict_name="_bold_snapshots",
            value=self._bold,
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
        self._bold = self._get_snapshot_val_if_exists(
            current_value=self._bold,
            snapshot_dict=self._bold_snapshots,
            snapshot_name=snapshot_name,
        )
