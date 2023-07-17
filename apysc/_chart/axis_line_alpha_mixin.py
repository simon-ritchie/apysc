"""The mix-in class implementation for the axis `line_alpha` value.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number
from apysc._validation import arg_validation_decos


class AxisLineAlphaMixIn:
    _line_alpha: Number

    @final
    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=1, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_line_alpha(
        self,
        *,
        line_alpha: Union[float, Number],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set an initial axis line alpha setting.

        Parameters
        ----------
        line_alpha : Union[float, Number]
            An axis line alpha setting.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if not isinstance(line_alpha, Number):
            line_alpha_: Number = Number(
                line_alpha,
                variable_name_suffix=variable_name_suffix,
            )
        else:
            line_alpha_ = line_alpha
        self._line_alpha = line_alpha_
