"""The mix-in class for the `from_rgb` method.
"""

from typing import Union, TYPE_CHECKING

from typing_extensions import final

from apysc._type.int import Int

if TYPE_CHECKING:
    from apysc._color.color import Color


class FromRgbMixIn:
    @final
    @classmethod
    def from_rgb(
        cls,
        *,
        red: Union[int, Int],
        green: Union[int, Int],
        blue: Union[int, Int],
        variable_name_suffix: str,
    ) -> "Color":
        from apysc._color.color import Color

        color: Color = Color("", variable_name_suffix=variable_name_suffix)
        color._value._value = _get_py_str_from_rgb(
            red=red, green=green, blue=blue
        )
        pass


def _get_py_str_from_rgb(
    *,
    red: Union[int, Int],
    green: Union[int, Int],
    blue: Union[int, Int],
) -> str:
    red_hex: str = _get_hex_str_from_int(color_int=red)
    pass


def _get_hex_str_from_int(*, color_int: Union[int, Int]) -> str:
    """
    Get a hexadecimal string from the specified integer value.

    Parameters
    ----------
    color_int : Union[int, Int]
        A color integer (0 to 255).

    Returns
    -------
    hex_str : str
        A hexadecimal string (e.g., "0F").
    """
    if isinstance(color_int, Int):
        hex_str: str = hex(color_int._value)
    else:
        hex_str = hex(color_int)
    hex_str = hex_str[2:].upper()
    hex_str = hex_str.zfill(2)
    return hex_str
