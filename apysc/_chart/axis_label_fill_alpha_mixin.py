"""The mix-in class implementation for the `axis_label_fill_alpha` value.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number
from apysc._validation import arg_validation_decos


class AxisLabelFillAlphaMixIn:
    _axis_label_fill_alpha: Number

    @final
    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_axis_label_fill_alpha(
        self,
        *,
        axis_label_fill_alpha: Union[float, Number],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set an initial axis label fill-alpha setting.

        Parameters
        ----------
        axis_label_fill_alpha : Union[float, Number]
            An axis label fill-alpha setting.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if not isinstance(axis_label_fill_alpha, Number):
            axis_label_fill_alpha_: Number = Number(
                axis_label_fill_alpha,
                variable_name_suffix=variable_name_suffix,
            )
        else:
            axis_label_fill_alpha_ = axis_label_fill_alpha
        self._axis_label_fill_alpha = axis_label_fill_alpha_
