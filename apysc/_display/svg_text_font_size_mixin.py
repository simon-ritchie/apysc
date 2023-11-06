"""Class implementation for the SVG text's font-size mix-in.
"""

from typing import Dict
from typing import Optional

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos


class SvgTextFontSizeMixIn(
    VariableNameMixIn,
    RevertMixIn,
):
    _font_size: int = 16

    @property
    @add_debug_info_setting(module_name=__name__)
    def font_size(self) -> Int:
        """
        Get a current font-size setting.

        Returns
        -------
        font_size : Int
            A current font-size setting.
        """
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        suffix: str = get_attr_or_variable_name_suffix(
            instance=self,
            value_identifier="font_size",
        )
        font_size: Int = Int(self._font_size, variable_name_suffix=suffix)
        self._append_font_size_getter_expression(font_size=font_size)
        return font_size

    @font_size.setter
    @arg_validation_decos.num_is_gte_zero(arg_position_index=1, optional=False)
    @arg_validation_decos.is_apysc_integer(arg_position_index=1)
    def font_size(self, value: Int) -> None:
        """
        Set a font-size setting.

        Parameters
        ----------
        value : Int
            A font-size setting.
        """
        from apysc._expression import expression_data_util

        self._font_size = value._value
        expression: str = f'{self.variable_name}.font("size", {value.variable_name});'
        expression_data_util.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_font_size_getter_expression(self, *, font_size: Int) -> None:
        """
        Append a font-size getter expression string.

        Parameters
        ----------
        font_size : Int
            A target font-size setting.
        """
        from apysc._expression import expression_data_util

        expression: str = (
            f'{font_size.variable_name} = {self.variable_name}.font("size");'
        )
        expression_data_util.append_js_expression(expression=expression)

    _font_size_snapshots: Optional[Dict[str, int]] = None

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._set_single_snapshot_val_to_dict(
            dict_name="_font_size_snapshots",
            value=self._font_size,
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
        self._font_size = self._get_snapshot_val_if_exists(
            current_value=self._font_size,
            snapshot_dict=self._font_size_snapshots,
            snapshot_name=snapshot_name,
        )
