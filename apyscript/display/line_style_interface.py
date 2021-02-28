"""Class implementation for line style related interface.

See Also
--------
- graphics_clear_interface
"""

from typing import Optional
from typing import Union

from apyscript.color import color_util
from apyscript.converter import cast
from apyscript.type.int import Int
from apyscript.validation import color_validation
from apyscript.validation import number_validation


class LineStyleInterface:

    _line_color: Optional[str] = None
    _line_thickness: Int
    _line_alpha: Optional[float] = None

    def line_style(
            self, color: str,
            thickness: Union[int, Int] = 1,
            alpha: float = 1.0) -> None:
        """
        Set line style values.

        Parameters
        ----------
        color : str
            Hexadecimal color string. e.g., '#00aaff'
        thickness : int or Int, default 1
            Line thickness (minimum value is 1).
        alpha : float, default 1.0
            Line color opacity (0.0 to 1.0).
        """
        color = color_util.complement_hex_color(hex_color_code=color)
        self._line_color = color
        number_validation.validate_integer(integer=thickness)
        number_validation.validate_num_is_gt_zero(num=thickness)
        self._line_thickness = Int(thickness)
        number_validation.validate_num(num=alpha)
        alpha = cast.to_float_from_int(int_or_float=alpha)
        color_validation.validate_alpha_range(alpha=alpha)
        self._line_alpha = alpha

    @property
    def line_color(self) -> Optional[str]:
        """
        Get current line color.

        Returns
        -------
        line_color : str or None
            Current line color (hexadecimal string, e.g., '#00aaff').
            If not be set, None will be returned.
        """
        return self._line_color

    @property
    def line_thickness(self) -> Int:
        """
        Get current line thickness.

        Returns
        -------
        line_thickness : Int
            Current line thickness.
        """
        return self._line_thickness

    @property
    def line_alpha(self) -> Optional[float]:
        """
        Get current line color opacity.

        Returns
        -------
        line_alpha : float or None
            Current line opacity (0.0 to 1.0).
            If not be set, None will be returned.
        """
        return self._line_alpha
