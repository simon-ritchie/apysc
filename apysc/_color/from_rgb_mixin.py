"""The mix-in class for the `from_rgb` method.
"""

from typing import Union, TYPE_CHECKING

from typing_extensions import final

from apysc._type.int import Int
from apysc._validation import arg_validation_decos
from apysc._html.debug_mode import add_debug_info_setting

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
        from apysc._color.color import Color
        from apysc._type.string import String
        from apysc._color import color_util
        from apysc._expression import expression_data_util

        color: Color = Color("", variable_name_suffix=variable_name_suffix)
        color._value._value = _get_py_str_from_rgb(
            red=red, green=green, blue=blue
        )
        red_hex_str: String = color_util.get_hex_apysc_string_from_int(
            color_int=red, variable_name_suffix=variable_name_suffix
        ).upper()
        green_hex_str: String = color_util.get_hex_apysc_string_from_int(
            color_int=green, variable_name_suffix=variable_name_suffix
        ).upper()
        blue_hex_str: String = color_util.get_hex_apysc_string_from_int(
            color_int=blue, variable_name_suffix=variable_name_suffix
        ).upper()
        color._value._value = (
            f"#{red_hex_str._value}{green_hex_str._value}{blue_hex_str._value}"
        )
        expression: str = (
            f'{color._value.variable_name} = "#" + {red_hex_str.variable_name}'
            f' + {green_hex_str.variable_name} + {blue_hex_str.variable_name};'
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
