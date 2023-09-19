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
