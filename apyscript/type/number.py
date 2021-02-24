"""Class implementation of floating point number.
"""

from typing import Any
from typing import Union

from apyscript.converter import cast
from apyscript.expression import expression_variables_util
from apyscript.type.number_value_interface import NumberValueInterface
from apyscript.validation import number_validation


class Number(NumberValueInterface):

    def __init__(self, value: Union[int, float, Any]) -> None:
        """
        Floating point number class for this library.

        Parameters
        ----------
        value : int or float or Int or Number
            Initial floating point number value. If int or Int value
            is specified, that value will be cast to float.
        """
        self.variable_name = expression_variables_util.get_next_variable_name(
            type_name='number')
        if isinstance(value, NumberValueInterface):
            value.value = cast.to_float_from_int(int_or_float=value.value)
        super(Number, self).__init__(value=value)
        self._value = cast.to_float_from_int(int_or_float=self.value)
        self.append_constructor_expression()

    @property
    def value(self) -> float:
        """
        Get current floating point number value.

        Returns
        -------
        value : float
            Current number value.
        """
        return super(Number, self).value

    @value.setter
    def value(self, value: Union[int, float, Any]) -> None:
        """
        Set floating point number value.

        Parameters
        ----------
        value : int or float or Int or Number
            Any floating point number value to set. If int or Int
            value is specified, that value will be cast to float.
        """
        number_validation.validate_num(num=value)
        if isinstance(value, NumberValueInterface):
            value._value = cast.to_float_from_int(int_or_float=value._value)
            value_ = value._value
        else:
            value = cast.to_float_from_int(int_or_float=value)
            value_ = value
        self._value = value_
        self.append_value_setter_expression(value=value)
