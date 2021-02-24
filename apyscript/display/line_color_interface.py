"""Class implementation for line color interface.
"""

from typing import Optional

from apyscript.color import color_util
from apyscript.expression import expression_file_util
from apyscript.html import html_util
from apyscript.type.variable_name_interface import VariableNameInterface


class LineColorInterface(VariableNameInterface):

    _line_color: Optional[str] = None

    @property
    def line_color(self) -> Optional[str]:
        """
        Get this instance's line color.

        Returns
        -------
        line_color : str or None
            Current line color (hexadecimal string, e.g., '#00aaff').
            If not be set, None will be returned.
        """
        return self._line_color

    @line_color.setter
    def line_color(self, value: str) -> None:
        """
        Update this instance's line color.

        Parameters
        ----------
        value : str
            Line color to set.
        """
        self.update_line_color_and_skip_appending_exp(value=value)
        self._append_line_color_update_expression()

    def _append_line_color_update_expression(self) -> None:
        """
        Append line color updating expression.
        """
        expression: str = (
            f'{self.variable_name}.stroke("{self.line_color}");'
        )
        expression = html_util.wrap_expression_by_script_tag(
            expression=expression)
        expression_file_util.append_expression(
            expression=expression)

    def update_line_color_and_skip_appending_exp(self, value: str) -> None:
        """
        Update line color and skip appending expression to file.

        Parameters
        ----------
        value : str
            Line color to set.
        """
        value = color_util.complement_hex_color(hex_color_code=value)
        self._line_color = value
