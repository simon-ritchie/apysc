"""The mix-in class implementation for the `tick_text_fill_color` value.
"""

from typing_extensions import final

from apysc._color.color import Color
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos


class TickTextFillColorMixIn:
    _tick_text_fill_color: Color

    @final
    @arg_validation_decos.is_color(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_tick_text_fill_color(
        self,
        *,
        tick_text_fill_color: Color,
    ) -> None:
        """
        Set an initial tick text fill color setting.

        Parameters
        ----------
        tick_text_fill_color : Color
            A tick text fill-color setting.
        """
        self._tick_text_fill_color = tick_text_fill_color
