"""The mix-in class implementation for the `x_axis_column_name` value.
"""

from typing import Union
from apysc._type.string import String
from typing_extensions import final
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos


class XAxisColumnNameMixIn:

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
