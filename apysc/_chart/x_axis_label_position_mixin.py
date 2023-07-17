"""The mix-in class implementation for the `x_axis_label_position`.
"""

from typing_extensions import final

from apysc._chart.x_axis_label_position import XAxisLabelPosition
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos


class XAxisLabelPositionMixIn:
    _x_axis_label_position: XAxisLabelPosition

    @final
    @arg_validation_decos.is_x_axis_label_position(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_x_axis_label_position(
        self,
        *,
        x_axis_label_position: XAxisLabelPosition,
    ) -> None:
        """
        Set an initial x-axis label position setting.

        Parameters
        ----------
        x_axis_label_position : XAxisLabelPosition
            An x-axis label position setting.
        """
        self._x_axis_label_position = x_axis_label_position
