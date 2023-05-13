"""The mix-in class implementation for the `axis_label_fill_color`.
"""

from typing import TypeVar

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.string import String
from apysc._validation import arg_validation_decos

_StrOrString = TypeVar("_StrOrString", str, String)


class AxisLabelFillColorMixIn:

    _axis_label_fill_color: String

    @final
    @arg_validation_decos.is_hex_color_code_format(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_axis_label_fill_color(
        self,
        *,
        axis_label_fill_color: _StrOrString,
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set an initial axis label fill-color setting.

        Parameters
        ----------
        axis_label_fill_color : _StrOrString
            An axis label fill-color setting.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        from apysc._color import color_util

        axis_label_fill_color = color_util.complement_hex_color(
            hex_color_code=axis_label_fill_color
        )
        if not isinstance(axis_label_fill_color, String):
            axis_label_fill_color_: String = String(
                axis_label_fill_color,
                variable_name_suffix=variable_name_suffix,
            )
        else:
            axis_label_fill_color_ = axis_label_fill_color
        self._axis_label_fill_color = axis_label_fill_color_