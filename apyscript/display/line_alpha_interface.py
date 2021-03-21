"""Class implementation for line alpha interface.
"""

from apyscript.type import Number
from apyscript.type.variable_name_interface import VariableNameInterface


class LineAlphaInterface(VariableNameInterface):

    _line_alpha: Number

    def _initialize_line_alpha_if_not_initialized(self) -> None:
        """
        Initialize _line_alpha attribute if it is not initialized yet.
        """
        if hasattr(self, '_line_alpha'):
            return
        self._line_alpha = Number(1.0)

    @property
    def line_alpha(self) -> Number:
        """
        Get this instance's line alpha (opacity).

        Returns
        -------
        line_alpha : Number
            Current line alpha (opacity. 0.0 to 1.0).
        """
        from apyscript.type import value_util
        return value_util.get_copy(value=self._line_alpha)

    @line_alpha.setter
    def line_alpha(self, value: Number) -> None:
        """
        Update this instance's line alpha (opacity).

        Parameters
        ----------
        value : Number
            Line alpha (opacity) to set.
        """
        self.update_line_alpha_and_skip_appending_exp(value=value)
        self._append_line_alpha_update_expression()

    def _append_line_alpha_update_expression(self) -> None:
        """
        Append line alpha updating expression.
        """
        from apyscript.expression import expression_file_util
        from apyscript.html import html_util
        expression: str = (
            f'{self.variable_name}.stroke({{opacity: {self.line_alpha}}});'
        )
        expression = html_util.wrap_expression_by_script_tag(
            expression=expression)
        expression_file_util.append_expression(
            expression=expression)

    def update_line_alpha_and_skip_appending_exp(
            self, value: Number) -> None:
        """
        Update line alpha and skip appending expression to file.

        Parameters
        ----------
        value : Number
            Line alpha (opacity) to set.
        """
        from apyscript.validation import color_validation
        from apyscript.validation import number_validation
        number_validation.validate_num(num=value)
        color_validation.validate_alpha_range(alpha=value)
        self._line_alpha = value
