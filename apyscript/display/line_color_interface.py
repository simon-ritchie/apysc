"""Class implementation for line color interface.
"""


from apyscript.color import color_util
from apyscript.expression import expression_file_util
from apyscript.html import html_util
from apyscript.type import String
from apyscript.type import value_util
from apyscript.type.variable_name_interface import VariableNameInterface


class LineColorInterface(VariableNameInterface):

    _line_color: String

    @property
    def line_color(self) -> String:
        """
        Get this instance's line color.

        Returns
        -------
        line_color : String
            Current line color (hexadecimal string, e.g., '#00aaff').
            If not be set, blank string will be returned.
        """
        self._initialize_line_color_if_not_initialized()
        line_color: String = value_util.get_copy(value=self._line_color)
        return line_color

    @line_color.setter
    def line_color(self, value: String) -> None:
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
            self, value: String) -> None:
        """
        Update line color and skip appending expression to file.

        Parameters
        ----------
        value : String
            Line color to set.
        """
        value.value = color_util.complement_hex_color(
            hex_color_code=value.value)
        self._initialize_line_color_if_not_initialized()
        self._line_color = value

    def _initialize_line_color_if_not_initialized(self) -> None:
        """
        Initialize line_color attribute if that value is not
        initialized yet.
        """
        if hasattr(self, '_line_color'):
            return
        self._line_color = String('')
