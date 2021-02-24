"""Class implementation for number value interface.
"""

from typing import Any
from typing import Union
from copy import deepcopy

from apyscript.expression import expression_file_util
from apyscript.html import html_util
from apyscript.type.variable_name_interface import VariableNameInterface
from apyscript.validation import number_validation
from apyscript.expression import expression_variables_util
from apyscript.type.type_name_interface import TypeNameInterface


class NumberValueInterface(VariableNameInterface, TypeNameInterface):

    _initial_value: Union[int, float, Any]
    _value: Union[int, float]

    def __init__(
            self, value: Union[int, float, Any], type_name: str) -> None:
        """
        Class for number value interface.

        Parameters
        ----------
        value : int or float or Int or Number
            Initial number value.
        type_name : str
            This instance expression's type name (e.g., int, number).
        """
        number_validation.validate_num(num=value)
        self._initial_value = value
        if isinstance(value, NumberValueInterface):
            value_ = value._value
        else:
            value_ = value
        self._value = value_
        self._type_name = type_name

    def append_constructor_expression(self) -> None:
        """
        Append current value's constructor expression to file.
        """
        if isinstance(self._initial_value, NumberValueInterface):
            value_: Union[int, float, str] = self._initial_value.variable_name
        else:
            value_ = self.value
        expression: str = (
            f'var {self.variable_name} = {value_};'
        )
        expression = html_util.wrap_expression_by_script_tag(
            expression=expression)
        expression_file_util.append_expression(expression=expression)

    @property
    def value(self) -> Union[int, float, Any]:
        """
        Get current number value.

        Returns
        -------
        value : int or float
            Current number value.
        """
        return self._value

    @value.setter
    def value(self, value: Union[int, float, Any]) -> None:
        """
        Set number value.

        Parameters
        ----------
        value : int or float or Int or Number
            Any number value to set.
        """
        number_validation.validate_num(num=value)
        if isinstance(value, NumberValueInterface):
            value_ = value._value
        else:
            value_ = value
        self._value = value_
        self.append_value_setter_expression(value=value)

    def append_value_setter_expression(
            self, value: Union[int, float, Any]) -> None:
        """
        Append value's setter expresion to file.

        Parameters
        ----------
        value : int or float or Int or Number
            Any number value to set.
        """
        if isinstance(value, NumberValueInterface):
            right_value: Union[str, int, float] = value.variable_name
        else:
            right_value = value
        expression: str = (
            f'{self.variable_name} = {right_value};'
        )
        expression = html_util.wrap_expression_by_script_tag(
            expression=expression)
        expression_file_util.append_expression(expression=expression)

    def copy(self) -> Any:
        """
        Make a deep copy of this instance.

        Returns
        -------
        result : NumberValueInterface
            Copied instance.
        """
        result: NumberValueInterface = deepcopy(self)
        result.variable_name = \
            expression_variables_util.get_next_variable_name(
                type_name=self.type_name)
        return result

    def __add__(self, other: Union[int, float, Any]) -> Any:
        """
        Method for addition.

        Parameters
        ----------
        other : int or float or Int or Number
            Other value to add.

        Returns
        -------
        result : NumberValueInterface
            Addition result value.
        """
        if isinstance(other, NumberValueInterface):
            value: Union[int, float, Any] = self._value + other.value
        else:
            value = self._value + other
        result: NumberValueInterface = deepcopy(self)
        result.value = value
        result.variable_name = \
            expression_variables_util.get_next_variable_name(
                type_name=self.type_name)
        return result
