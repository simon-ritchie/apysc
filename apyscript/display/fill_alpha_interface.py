"""Class implementation for fill alpha interface.
"""

from typing import Any
from typing import Optional

from apyscript.converter import cast
from apyscript.expression import expression_file_util
from apyscript.html import html_util
from apyscript.type import Number
from apyscript.type import value_util
from apyscript.type.number_value_interface import NumberValueInterface
from apyscript.type.variable_name_interface import VariableNameInterface
from apyscript.validation import color_validation
from apyscript.validation import number_validation


class FillAlphaInterface(VariableNameInterface):

    _fill_alpha: Number

    @property
    def fill_alpha(self) -> Optional[Number]:
        """
        Get this instance's fill opacity.

        Returns
        -------
        fill_alpha : Number or None
            Current fill opacity (0.0 to 1.0).
            If not be set, None will be returned.
        """
        return value_util.get_copy(value=self._fill_alpha)

    @fill_alpha.setter
    def fill_alpha(
            self, value: Number) -> None:
        """
        Update this instance's fill opacity.

        Parameters
        ----------
        value : float or Number
            Fill opacity to set.
        """
        if not isinstance(value, NumberValueInterface):
            value = Number(value=value)
        self.update_fill_alpha_and_skip_appending_exp(value=value)
        self._append_fill_alpha_update_expression()

    def _append_fill_alpha_update_expression(self) -> None:
        """
        Append fill alpha updating expression.
        """
        value_str: str = value_util.get_value_str_for_expression(
            value=self._fill_alpha)
        expression: str = (
            f'{self.variable_name}.fill({{opacity: {value_str}}});'
        )
        expression = html_util.wrap_expression_by_script_tag(
            expression=expression)
        expression_file_util.append_expression(
            expression=expression)

    def update_fill_alpha_and_skip_appending_exp(
            self, value: Any) -> None:
        """
        Update fill opacity and skip appending expression to file.

        Parameters
        ----------
        value : float or Number
            Fill opacity to set.
        """
        number_validation.validate_num(num=value)
        if not isinstance(value, Number):
            value = cast.to_float_from_int(int_or_float=value)
            color_validation.validate_alpha_range(alpha=value)
            value = Number(value=value)
        color_validation.validate_alpha_range(alpha=value.value)
        self._fill_alpha = value
