"""Class implementation for fill color related interface.
"""


from typing import Optional

from apyscript.color import color_util


class FillColorInterface:

    _fill_color: Optional[str] = None

    def begin_fill(self, color: str) -> None:
        """
        Set single color value for fill.

        Parameters
        ----------
        color : str
            Hexadecimal color string. e.g., '#00aaff'
        """
        color = color_util.complement_hex_color(hex_color_code=color)
        self._fill_color = color

    @property
    def fill_color(self) -> Optional[str]:
        """
        Get current fill color.

        Returns
        -------
        fill_color : str
            Current fill color (hexadecimal string, e.g., '#00aaff').
            If not be set, None will be returned.
        """
        return self._fill_color
