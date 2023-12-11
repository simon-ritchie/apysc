# pyright: reportIncompatibleMethodOverride=false

"""The color class implementation.
"""

from typing import Any
from typing import TypeVar

from apysc._color.blue_color_mixin import BlueColorMixIn
from apysc._color.color_copy_mixin import ColorCopyMixIn
from apysc._color.from_rgb_mixin import FromRgbMixIn
from apysc._color.green_color_mixin import GreenColorMixIn
from apysc._color.red_color_mixin import RedColorMixIn
from apysc._event.custom_event_mixin import CustomEventMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.boolean import Boolean
from apysc._type.string import String
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos

_StrOrString = TypeVar("_StrOrString", str, String)


class Color(
    CustomEventMixIn,
    ColorCopyMixIn["Color"],
    VariableNameMixIn,
    VariableNameSuffixMixIn,
    VariableNameSuffixAttrOrVarMixIn,
    FromRgbMixIn,
    RedColorMixIn,
    GreenColorMixIn,
    BlueColorMixIn,
):
    """
    The color class implementation.

    References
    ----------
    - Color class
        - https://simon-ritchie.github.io/apysc/en/color.html
    - Colors class
        - https://simon-ritchie.github.io/apysc/en/colors.html
    - MaterialDesignColors class
        - https://simon-ritchie.github.io/apysc/en/material_design_colors.html
    - COLORLESS constant
        - https://simon-ritchie.github.io/apysc/en/colorless.html
    - Color class from_rgb class method
        - https://simon-ritchie.github.io/apysc/en/color_from_rgb.html
    - Color class red_color property
        - https://simon-ritchie.github.io/apysc/en/red_color.html
    - Color class green_color property
        - https://simon-ritchie.github.io/apysc/en/green_color.html
    - Color class blue_color property
        - https://simon-ritchie.github.io/apysc/en/blue_color.html

    Examples
    --------
    >>> import apysc as ap
    >>> color: ap.Color = ap.Color("#0af")
    >>> color
    Color("#00aaff")

    >>> color = ap.Color("#ffffff")
    >>> color
    Color("#ffffff")
    """

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
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        References
        ----------
        - Color class
            - https://simon-ritchie.github.io/apysc/en/color.html
        - Colors class
            - https://simon-ritchie.github.io/apysc/en/colors.html
        - MaterialDesignColors class
            - https://simon-ritchie.github.io/apysc/en/material_design_colors.html
        - COLORLESS constant
            - https://simon-ritchie.github.io/apysc/en/colorless.html
        - Color class from_rgb class method
            - https://simon-ritchie.github.io/apysc/en/color_from_rgb.html
        - Color class red_color property
            - https://simon-ritchie.github.io/apysc/en/red_color.html
        - Color class green_color property
            - https://simon-ritchie.github.io/apysc/en/green_color.html
        - Color class blue_color property
            - https://simon-ritchie.github.io/apysc/en/blue_color.html

        Examples
        --------
        >>> import apysc as ap
        >>> color: ap.Color = ap.Color("#0af")
        >>> color
        Color("#00aaff")

        >>> color = ap.Color("#ffffff")
        >>> color
        Color("#ffffff")
        """
        from apysc._color import color_util

        value = color_util.complement_hex_color(hex_color_code=value)
        self._value = String(
            value=value,
            variable_name_suffix=variable_name_suffix,
        )
        self._variable_name_suffix = variable_name_suffix
        self._variable_name = self._value._variable_name

    @add_debug_info_setting(module_name=__name__)
    def __eq__(self, other: Any) -> Any:
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
            result = Boolean(False, variable_name_suffix=self._variable_name_suffix)
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
        if not hasattr(self, "_value"):
            return 'Color("")'
        return f'Color("{self._value._value}")'
