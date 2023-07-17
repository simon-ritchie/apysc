"""The mix-in class implementation for the `axis_label_font_size` value.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._validation import arg_validation_decos


class AxisLabelFontSizeMixIn:
    _axis_label_font_size: Int

    @final
    @arg_validation_decos.is_integer(arg_position_index=1, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=1, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_axis_label_font_size(
        self,
        *,
        axis_label_font_size: Union[int, Int],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set an initial axis label font size setting.

        Parameters
        ----------
        axis_label_font_size : Union[int, Int]
            An axis label font size setting.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if not isinstance(axis_label_font_size, Int):
            axis_label_font_size_: Int = Int(
                axis_label_font_size,
                variable_name_suffix=variable_name_suffix,
            )
        else:
            axis_label_font_size_ = axis_label_font_size
        self._axis_label_font_size = axis_label_font_size_
