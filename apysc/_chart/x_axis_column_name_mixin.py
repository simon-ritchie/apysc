"""The mix-in class implementation for the `x_axis_column_name` value.
"""

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos


class XAxisColumnNameMixIn:
    _x_axis_column_name: str

    @final
    @arg_validation_decos.is_builtin_string(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_x_axis_column_name(
        self,
        *,
        x_axis_column_name: str,
    ) -> None:
        """
        Set an initial x-axis column name.

        Parameters
        ----------
        x_axis_column_name : str
            X-axis column name.
        """
        self._x_axis_column_name = x_axis_column_name
