"""The mix-in class implementation for the `x_axis_column_name` value.
"""

from typing import Dict, Optional, Union
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.string import String
from typing_extensions import final
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos


class XAxisColumnNameMixIn(
    RevertMixIn,
):

    _x_axis_column_name: String

    @final
    @arg_validation_decos.is_string(arg_position_index=1)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_x_axis_column_name(
        self,
        *,
        x_axis_column_name: Union[str, String],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set an initial x-axis column name.

        Parameters
        ----------
        x_axis_column_name : Union[str, String]
            X-axis column name.
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if not isinstance(x_axis_column_name, String):
            x_axis_column_name_: String = String(
                x_axis_column_name,
                variable_name_suffix=variable_name_suffix,
            )
        else:
            x_axis_column_name_ = x_axis_column_name
        self._x_axis_column_name = x_axis_column_name_

    _x_axis_column_name_snapshots: Optional[Dict[str, str]] = None

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._set_single_snapshot_val_to_dict(
            dict_name="_x_axis_column_name_snapshots",
            value=self._x_axis_column_name._value,
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
        self._x_axis_column_name._value = self._get_snapshot_val_if_exists(
            current_value=self._x_axis_column_name._value,
            snapshot_dict=self._x_axis_column_name_snapshots,
            snapshot_name=snapshot_name,
        )
