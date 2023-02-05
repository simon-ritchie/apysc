"""Interface class implementation for the x path data.
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


class PathXMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    RevertMixIn,
    AttrLinkingMixIn,
    VariableNameSuffixMixIn,
):

    _x: Number

    @final
    def _initialize_x_if_not_initialized(self) -> None:
        """
        Initialize the _x attribute if this instance does not
        initialize it yet.
        """
        if hasattr(self, "_x"):
            return
        suffix: str = self._get_attr_or_variable_name_suffix(value_identifier="x")
        self._x = Number(
            0,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

        self._append_x_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_x_linking_setting(self) -> None:
        """
        Append an x attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(new_attr=self._x, attr_name="x")
        self._append_attr_to_linking_stack(attr=self._x, attr_name="x")

    @property
    @add_debug_info_setting(module_name=__name__)
    def x(self) -> Number:
        """
        Get an x-coordinate of the destination point.

        Returns
        -------
        x : Number
            An x-coordinate of the destination point.

        Examples
        --------
        >>> import apysc as ap
        >>> line_to: ap.PathLineTo = ap.PathLineTo(x=50, y=50)
        >>> line_to.x = ap.Number(100)
        >>> line_to.x
        Number(100.0)
        """
        self._initialize_x_if_not_initialized()
        return self._x._copy()

    @x.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def x(self, value: Number) -> None:
        """
        Set an x-coordinate of the destination point.

        Parameters
        ----------
        value : Number
            X-coordinate of the destination point.
        """
        self._initialize_x_if_not_initialized()
        self._x.value = value

        self._append_x_linking_setting()

    _x_snapshots: Dict[str, float]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_x_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_x_snapshots",
            value=float(self._x._value),
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
        self._initialize_x_if_not_initialized()
        self._x._value = self._x_snapshots[snapshot_name]
