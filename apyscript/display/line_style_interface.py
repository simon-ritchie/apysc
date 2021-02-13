"""Class implementation for line style related interface.
"""

from typing import Optional

from apyscript.color import color_util
from apyscript.validation import color_validation
from apyscript.validation import number_validation


class LineStyleInterface:

    _line_color: Optional[str] = None
    _line_thickness: Optional[int] = None
    _line_alpha: Optional[float] = None

    def line_style(
            self, color: str, thickness: int = 1,
            alpha: float = 1.0) -> None:
        """
        Set line style values.

        Parameters
        ----------
        color : str
            Hexadecimal color string. e.g., '#00aaff'
        thickness : int, default 1
            Line thickness (minimum value is 1).
        alpha : float, default 1.0
            Line color opacity (0.0 to 1.0).
        """
        color = color_util.complement_hex_color(hex_color_code=color)
        self._line_color = color
        number_validation.validate_integer(integer=thickness)
        number_validation.validate_num_is_gt_zero(num=thickness)
        self._line_thickness = thickness
        number_validation.validate_num(num=alpha)
        color_validation.validate_alpha_range(alpha=alpha)
        self._line_alpha = alpha
