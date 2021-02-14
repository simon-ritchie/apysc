"""Class implementation for line alpha interface.
"""

from typing import Optional

from apyscript.display.variable_name_interface import VariableNameInterface
from apyscript.expression import expression_file_util
from apyscript.html import html_util
from apyscript.validation import number_validation
from apyscript.validation import color_validation


class LineAlphaInterface(VariableNameInterface):

    _line_alpha: Optional[float] = None

    @property
    def line_alpha(self) -> Optional[float]:
        """
        Get this instance's line alpha (opacity).

        Returns
        -------
        line_alpha : float or None
            Current line alpha (opacity. 0.0 to 1.0).
            If not be set, None will be returned.
        """
        return self._line_alpha

    @line_alpha.setter
    def line_alpha(self, value: float) -> None:
        """
        Update this instance's line alpha (opacity).

        Parameters
        ----------
        value : float
            Line alpha (opacity) to set.
        """
        number_validation.validate_num(num=value)
        color_validation.validate_alpha_range(alpha=value)
        self._line_alpha = value
