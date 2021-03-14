"""Class implementation for line color interface.
"""

from typing import Union

from apyscript.color import color_util
from apyscript.expression import expression_file_util
from apyscript.html import html_util
from apyscript.type import String
from apyscript.type.variable_name_interface import VariableNameInterface


class LineColorInterface(VariableNameInterface):

    _line_color: String

    @property
    def line_color(self) -> Union[str, String]:
        """
        Get this instance's line color.

        Returns
        -------
        line_color : String
            Current line color (hexadecimal string, e.g., '#00aaff').
            If not be set, blank string will be returned.
        """
        return self._line_color

    @line_color.setter
    def line_color(self, value: Union[str, String]) -> None:
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

    def update_line_color_and_skip_appending_exp(
            self, value: Union[str, String]) -> None:
        """
        Update line color and skip appending expression to file.

        Parameters
        ----------
        value : str or String
            Line color to set.
        """
        if isinstance(value, String):
            value.value = color_util.complement_hex_color(
                hex_color_code=value.value)
        else:
            value = color_util.complement_hex_color(
                hex_color_code=value)
            value = String(value)
        self._line_color = value
