"""Class implementation for the SVG text's align mix-in.
"""

from enum import Enum
from typing import Dict
from typing import Optional

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos


class SvgTextAlign(Enum):
    """
    SVG text's align enum class.

    Attributes
    ----------
    LEFT : str
        An enum definition to align left-position.
    CENTER : str
        An enum definition to align center-position.
    RIGHT : str
        An enum definition to align right-position.
    """

    LEFT = "start"
    CENTER = "middle"
    RIGHT = "end"


class SvgTextAlignMixIn(
    VariableNameMixIn,
    RevertMixIn,
):
    _align: SvgTextAlign = SvgTextAlign.LEFT

    @property
    @add_debug_info_setting(module_name=__name__)
    def align(self) -> SvgTextAlign:
        """
        Get a current text-align setting.

        Returns
        -------
        align : SvgTextAlign
            A current text-align setting.
        """
        return self._align

    @align.setter
    @add_debug_info_setting(module_name=__name__)
    @arg_validation_decos.is_svg_text_align(arg_position_index=1)
    def align(self, value: SvgTextAlign) -> None:
        """
        Set a text-align setting.

        Parameters
        ----------
        value : SvgTextAlign
            A text-align setting.
        """
        from apysc._expression import expression_data_util

        self._align = value
        expression: str = f'{self.variable_name}.font("anchor", "{value.value}");'
        expression_data_util.append_js_expression(expression=expression)

    _align_snapshots: Optional[Dict[str, SvgTextAlign]] = None

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._set_single_snapshot_val_to_dict(
            dict_name="_align_snapshots",
            value=self._align,
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
        self._align = self._get_snapshot_val_if_exists(
            current_value=self._align,
            snapshot_dict=self._align_snapshots,
            snapshot_name=snapshot_name,
        )
