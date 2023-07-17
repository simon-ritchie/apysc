"""The mix-in class implementation for the `y_axis_label_position` value.
"""

from typing_extensions import final

from apysc._chart.y_axis_label_position import YAxisLabelPosition
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos


class YAxisLabelPositionMixIn:
    _y_axis_label_position: YAxisLabelPosition

    @final
    @arg_validation_decos.is_y_axis_label_position(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_y_axis_label_position(
        self,
        *,
        y_axis_label_position: YAxisLabelPosition,
    ) -> None:
        """
        Set an initial y-axis label position setting.

        Parameters
        ----------
        y_axis_label_position : YAxisLabelPosition
            A y-axis label position setting.
        """
        self._y_axis_label_position = y_axis_label_position
