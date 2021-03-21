"""Class implementation for line thickness interface.
"""

from apyscript.type import Int
from apyscript.type.variable_name_interface import VariableNameInterface


class LineThicknessInterface(VariableNameInterface):

    _line_thickness: Int

    def _initialize_line_thickness_if_not_initialized(self) -> None:
        """
        Initialize _line_thickness attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_line_thickness'):
            return
        self._line_thickness = Int(1)

    @property
    def line_thickness(self) -> Int:
        """
        Get this instance's line thickness.

        Returns
        -------
        line_thickness : Int
            Current line thickness.
        """
        from apyscript.type import value_util
        return value_util.get_copy(value=self._line_thickness)

    @line_thickness.setter
    def line_thickness(self, value: Int) -> None:
        """
        Update this instance's line thickness.

        Parameters
        ----------
        value : Int
            Line thickness to set.
        """
        self.update_line_thickness_and_skip_appending_exp(value=value)
        self._append_line_thickness_update_expression()

    def _append_line_thickness_update_expression(self) -> None:
        """
        Append line thickness update expression.
        """
        from apyscript.expression import expression_file_util
        from apyscript.html import html_util
        expression: str = (
            f'{self.variable_name}.attr({{"stroke-width": '
            f'{self.line_thickness}}});'
        )
        expression = html_util.wrap_expression_by_script_tag(
            expression=expression)
        expression_file_util.append_expression(
            expression=expression)

    def update_line_thickness_and_skip_appending_exp(
            self, value: Int) -> None:
        """
        Update line thickness and skip appending expression to file.

        Parameters
        ----------
        value : Int
            Line thickness to set.
        """
        from apyscript.validation import number_validation
        number_validation.validate_integer(integer=value)
        number_validation.validate_num_is_gte_zero(num=value)
        self._line_thickness = value
