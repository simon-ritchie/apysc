"""Class implementation of integer.
"""

from typing import Union

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number_value_interface import NumberValueInterface
from apysc._validation import arg_validation_decos


class Int(NumberValueInterface[int, 'Int']):
    """
    Integer class for the apysc library.

    References
    ----------
    - Int and Number document
        - https://simon-ritchie.github.io/apysc/int_and_number.html
    - Int and Number common arithmetic operations document
        - https://simon-ritchie.github.io/apysc/int_and_number_arithmetic_operations.html  # noqa
    - Int and Number common comparison operations document
        - https://simon-ritchie.github.io/apysc/int_and_number_comparison_operations.html  # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> int_val: ap.Int = ap.Int(10)
    >>> int_val
    Int(10)

    >>> int_val == 10
    Boolean(True)

    >>> int_val == ap.Int(10)
    Boolean(True)

    >>> int_val >= 10
    Boolean(True)

    >>> int_val += 10
    >>> int_val
    Int(20)

    >>> int_val = ap.Int(10.5)
    >>> int_val
    Int(10)
    """

    @arg_validation_decos.is_num(arg_position_index=1)
    @add_debug_info_setting(
        module_name=__name__, class_name='Int')
    def __init__(
            self, value: Union[int, float, NumberValueInterface]) -> None:
        """
        Integer class for apysc library.

        Parameters
        ----------
        value : int or float or Int or Number
            Initial integer value. If the `float` or `Number`
            value is specified, this class casts it to an integer.

        References
        ----------
        - Int and Number document
            - https://simon-ritchie.github.io/apysc/int_and_number.html
        - Int and Number common arithmetic operations document
            - https://simon-ritchie.github.io/apysc/int_and_number_arithmetic_operations.html  # noqa
        - Int and Number common comparison operations document
            - https://simon-ritchie.github.io/apysc/int_and_number_comparison_operations.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> int_val: ap.Int = ap.Int(10)
        >>> int_val
        Int(10)

        >>> int_val == 10
        Boolean(True)

        >>> int_val == ap.Int(10)
        Boolean(True)

        >>> int_val >= 10
        Boolean(True)

        >>> int_val += 10
        >>> int_val
        Int(20)

        >>> int_val = ap.Int(10.5)
        >>> int_val
        Int(10)
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

    @add_debug_info_setting(
        module_name=__name__, class_name='Int')
    def _append_cast_expression(
            self, *, is_number_specified: bool) -> None:
        """
        Append integer cast (Math.trunc) expression.

        Parameters
        ----------
        is_number_specified : bool
            Boolean value whether a specified value is Number
            instance or not.
        """
        import apysc as ap
        if not is_number_specified:
            return
        expression: str = (
            f'{self.variable_name} = Math.trunc({self.variable_name}, 10);'
        )
        ap.append_js_expression(expression=expression)

    def _set_value_and_skip_expression_appending(
            self, *,
            value: Union[int, float, NumberValueInterface]) -> None:
        """
        Update value attribute and skip expression appending.

        Parameters
        ----------
        value : int or float or Int or Number
            Any number value to set. This interface casts that
            value to an integer if float or number value is specified.
        """
        from apysc._converter import cast
        if isinstance(value, NumberValueInterface):
            value._value = cast.to_int_from_float(int_or_float=value._value)
            value_: Union[int, float, NumberValueInterface] = value._value
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
        if not hasattr(self, '_value'):
            repr_str: str = 'Int(0)'
        else:
            repr_str = f'Int({self._value})'
        return repr_str
