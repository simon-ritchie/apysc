"""Class implementation of integer.
"""

from typing import Any, Union

from apyscript.type.number_value_interface import NumberValueInterface


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
