"""The mix-in class for the `from_rgb` method.
"""

from typing import TYPE_CHECKING
from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._validation import arg_validation_decos

if TYPE_CHECKING:
    from apysc._color.color import Color


class FromRgbMixIn:
    @final
    @classmethod
    @arg_validation_decos.is_uint8_range(arg_position_index=1)
    @arg_validation_decos.is_uint8_range(arg_position_index=2)
    @arg_validation_decos.is_uint8_range(arg_position_index=3)
    @arg_validation_decos.is_builtin_string(arg_position_index=4, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def from_rgb(
        cls,
        *,
        red: Union[int, Int],
        green: Union[int, Int],
        blue: Union[int, Int],
        variable_name_suffix: str = "",
    ) -> "Color":
        """
        Create a color instance from RGB (red, green, and blue) values.

        Parameters
        ----------
        red : Union[int, Int]
            A red color value (0 to 255).
        green : Union[int, Int]
            A green color value (0 to 255).
        blue : Union[int, Int]
            A blue color value (0 to 255).
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        color : Color
            A created color instance.

        References
        ----------
        - Color class from_rgb class method
            - https://simon-ritchie.github.io/apysc/en/color_from_rgb.html
        - Color class
            - https://simon-ritchie.github.io/apysc/en/color.html

        Examples
        --------
        >>> import apysc as ap
        >>> color: ap.Color = ap.Color.from_rgb(red=0, green=255, blue=0)
        >>> color
        Color("#00FF00")
        """
        from apysc._color import color_util
        from apysc._color.color import Color
        from apysc._expression import expression_data_util
        from apysc._type.string import String

        color: Color = Color("", variable_name_suffix=variable_name_suffix)
        color._value._value = _get_py_str_from_rgb(red=red, green=green, blue=blue)
        red_hex_str: String = color_util.get_hex_apysc_string_from_int(
            color_int=red, variable_name_suffix=variable_name_suffix
        )
        green_hex_str: String = color_util.get_hex_apysc_string_from_int(
            color_int=green, variable_name_suffix=variable_name_suffix
        )
        blue_hex_str: String = color_util.get_hex_apysc_string_from_int(
            color_int=blue, variable_name_suffix=variable_name_suffix
        )
        color._value._value = (
            f"#{red_hex_str._value}{green_hex_str._value}{blue_hex_str._value}"
        )
        expression: str = (
            f'{color._value.variable_name} = "#" + {red_hex_str.variable_name}'
            f" + {green_hex_str.variable_name} + {blue_hex_str.variable_name};"
        )
        expression_data_util.append_js_expression(expression=expression)
        return color


def _get_py_str_from_rgb(
    *,
    red: Union[int, Int],
    green: Union[int, Int],
    blue: Union[int, Int],
) -> str:
    """
    Get a Python string from RGB values.

    Parameters
    ----------
    red : Union[int, Int]
        The red color.
    green : Union[int, Int]
        The green color.
    blue : Union[int, Int]
        The blue color.

    Returns
    -------
    py_str : str
        A Python string, e.g., '#0000ff'.
    """
    from apysc._color import color_util

    red_hex: str = color_util.get_hex_str_from_int(color_int=red)
    green_hex: str = color_util.get_hex_str_from_int(color_int=green)
    blue_hex: str = color_util.get_hex_str_from_int(color_int=blue)
    return f"#{red_hex}{green_hex}{blue_hex}"
