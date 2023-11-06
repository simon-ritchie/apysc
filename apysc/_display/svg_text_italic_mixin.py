"""Class implementation for the SVG text's italic mix-in.
"""

from typing import Dict
from typing import Optional

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.boolean import Boolean
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos


class SvgTextItalicMixIn(
    VariableNameMixIn,
    RevertMixIn,
):
    _italic: bool = False

    @property
    @add_debug_info_setting(module_name=__name__)
    def italic(self) -> Boolean:
        """
        Get a boolean value indicating whether a text is italic style or not.

        Returns
        -------
        italic_ : Boolean
            A boolean value indicating whether a text is italic style or not.
        """
        from apysc._expression import expression_data_util
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        suffix: str = get_attr_or_variable_name_suffix(
            instance=self,
            value_identifier="italic",
        )
        italic_: Boolean = Boolean(self._italic, variable_name_suffix=suffix)
        expression: str = (
            f"{italic_.variable_name} = "
            f'{self.variable_name}.font("style") === "italic";'
        )
        expression_data_util.append_js_expression(expression=expression)
        return italic_

    @italic.setter
    @arg_validation_decos.is_apysc_boolean(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def italic(self, value: Boolean) -> None:
        from apysc._expression import expression_data_util

        self._italic = value._value
        expression: str = (
            f"if ({value.variable_name}) {{"
            f'\n  {self.variable_name}.font("style", "italic");'
            "\n} else {"
            f'\n  {self.variable_name}.font("style", "normal");'
            "\n}"
        )
        expression_data_util.append_js_expression(expression=expression)

    _italic_snapshots: Optional[Dict[str, bool]] = None

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._set_single_snapshot_val_to_dict(
            dict_name="_italic_snapshots",
            value=self._italic,
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
        self._italic = self._get_snapshot_val_if_exists(
            current_value=self._italic,
            snapshot_dict=self._italic_snapshots,
            snapshot_name=snapshot_name,
        )
