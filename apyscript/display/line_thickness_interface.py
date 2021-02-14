"""Class implementation for line thickness interface.
"""

from typing import Optional

from apyscript.display.variable_name_interface import VariableNameInterface
from apyscript.expression import expression_file_util
from apyscript.html import html_util
from apyscript.validation import number_validation


class LineThicknessInterface(VariableNameInterface):

    _line_thickness: Optional[int] = None

    @property
    def line_thickness(self) -> Optional[int]:
        """
        Get this instance's line thickness.

        Parameters
        ----------
        line_thickness : int or None
            Current line thickness.
            If not be set, None will be returned.
        """
        return self._line_thickness

    @line_thickness.setter
    def line_thickness(self, value: int) -> None:
        """
        Update this instance's line thickness.

        Parameters
        ----------
        value : int
            Line thickness to set.
        """
        number_validation.validate_integer(integer=value)
        number_validation.validate_num_is_gte_zero(num=value)
        self._line_thickness = value
