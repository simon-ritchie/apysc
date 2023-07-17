"""Mix-in class implementation for the control y path data.
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


class PathControlMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    RevertMixIn,
    AttrLinkingMixIn,
    VariableNameSuffixMixIn,
):
    _control_y: Number

    @final
    def _initialize_control_y_if_not_initialized(self) -> None:
        """
        Initialize the _control_y attribute if this instance
        does not initialize it yet.
        """
        if hasattr(self, "_control_y"):
            return
        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="control_y"
        )
        self._control_y = Number(
            0,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

        self._append_control_y_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_control_y_linking_setting(self) -> None:
        """
        Append a control_y attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._control_y, attr_name="control_y"
        )
        self._append_attr_to_linking_stack(attr=self._control_y, attr_name="control_y")

    @property
    @add_debug_info_setting(module_name=__name__)
    def control_y(self) -> Number:
        """
        Get a Y-coordinate of the control point.

        Returns
        -------
        control_y : Number
            Y-coordinate of the control point.

        Examples
        --------
        >>> import apysc as ap
        >>> bezier_2d: ap.PathBezier2D = ap.PathBezier2D(
        ...     control_x=0, control_y=0, dest_x=50, dest_y=50
        ... )
        >>> bezier_2d.control_y = ap.Number(25)
        >>> bezier_2d.control_y
        Number(25.0)
        """
        self._initialize_control_y_if_not_initialized()
        return self._control_y._copy()

    @control_y.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def control_y(self, value: Number) -> None:
        """
        Set a Y-coordinate of the control point.

        Parameters
        ----------
        value : Number
            Y-coordinate of the control point.
        """
        self._initialize_control_y_if_not_initialized()
        self._control_y.value = value

        self._append_control_y_linking_setting()

    _control_y_snapshots: Optional[Dict[str, float]] = None

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_control_y_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_control_y_snapshots",
            value=float(self._control_y._value),
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
        self._initialize_control_y_if_not_initialized()
        self._control_y._value = self._get_snapshot_val_if_exists(
            current_value=self._control_y._value,
            snapshot_dict=self._control_y_snapshots,
            snapshot_name=snapshot_name,
        )
