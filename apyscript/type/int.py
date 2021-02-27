"""Class implementation of integer.
"""

from typing import Any
from typing import Union

from apyscript.converter import cast
from apyscript.expression import expression_file_util
from apyscript.expression import expression_variables_util
from apyscript.type import type_util
from apyscript.type.number_value_interface import NumberValueInterface
from apyscript.validation import number_validation


class Int(NumberValueInterface):

    def __init__(self, value: Union[int, float, Any]) -> None:
        """
        Integer class for apyscript library.

        Parameters
        ----------
        value : int or float or Int or Number
            Initial integer value. If float or Number value is specified,
            that value will be cast to integer.
        """
        is_number_specified: bool = type_util.is_number(
            value=value)
        type_name: str = 'int'
        self.variable_name = expression_variables_util.get_next_variable_name(
            type_name=type_name)
        super(Int, self).__init__(value=value, type_name=type_name)
        self._value = cast.to_int_from_float(int_or_float=self.value)
        self.append_constructor_expression()
        self._append_cast_expression(
            is_number_specified=is_number_specified)

    def _append_cast_expression(
            self, is_number_specified: bool) -> None:
        """
        Append integer cast (parseInt) expression to file.

        Parameters
        ----------
        is_number_specified : bool
            Boolean value whether a specified value is Number
            instance or not.
        """
        if not is_number_specified:
            return
        expression: str = (
            f'{self.variable_name} = parseInt({self.variable_name}, 10);'
        )
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)

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
            value._value = cast.to_int_from_float(int_or_float=value._value)
            value_ = value._value
        else:
            value = cast.to_int_from_float(int_or_float=value)
            value_ = value
        self._value = value_
