"""Mix-in class implementation for the `_set_initial_border_color` method.
"""

from typing_extensions import final

from apysc._color.color import Color
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos


class SetInitialBorderColorMixIn:
    _border_color: Color

    @final
    @arg_validation_decos.is_color(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_border_color(
        self,
        *,
        border_color: Color,
    ) -> None:
        """
        Set a chart's initial border color.

        Parameters
        ----------
        border_color : Color
            A chart's initial border color.
        """
        self._border_color = border_color
