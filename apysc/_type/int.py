"""Class implementation of integer.
"""

from typing import Any
from typing import Union

from apysc._type.number_value_interface import NumberValueInterface


class Int(NumberValueInterface):

    def __init__(self, value: Union[int, float, Any]) -> None:
        """
        Integer class for apysc library.

        Parameters
        ----------
        value : int or float or Int or Number
            Initial integer value. If float or Number value is specified,
            that value will be cast to integer.
        """
        from apysc._converter import cast
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        from apysc._expression.event_handler_scope import \
            TemporaryNotHandlerScope
        from apysc._type import type_util
        with TemporaryNotHandlerScope():
            is_number_specified: bool = type_util.is_number(
                value=value)
            TYPE_NAME: str = var_names.INT
            self.variable_name = expression_variables_util.\
                get_next_variable_name(type_name=TYPE_NAME)
            super(Int, self).__init__(value=value, type_name=TYPE_NAME)
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
        from apysc import append_js_expression
        if not is_number_specified:
            return
        expression: str = (
            f'{self.variable_name} = parseInt({self.variable_name}, 10);'
        )
        append_js_expression(expression=expression)

    def set_value_and_skip_expression_appending(
            self,
            value: Union[int, float, NumberValueInterface, Any]) -> None:
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
        number_validation.validate_num(num=value)  # type: ignore
        if isinstance(value, NumberValueInterface):
            value._value = cast.to_int_from_float(int_or_float=value._value)
            value_ = value._value
        else:
            value = cast.to_int_from_float(int_or_float=value)
            value_ = value
        self._value = value_  # type: ignore

    def __repr__(self) -> str:
        """
        Get a representation string of this instance.

        Returns
        -------
        repr_str : str
            Representation string of this instance.
        """
        repr_str: str = (
            f'Int({self._value})'
        )
        return repr_str
