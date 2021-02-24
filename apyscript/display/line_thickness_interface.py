"""Class implementation for line thickness interface.
"""

from typing import Optional

from apyscript.expression import expression_file_util
from apyscript.html import html_util
from apyscript.type.variable_name_interface import VariableNameInterface
from apyscript.validation import number_validation


class LineThicknessInterface(VariableNameInterface):

    _line_thickness: Optional[int] = None

    @property
    def line_thickness(self) -> Optional[int]:
        """
        Get this instance's line thickness.

        Returns
        -------
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
        self.update_line_thickness_and_skip_appending_exp(value=value)
        self._append_line_thickness_update_expression()

    def _append_line_thickness_update_expression(self) -> None:
        """
        Append line thickness update expression.
        """
        expression: str = (
            f'{self.variable_name}.attr({{"stroke-width": '
            f'{self.line_thickness}}});'
        )
        expression = html_util.wrap_expression_by_script_tag(
            expression=expression)
        expression_file_util.append_expression(
            expression=expression)

    def update_line_thickness_and_skip_appending_exp(
            self, value: int) -> None:
        """
        Update line thickness and skip appending expression to file.

        Parameters
        ----------
        value : int
            LKine thickness to set.
        """
        number_validation.validate_integer(integer=value)
        number_validation.validate_num_is_gte_zero(num=value)
        self._line_thickness = value
