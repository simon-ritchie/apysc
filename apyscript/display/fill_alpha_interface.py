"""Class implementation for fill alpha interface.
"""

from typing import Optional
from typing import Union

from apyscript.converter import cast
from apyscript.expression import expression_file_util
from apyscript.html import html_util
from apyscript.type.number import Number
from apyscript.type.variable_name_interface import VariableNameInterface
from apyscript.validation import color_validation
from apyscript.validation import number_validation


class FillAlphaInterface(VariableNameInterface):

    _fill_alpha: Optional[float] = None

    @property
    def fill_alpha(self) -> Optional[float]:
        """
        Get this instance's fill opacity.

        Returns
        -------
        fill_alpha : float or None
            Current fill opacity (0.0 to 1.0).
            If not be set, None will be returned.
        """
        return self._fill_alpha

    @fill_alpha.setter
    def fill_alpha(self, value: float) -> None:
        """
        Update this instance's fill opacity.

        Parameters
        ----------
        value : float
            Fill opacity to set.
        """
        self.update_fill_alpha_and_skip_appending_exp(value=value)
        self._append_fill_alpha_update_expression()

    def _append_fill_alpha_update_expression(self) -> None:
        """
        Append fill alpha updating expression.
        """
        expression: str = (
            f'{self.variable_name}.fill({{opacity: {self.fill_alpha}}});'
        )
        expression = html_util.wrap_expression_by_script_tag(
            expression=expression)
        expression_file_util.append_expression(
            expression=expression)

    def update_fill_alpha_and_skip_appending_exp(
            self, value: Union[float, Number]) -> None:
        """
        Update fill opacity and skip appending expression to file.

        Parameters
        ----------
        value : float
            Fill opacity to set.
        """
        number_validation.validate_num(num=value)
        if not isinstance(value, Number):
            value = cast.to_float_from_int(int_or_float=value)
        else:
            value = value.value
        color_validation.validate_alpha_range(alpha=value)
        self._fill_alpha = value
