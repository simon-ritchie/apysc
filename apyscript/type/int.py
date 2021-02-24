"""Class implementation of integer.
"""

from typing import Any, Union

from apyscript.type.number_value_interface import NumberValueInterface
from apyscript.converter import cast
from apyscript.expression import expression_variables_util
from apyscript.validation import number_validation


class Int(NumberValueInterface):

    def __init__(self, value: Union[int, float, Any]) -> None:
        """
        Integer class for this library.

        Parameters
        ----------
        value : int or float or Int or Number
            Initial integer value. If float or Number value is specified,
            that value will be cast to integer.
        """
        self.variable_name = expression_variables_util.get_next_variable_name(
            type_name='int')
        if isinstance(value, NumberValueInterface):
            value.value = cast.to_int_from_float(int_or_float=value.value)
        super(Int, self).__init__(value=value)
        self._value = cast.to_int_from_float(int_or_float=self.value)
        self.append_constructor_expression()

    @property
    def value(self) -> int:
        """
        Get current integer value.

        Returns
        -------
        value : int
            Current number value.
        """
        return super(Int, self).value  # type: ignore

    @value.setter
    def value(
            self,
            value: Union[int, float, Any]) -> None:  # type: ignore
        """
        Set integer value.

        Parameters
        ----------
        value : int or float or Int or Number
            Any integer value to set. If float or Number value is
            specified, that value will be cast to integer.
        """
        number_validation.validate_num(num=value)
        if isinstance(value, NumberValueInterface):
            value._value = cast.to_int_from_float(int_or_float=value._value)
            value_ = value._value
        else:
            value = cast.to_int_from_float(int_or_float=value)
            value_ = value
        self._value = value_
        self.append_value_setter_expression(value=value)
