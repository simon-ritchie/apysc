"""The mix-in class implementation for the `axis_label_fill_color`.
"""

from typing_extensions import final

from apysc._color.color import Color
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos


class AxisLabelFillColorMixIn:
    _axis_label_fill_color: Color

    @final
    @arg_validation_decos.is_color(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_axis_label_fill_color(
        self,
        *,
        axis_label_fill_color: Color,
    ) -> None:
        """
        Set an initial axis label fill-color setting.

        Parameters
        ----------
        axis_label_fill_color : Color
            An axis label fill-color setting.
        """
        self._axis_label_fill_color = axis_label_fill_color
