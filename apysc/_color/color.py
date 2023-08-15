"""The color class implementation.
"""

from typing import Any, TypeVar
from typing_extensions import final

from apysc._event.custom_event_mixin import CustomEventMixIn
from apysc._type.string import String
from apysc._validation import arg_validation_decos
from apysc._color.color_copy_mixin import ColorCopyMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.boolean import Boolean

_StrOrString = TypeVar("_StrOrString", str, String)


class Color(
    CustomEventMixIn,
    ColorCopyMixIn["Color"],
):
    _value: String
    _variable_name_suffix: str

    @arg_validation_decos.is_hex_color_code_format(arg_position_index=1, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
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
        self._variable_name_suffix = variable_name_suffix

    @add_debug_info_setting(module_name=__name__)
    def __eq__(self, other: "Color") -> Any:
        """
        Comparison method between two color values.

        Parameters
        ----------
        other : Color
            The other color value.

        Returns
        -------
        result : Boolean
            If the two color values are equal, this interface returns True.
        """
        from apysc._expression import expression_data_util

        if isinstance(other, str):
            raise TypeError(
                "The comparison between the `Color` class and `str` are not supported."
            )
        if isinstance(other, String):
            raise TypeError(
                "The comparison between the `Color` class and `String` "
                "are not supported."
            )
        if isinstance(other, Color):
            result: Boolean = Boolean(
                self._value._value == other._value._value,
                variable_name_suffix=self._variable_name_suffix,
            )
        else:
            result = Boolean(
                False, variable_name_suffix=self._variable_name_suffix
            )
        if isinstance(other, Color):
            expression: str = (
                f"{result.variable_name} = {self._value.variable_name}"
                f" === {other._value.variable_name};"
            )
            expression_data_util.append_js_expression(expression=expression)

        return result

    def __repr__(self) -> str:
        """
        Get a representation string of this instance.

        Returns
        -------
        repr_str : str
            Representation string of this instance.
        """
        return f'Color("{self._value._value}")'
