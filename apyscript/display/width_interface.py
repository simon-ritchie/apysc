"""Class implementation for witdth interface.
"""

from apyscript.converter import cast
from apyscript.expression import expression_file_util
from apyscript.html import html_util
from apyscript.type.variable_name_interface import VariableNameInterface
from apyscript.validation import size_validation


class WidthInterface(VariableNameInterface):

    _width: int

    @property
    def width(self) -> int:
        """
        Get this instance's width.

        Returns
        -------
        width : int
            This instance's width.
        """
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        """
        Update this instance's width.

        Parameters
        ----------
        value : int
            Width value to set.
        """
        self.update_width_and_skip_appending_exp(value=value)
        self._append_width_update_expression()

    def _append_width_update_expression(self) -> None:
        """
        Append width updating expression.
        """
        expression: str = (
            f'{self.variable_name}.width({self.width});'
        )
        expression = html_util.wrap_expression_by_script_tag(
            expression=expression)
        expression_file_util.append_expression(
            expression=expression)

    def update_width_and_skip_appending_exp(self, value: int) -> None:
        """
        Update width value and skip appending expression to file.

        Parameters
        ----------
        value : int
            Width value to set.
        """
        value = cast.to_int_from_float(int_or_float=value)
        size_validation.validate_size_is_int(size=value)
        size_validation.validate_size_is_gte_zero(size=value)
        self._width = value
