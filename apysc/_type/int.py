"""Class implementation of integer.
"""

from typing import Union

from apysc._type.number_value_interface import NumberValueInterface


class Int(NumberValueInterface[int, 'Int']):
    """
    Integer class for the apysc library.

    References
    ----------
    - Int and Number document
        - https://simon-ritchie.github.io/apysc/int_and_number.html
    - Int and Number common arithmetic operations document
        - https://bit.ly/3evzcVj
    - Int and Number common comparison operations document
        - https://bit.ly/3zolw6T

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

    def __init__(
            self, value: Union[int, float, NumberValueInterface]) -> None:
        """
        Integer class for apysc library.

        Parameters
        ----------
        value : int or float or Int or Number
            Initial integer value. If float or Number value is specified,
            that value will be cast to integer.

        References
        ----------
        - Int and Number document
            - https://simon-ritchie.github.io/apysc/int_and_number.html
        - Int and Number common arithmetic operations document
            - https://bit.ly/3evzcVj
        - Int and Number common comparison operations document
            - https://bit.ly/3zolw6T

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
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=Int):
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
            self, *, is_number_specified: bool) -> None:
        """
        Append integer cast (parseInt) expression.

        Parameters
        ----------
        is_number_specified : bool
            Boolean value whether a specified value is Number
            instance or not.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_cast_expression, locals_=locals(),
                module_name=__name__, class_=Int):
            if not is_number_specified:
                return
            expression: str = (
                f'{self.variable_name} = parseInt({self.variable_name}, 10);'
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
            Any number value to set. If float or Number value is specified,
            that value will be cast to integer.
        """
        from apysc._converter import cast
        from apysc._validation import number_validation
        number_validation.validate_num(num=value)  # type: ignore
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
