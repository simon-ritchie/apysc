"""The mix-in class implementation for the axis `line_thickness` value.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._validation import arg_validation_decos


class AxisLineThicknessMixIn:
    _line_thickness: Int

    @final
    @arg_validation_decos.is_integer(arg_position_index=1, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=1, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_line_thickness(
        self,
        *,
        line_thickness: Union[int, Int],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set an initial axis line thickness (line width) setting.

        Parameters
        ----------
        line_thickness : Union[int, Int]
            An axis line thickness (line width) setting.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if not isinstance(line_thickness, Int):
            line_thickness_: Int = Int(
                line_thickness,
                variable_name_suffix=variable_name_suffix,
            )
        else:
            line_thickness_ = line_thickness
        self._line_thickness = line_thickness_
