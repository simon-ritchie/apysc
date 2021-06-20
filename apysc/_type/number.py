"""Class implementation of floating point number.
"""

from typing import Any
from typing import Union

from apysc._type.number_value_interface import NumberValueInterface


class Number(NumberValueInterface):

    def __init__(self, value: Union[int, float, Any]) -> None:
        """
        Floating point number class for apysc library.

        Parameters
        ----------
        value : int or float or Int or Number
            Initial floating point number value. If int or Int value
            is specified, that value will be cast to float.
        """
        from apysc._converter import cast
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        from apysc._expression.event_handler_scope import \
            TemporaryNotHandlerScope
        with TemporaryNotHandlerScope():
            TYPE_NAME: str = var_names.NUMBER
            self.variable_name = expression_variables_util.\
                get_next_variable_name(type_name=TYPE_NAME)
            super(Number, self).__init__(value=value, type_name=TYPE_NAME)
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
        from apysc._converter import cast
        from apysc._validation import number_validation
        number_validation.validate_num(num=value)
        if isinstance(value, NumberValueInterface):
            value._value = cast.to_float_from_int(int_or_float=value._value)
            value_ = value._value
        else:
            value = cast.to_float_from_int(int_or_float=value)
            value_ = value
        self._value = value_

    def __repr__(self) -> str:
        """
        Get a representation string of this instance.

        Returns
        -------
        repr_str : str
            Representation string of this instance.
        """
        repr_str: str = (
            f'Number({self._value})'
        )
        return repr_str
