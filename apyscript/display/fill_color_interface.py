"""Class implementation for fill color interface.
"""

from typing import Optional
from apyscript.display.variable_name_interface import VariableNameInterface
from apyscript.expression import expression_file_util
from apyscript.html import html_util
from apyscript.color import color_util


class FillColorInterface(VariableNameInterface):

    _fill_color: Optional[str] = None

    @property
    def fill_color(self) -> Optional[str]:
        """
        Get this instance's fill color.

        Returns
        -------
        fill_color : str or None
            Current fill color (hexadecimal string, e.g., '#00aaff').
            If not be set, None will be returned.
        """
        return self._fill_color

    @fill_color.setter
    def fill_color(self, value: str) -> None:
        """
        Update this instance's fill color.

        Parameters
        ----------
        value : int
            Fill color to set.
        """
        value = color_util.complement_hex_color(hex_color_code=value)
        self._fill_color = value
