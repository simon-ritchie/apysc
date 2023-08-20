"""The mix-in class implementation for
the `_copy_color_if_default_value_specified` method.
"""

from typing_extensions import final

from apysc._color.color import Color
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos


class CopyColorIfDefaultValueSpecifiedMixIn:
    @final
    @arg_validation_decos.is_color(arg_position_index=1, optional=False)
    @arg_validation_decos.is_color(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _copy_color_if_default_value_specified(
        self,
        color: Color,
        default_color: Color,
    ) -> Color:
        """
        Copy the specified color if it is a default color.

        Parameters
        ----------
        color : Color
            A color.
        default_color : Color
            A default color.

        Returns
        -------
        color : Color
            Copied color if it is a default color.
        """
        if color._value.variable_name == default_color._value.variable_name:
            return color._copy()
        return color
