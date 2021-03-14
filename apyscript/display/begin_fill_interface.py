"""Class implementation for begin_fill method related interface.

See Also
--------
- graphics_clear_interface
"""


from typing import Union

from apyscript.color import color_util
from apyscript.converter import cast
from apyscript.type import Number
from apyscript.type import String
from apyscript.validation import color_validation
from apyscript.validation import number_validation


class BiginFillInterface:

    _fill_color: String
    _fill_alpha: Number

    def begin_fill(
            self, color: Union[str, String],
            alpha: Union[float, Number] = 1.0) -> None:
        """
        Set single color value for fill.

        Parameters
        ----------
        color : str or String
            Hexadecimal color string. e.g., '#00aaff'
        alpha : float or Number, default 1.0
            Color opacity (0.0 to 1.0).
        """
        if isinstance(color, String):
            color.value = color_util.complement_hex_color(
                hex_color_code=color.value)
        else:
            color = color_util.complement_hex_color(
                hex_color_code=color)
        self._fill_color.value = color
        number_validation.validate_num(num=alpha)
        if not isinstance(alpha, Number):
            alpha = cast.to_float_from_int(int_or_float=alpha)
        color_validation.validate_alpha_range(alpha=alpha)
        if isinstance(alpha, Number):
            self._fill_alpha.value = alpha.value
        else:
            self._fill_alpha.value = alpha

    @property
    def fill_color(self) -> String:
        """
        Get current fill color.

        Returns
        -------
        fill_color : str or None
            Current fill color (hexadecimal string, e.g., '#00aaff').
            If not be set, None will be returned.
        """
        return self._fill_color

    @property
    def fill_alpha(self) -> Number:
        """
        Get current fill color opacity.

        Returns
        -------
        fill_alpha : Number
            Current fill color opacity (0.0 to 1.0).
        """
        return self._fill_alpha
