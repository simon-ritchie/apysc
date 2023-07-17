"""The mix-in class implementation for the `tick_text_fill_color` value.
"""

from typing import TypeVar

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.string import String
from apysc._validation import arg_validation_decos

_StrOrString = TypeVar("_StrOrString", str, String)


class TickTextFillColorMixIn:
    _tick_text_fill_color: String

    @final
    @arg_validation_decos.is_hex_color_code_format(arg_position_index=1, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_tick_text_fill_color(
        self,
        *,
        tick_text_fill_color: _StrOrString,
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set an initial tick text fill color setting.

        Parameters
        ----------
        tick_text_fill_color : Union[str, String]
            A tick text fill-color setting.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        from apysc._color import color_util

        tick_text_fill_color = color_util.complement_hex_color(
            hex_color_code=tick_text_fill_color
        )
        if not isinstance(tick_text_fill_color, String):
            tick_text_fill_color_: String = String(
                tick_text_fill_color,
                variable_name_suffix=variable_name_suffix,
            )
        else:
            tick_text_fill_color_ = tick_text_fill_color
        self._tick_text_fill_color = tick_text_fill_color_
