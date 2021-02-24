"""Class implementation of floating point number.
"""

from typing import Any, Union

from apyscript.type.number_value_interface import NumberValueInterface


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
        super(Number, self).__init__(value=value)
