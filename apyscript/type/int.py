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
        super(Int, self).__init__(value=value)
        self._value = cast.to_int_from_float(int_or_float=self.value)
        self.variable_name = expression_variables_util.get_next_variable_name(
            type_name='int')

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
            value_: Union[int, float, Any]) -> None:  # type: ignore
        """
        Set integer value.

        Parameters
        ----------
        value_ : int or float or Int or Number
            Any integer value to set. If float or Number value is
            specified, that value will be cast to integer.
        """
        number_validation.validate_num(num=value_)
        if isinstance(value_, NumberValueInterface):
            value_ = value_._value
        self._value = value_
        self._value = cast.to_int_from_float(int_or_float=self.value)
