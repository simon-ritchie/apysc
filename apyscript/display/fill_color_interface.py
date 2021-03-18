"""Class implementation for fill color interface.
"""


from apyscript.color import color_util
from apyscript.expression import expression_file_util
from apyscript.html import html_util
from apyscript.type import String
from apyscript.type import value_util
from apyscript.type.variable_name_interface import VariableNameInterface


class FillColorInterface(VariableNameInterface):

    _fill_color: String

    @property
    def fill_color(self) -> String:
        """
        Get this instance's fill color.

        Returns
        -------
        fill_color : String
            Current fill color (hexadecimal string, e.g., '#00aaff').
            If not be set, None will be returned.
        """
        self._initialize_fill_color_if_not_initialized()
        fill_color: String = value_util.get_copy(value=self._fill_color)
        return fill_color

    @fill_color.setter
    def fill_color(self, value: String) -> None:
        """
        Update this instance's fill color.

        Parameters
        ----------
        value : String
            Fill color to set.
        """
        self.update_fill_color_and_skip_appending_exp(value=value)
        self._append_fill_color_update_expression()

    def _append_fill_color_update_expression(self) -> None:
        """
        Append fill color updating expression.
        """
        expression: str = (
            f'{self.variable_name}.fill("{self.fill_color}");'
        )
        expression = html_util.wrap_expression_by_script_tag(
            expression=expression)
        expression_file_util.append_expression(
            expression=expression)

    def update_fill_color_and_skip_appending_exp(
            self, value: String) -> None:
        """
        Update fill color and skip appending expression to file.

        Parameters
        ----------
        value : String
            Fill color to set.
        """
        if isinstance(value, String):
            value_: str = color_util.complement_hex_color(
                hex_color_code=value.value)
        self._initialize_fill_color_if_not_initialized()
        self._fill_color.value = value_

    def _initialize_fill_color_if_not_initialized(self) -> None:
        """
        Initialize fill_color attribute if that value is not
        instantiated yet.
        """
        if hasattr(self, '_fill_color'):
            return
        self._fill_color = String('')
