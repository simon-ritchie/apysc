"""The color class implementation.
"""

from typing import TypeVar
from typing_extensions import final

from apysc._event.custom_event_mixin import CustomEventMixIn
from apysc._type.string import String
from apysc._validation import arg_validation_decos

_StrOrString = TypeVar("_StrOrString", str, String)


class Color(
    CustomEventMixIn,
):
    _value: String

    @arg_validation_decos.is_hex_color_code_format(arg_position_index=1, optional=False)
    def __init__(
        self,
        value: _StrOrString,
        *,
        variable_name_suffix: str = "",
    ) -> None:
        """
        The color class implementation.

        Parameters
        ----------
        value : str or String
            A hexadecimal color code string (e.g., '#000000').
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        from apysc._color import color_util

        value = color_util.complement_hex_color(hex_color_code=value)
        self._value = String(
            value=value,
            variable_name_suffix=variable_name_suffix,
        )
