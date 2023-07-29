"""The color class implementation.
"""

from typing import Any, TypeVar
from typing_extensions import final

from apysc._event.custom_event_mixin import CustomEventMixIn
from apysc._type.string import String
from apysc._validation import arg_validation_decos
from apysc._color.color_copy_mixin import ColorCopyMixIn

_StrOrString = TypeVar("_StrOrString", str, String)


class Color(
    CustomEventMixIn,
    ColorCopyMixIn["Color"],
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

    def __eq__(self, other: Any) -> bool:
        """
        Comparison method between two color values.

        Parameters
        ----------
        other : Any
            The other color value.

        Returns
        -------
        result : bool
            If the two color values are equal, this interface returns True.
        """
        if isinstance(other, str):
            raise TypeError(
                "The comparison between the `Color` class and `str` are not supported."
            )
        if isinstance(other, String):
            raise TypeError(
                "The comparison between the `Color` class and `String` "
                "are not supported."
            )
        if not isinstance(other, Color):
            return False
        return self._value._value == other._value._value
