"""The mix-in class implementation for the axis `line_color` value.
"""

from typing import TypeVar

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.string import String
from apysc._validation import arg_validation_decos

_StrOrString = TypeVar("_StrOrString", str, String)


class AxisLineColorMixIn:
    _line_color: String

    @final
    @arg_validation_decos.is_hex_color_code_format(arg_position_index=1, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_line_color(
        self,
        *,
        line_color: _StrOrString,
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set an initial line color.

        Parameters
        ----------
        line_color : _StrOrString
            An axis line color setting.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        from apysc._color import color_util

        line_color = color_util.complement_hex_color(hex_color_code=line_color)

        if not isinstance(line_color, String):
            line_color_: String = String(
                line_color,
                variable_name_suffix=variable_name_suffix,
            )
        else:
            line_color_ = line_color
        self._line_color = line_color_
