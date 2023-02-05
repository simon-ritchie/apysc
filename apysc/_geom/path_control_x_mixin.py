"""Mix-in class implementation for the control x path data.
"""

from typing import Dict

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


class PathControlXMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    RevertMixIn,
    AttrLinkingMixIn,
    VariableNameSuffixMixIn,
):

    _control_x: Number

    @final
    def _initialize_control_x_if_not_initialized(self) -> None:
        """
        Initialize the _control_x attribute if this instance
        does not initialize it yet.
        """
        if hasattr(self, "_control_x"):
            return
        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="control_x"
        )
        self._control_x = Number(
            0,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

        self._append_control_x_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_control_x_linking_setting(self) -> None:
        """
        Append a control_x attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._control_x, attr_name="control_x"
        )
        self._append_attr_to_linking_stack(attr=self._control_x, attr_name="control_x")

    @property
    @add_debug_info_setting(module_name=__name__)
    def control_x(self) -> Number:
        """
        Get a X-coordinate of the point.

        Returns
        -------
        control_x : Number
            X-coordinate of the control point.

        Examples
        --------
        >>> import apysc as ap
        >>> bezier_2d: ap.PathBezier2D = ap.PathBezier2D(
        ...     control_x=50, control_y=0, dest_x=100, dest_y=50
        ... )
        >>> bezier_2d.control_x = ap.Number(125)
        >>> bezier_2d.control_x
        Number(125.0)
        """
        self._initialize_control_x_if_not_initialized()
        return self._control_x._copy()

    @control_x.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def control_x(self, value: Number) -> None:
        """
        Set a X-coordinate of the control point.

        Parameters
        ----------
        value : Number
            X-coordinate of the control point.
        """
        self._initialize_control_x_if_not_initialized()
        self._control_x.value = value

        self._append_control_x_linking_setting()

    _control_x_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_control_x_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_control_x_snapshots",
            value=int(self._control_x._value),
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
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_control_x_if_not_initialized()
        self._control_x._value = self._control_x_snapshots[snapshot_name]
