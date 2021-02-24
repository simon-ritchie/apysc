"""Class implementation for number value interface.
"""

from typing import Any, Union
from apyscript.type.variable_name_interface import VariableNameInterface
from apyscript.validation import number_validation
from apyscript.expression import expression_file_util
from apyscript.html import html_util


class NumberValueInterface(VariableNameInterface):

    _value: Union[int, float]

    def __init__(self, value: Union[int, float, Any]) -> None:
        """
        Class for number value interface.

        Parameters
        ----------
        value : int or float or Int or Number
            Initial number value.
        """
        number_validation.validate_num(num=value)
        self._value = value

    def append_constructor_expression(self) -> None:
        """
        Append current value's constructor expression to file.
        """
        expression: str = (
            f'var {self.variable_name} = {self.value};'
        )
        expression = html_util.wrap_expression_by_script_tag(
            expression=expression)
        expression_file_util.append_expression(expression=expression)

    @property
    def value(self) -> Union[int, float]:
        """
        Get current number value.

        Returns
        -------
        value : int or float
            Current number value.
        """
        return self._value

    @value.setter
    def value(self, value_: Union[int, float, Any]) -> None:
        """
        Set number value.

        Parameters
        ----------
        value_ : int or float or Int or Number
            Any number value to set.
        """
        number_validation.validate_num(num=value_)
        if isinstance(value_, NumberValueInterface):
            value_ = value_._value
        self._value = value_
