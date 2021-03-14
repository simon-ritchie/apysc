"""Class implementation for boolean.
"""

from typing import Any
from typing import Union

from apyscript.converter import cast
from apyscript.expression import expression_file_util
from apyscript.expression import expression_variables_util
from apyscript.type.copy_interface import CopyInterface
from apyscript.type.variable_name_interface import VariableNameInterface
from apyscript.validation import bool_validation
from apyscript.validation import number_validation


class Boolean(CopyInterface):

    _initial_value: Union[bool, int, Any]
    _value: bool

    def __init__(self, value: Union[bool, int, Any]) -> None:
        """
        Boolean class for apyscript library.

        Parameters
        ----------
        value : bool or int or Boolean or Int
            Initial boolean value. 0 or 1 are acceptable for integer
            value.
        """
        TYPE_NAME: str = 'boolean'
        number_validation.validate_int_is_zero_or_one(integer=value)
        self._initial_value = value
        value_: bool = self._get_bool_from_arg_value(value=value)
        self._value = value_
        self._type_name = TYPE_NAME
        self.variable_name = expression_variables_util.get_next_variable_name(
            type_name=TYPE_NAME)
        self._append_constructor_expression()

    def _get_bool_from_arg_value(
            self, value: Union[bool, int, Any]) -> bool:
        """
        Get bool value from specified argument value.

        Parameters
        ----------
        value : bool or int or Boolean or Int
            Specified value. 0 or 1 are acceptable for integer
            value.

        Returns
        -------
        result : bool
            Converted boolean value.
        """
        from apyscript.type.number_value_interface import NumberValueInterface
        if isinstance(value, (int, float, NumberValueInterface)):
            result: bool = cast.to_bool_from_int(integer=value)
        elif isinstance(value, Boolean):
            result = value._value
        else:
            result = value
        bool_validation.validate_bool(value=result)
        return result

    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression to file.
        """
        expression: str = f'var {self.variable_name} = '
        if isinstance(self._initial_value, VariableNameInterface):
            expression += f'Boolean({self._initial_value.variable_name});'
        elif self._value:
            expression += 'true;'
        else:
            expression += 'false;'
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)

    @property
    def value(self) -> Union[bool, int, Any]:
        """
        Get a current boolean value.

        Returns
        -------
        value : bool
            Current boolean value.
        """
        return self._value

    @value.setter
    def value(self, value: Union[bool, int, Any]) -> None:
        """
        Set boolean value.

        Parameters
        ----------
        value : bool or int or Boolean or Int
            Any boolean value to set.
        """
        self._set_value_and_skip_expression_appending(value=value)
        if isinstance(value, VariableNameInterface):
            self._append_value_setter_expression(value=value)
        else:
            self._append_value_setter_expression(value=self._value)

    def _append_value_setter_expression(
            self, value: Union[bool, Any]) -> None:
        """
        Append value's setter expression to file.

        Parameters
        ----------
        value : bool or VariableNameInterface
            Any value to set.
        """
        expression: str = f'{self.variable_name} = '
        if isinstance(value, VariableNameInterface):
            expression += f'Boolean({value._variable_name});'
        elif value:
            expression += 'true;'
        else:
            expression += 'false;'
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)

    def _set_value_and_skip_expression_appending(
            self, value: Union[bool, int, Any]) -> None:
        """
        Update value attribute and skip expression appending.

        Parameters
        ----------
        value : bool or int or Boolean or Int
            Any boolean value to set.
        """
        value_: bool = self._get_bool_from_arg_value(value=value)
        self._value = value_

    def __bool__(self) -> bool:
        """
        Get a boolean value directly.

        Returns
        -------
        result : bool
            Current boolean value.
        """
        return self._value

    def __repr__(self) -> str:
        """
        Get a representation string of this instance.

        Returns
        -------
        repr_str : str
            Representation string of this instance.
        """
        repr_str: str = (
            f'Boolean({self._value})'
        )
        return repr_str
