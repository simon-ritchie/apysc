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
        Floating point number class for apyscript library.

        Parameters
        ----------
        value : int or float or Int or Number
            Initial floating point number value. If int or Int value
            is specified, that value will be cast to float.
        """
        type_name: str = 'number'
        self.variable_name = expression_variables_util.get_next_variable_name(
            type_name=type_name)
        super(Number, self).__init__(value=value, type_name=type_name)
        self._value = cast.to_float_from_int(int_or_float=self.value)
        self.append_constructor_expression()

    def set_value_and_skip_expression_appending(
            self, value: Union[int, float, Any]) -> None:
        """
        Update value attribute and skip expression appending.

        Parameters
        ----------
        value : int or float or Int or Number
            Any number value to set. If float or Number value is specified,
            that value will be cast to integer.
        """
        number_validation.validate_num(num=value)
        if isinstance(value, NumberValueInterface):
            value._value = cast.to_float_from_int(int_or_float=value._value)
            value_ = value._value
        else:
            value = cast.to_float_from_int(int_or_float=value)
            value_ = value
        self._value = value_
