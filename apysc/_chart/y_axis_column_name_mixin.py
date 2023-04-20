"""The mix-in class implementation for the `y_axis_column_name` value.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.string import String
from apysc._validation import arg_validation_decos


class YAxisColumnNameMixIn:

    _y_axis_column_name: String

    @final
    @arg_validation_decos.is_string(arg_position_index=1)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_y_axis_column_name(
        self,
        *,
        y_axis_column_name: Union[str, String],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set an initial y-axis column name.

        Parameters
        ----------
        y_axis_column_name : Union[str, String]
            Y-axis column name.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if not isinstance(y_axis_column_name, String):
            y_axis_column_name_: String = String(
                y_axis_column_name,
                variable_name_suffix=variable_name_suffix,
            )
        else:
            y_axis_column_name_ = y_axis_column_name
        self._y_axis_column_name = y_axis_column_name_
