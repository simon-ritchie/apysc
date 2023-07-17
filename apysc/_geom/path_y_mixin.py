"""Mix-in class implementation for the y path data.
"""

from typing import Dict
from typing import Optional

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.number import Number
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos


class PathYMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    RevertMixIn,
    AttrLinkingMixIn,
    VariableNameSuffixMixIn,
):
    _y: Number

    @final
    def _initialize_y_if_not_initialized(self) -> None:
        """
        Initialize the _y attribute if this instance does not
        initialize it yet.
        """
        if hasattr(self, "_y"):
            return
        suffix: str = self._get_attr_or_variable_name_suffix(value_identifier="y")
        self._y = Number(
            0,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

        self._append_y_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_y_linking_setting(self) -> None:
        """
        Append a y attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(new_attr=self._y, attr_name="y")
        self._append_attr_to_linking_stack(attr=self._y, attr_name="y")

    @property
    @add_debug_info_setting(module_name=__name__)
    def y(self) -> Number:
        """
        Get a y-coordinate of the destination point.

        Returns
        -------
        y : Number
            A y-coordinate of the destination point.

        Examples
        --------
        >>> import apysc as ap
        >>> line_to: ap.PathLineTo = ap.PathLineTo(x=50, y=50)
        >>> line_to.y = ap.Number(100)
        >>> line_to.y
        Number(100.0)
        """
        self._initialize_y_if_not_initialized()
        return self._y._copy()

    @y.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def y(self, value: Number) -> None:
        """
        Set a y-coordinate of the destination point.

        Parameters
        ----------
        value : Number
            Y-coordinate of the destination point.
        """
        self._initialize_y_if_not_initialized()
        self._y.value = value

        self._append_y_linking_setting()

    _y_snapshots: Optional[Dict[str, float]] = None

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_y_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_y_snapshots",
            value=float(self._y._value),
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
        self._y._value = self._get_snapshot_val_if_exists(
            current_value=self._y._value,
            snapshot_dict=self._y_snapshots,
            snapshot_name=snapshot_name,
        )
