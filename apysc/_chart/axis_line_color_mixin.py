"""The mix-in class implementation for the axis `line_color` value.
"""

from typing_extensions import final

from apysc._color.color import Color
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos


class AxisLineColorMixIn:
    @final
    @arg_validation_decos.is_color(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_line_color(
        self,
        *,
        line_color: Color,
    ) -> None:
        """
        Set an initial line color.

        Parameters
        ----------
        line_color : Color
            An axis line color setting.
        """
        self._line_color = line_color._copy()
