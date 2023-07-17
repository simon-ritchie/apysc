"""Mix-in class implementation for the `_set_initial_background_fill_color`
method.
"""

from typing import TypeVar

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.string import String
from apysc._validation import arg_validation_decos

_StrOrString = TypeVar("_StrOrString", str, String)


class SetInitialBackgroundFillColorMixIn:
    _background_fill_color: String

    @final
    @arg_validation_decos.is_hex_color_code_format(arg_position_index=1, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_background_fill_color(
        self,
        *,
        background_fill_color: _StrOrString,
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set a chart's initial background fill-color.

        Parameters
        ----------
        background_fill_color : str or String
            A chart's initial background fill-color.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        from apysc._color import color_util

        background_fill_color = color_util.complement_hex_color(
            hex_color_code=background_fill_color
        )
        if not isinstance(background_fill_color, String):
            background_fill_color_: String = String(
                background_fill_color,
                variable_name_suffix=variable_name_suffix,
            )
        else:
            background_fill_color_ = background_fill_color
        self._background_fill_color = background_fill_color_
