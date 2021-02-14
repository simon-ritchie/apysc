"""Class implementation for fill alpha interface.
"""

from typing import Optional

from apyscript.color import color_util
from apyscript.display.variable_name_interface import VariableNameInterface
from apyscript.expression import expression_file_util
from apyscript.html import html_util
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
        number_validation.validate_num(num=value)
        color_validation.validate_alpha_range(alpha=value)
        self._fill_alpha = value
