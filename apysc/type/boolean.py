"""Class implementation for boolean.
"""

from typing import Any
from typing import Dict
from typing import Union

from apysc import Int
from apysc.type.copy_interface import CopyInterface
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface


class Boolean(CopyInterface, RevertInterface):

    _initial_value: Union[bool, int, Any]
    _value: bool

    def __init__(self, value: Union[bool, int, Int, Any]) -> None:
        """
        Boolean class for apysc library.

        Parameters
        ----------
        value : bool or int or Boolean or Int
            Initial boolean value. 0 or 1 are acceptable for integer
            value.
        """
        from apysc.expression import expression_variables_util
        from apysc.expression import var_names
        from apysc.validation import number_validation
        TYPE_NAME: str = var_names.BOOLEAN
        number_validation.validate_int_is_zero_or_one(integer=value)
        self._initial_value = value
        value_: bool = self._get_bool_from_arg_value(value=value)
        self._value = value_
        self._type_name = TYPE_NAME
        self.variable_name = expression_variables_util.get_next_variable_name(
            type_name=TYPE_NAME)
        self._append_constructor_expression()

    def _get_bool_from_arg_value(
            self, value: Union[bool, int, Int, Any]) -> bool:
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
        from apysc.converter import cast
        from apysc.type.number_value_interface import NumberValueInterface
        from apysc.validation import bool_validation
        if isinstance(value, (int, float, NumberValueInterface)):
            result: bool = cast.to_bool_from_int(integer=value)  # type: ignore
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
        from apysc.expression import expression_file_util
        from apysc.type.variable_name_interface import VariableNameInterface
        expression: str = f'var {self.variable_name} = '
        if isinstance(self._initial_value, VariableNameInterface):
            expression += f'Boolean({self._initial_value.variable_name});'
        elif self._value:
            expression += 'true;'
        else:
            expression += 'false;'
        expression_file_util.append_js_expression(expression=expression)

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
    def value(self, value: Union[bool, int, Int, Any]) -> None:
        """
        Set boolean value.

        Parameters
        ----------
        value : bool or int or Boolean or Int
            Any boolean value to set.
        """
        from apysc.type.variable_name_interface import VariableNameInterface
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
        from apysc.expression import expression_file_util
        from apysc.type.variable_name_interface import VariableNameInterface
        expression: str = f'{self.variable_name} = '
        if isinstance(value, VariableNameInterface):
            expression += f'Boolean({value._variable_name});'
        elif value:
            expression += 'true;'
        else:
            expression += 'false;'
        expression_file_util.append_js_expression(expression=expression)

    def _set_value_and_skip_expression_appending(
            self, value: Union[bool, int, Int, Any]) -> None:
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

    _value_snapshots: Dict[str, bool]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make values snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_value_snapshots'):
            self._value_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._value_snapshots[snapshot_name] = self._value

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert values if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._value = self._value_snapshots[snapshot_name]

    def __eq__(self, other: Any) -> Any:
        """
        Comparison method for equal condition.

        Parameters
        ----------
        other : *
            Other value to compare (Boolean, bool, int, or Int).

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        self._validate_comparison_other_type(other=other)
        result: Boolean
        if isinstance(other, Boolean):
            result = Boolean(self._value == other._value)
            self._append_eq_expression(result=result, other=other)
            return result
        elif isinstance(other, Int):
            other_ = bool(other.value)
            result = Boolean(self._value == other_)
        else:
            other = bool(other)
            result = Boolean(self._value == other)
            other = Boolean(other)
        self._append_eq_expression(result=result, other=other)
        return result

    def _validate_comparison_other_type(self, other: Any) -> None:
        """
        Validate comparison's other value type.

        Parameters
        ----------
        other : *
            Other value to compare.

        Raises
        ------
        ValueError
            If other value type is not Boolean, bool, Int, and int.
        """
        ACCEPTABLE_TYPES: tuple = (Boolean, bool, Int, int)
        if isinstance(other, ACCEPTABLE_TYPES):
            return
        raise ValueError(
            'Can\'t acceptable comparison value type is specified: '
            f'{type(other)}, {other}'
            f'\nAcceptable value types are: {ACCEPTABLE_TYPES}')

    def _append_eq_expression(
            self, result: VariableNameInterface,
            other: VariableNameInterface) -> None:
        """
        Append __eq__ method expression to file.

        Parameters
        ----------
        result : Boolean
            Result boolean value.
        other : Boolean or Int
            Other value to compare.
        """
        from apysc.expression import expression_file_util
        other_str: str = other.variable_name
        if isinstance(other, Int):
            other_str = f'Boolean({other_str});'
        expression: str = (
            f'{result.variable_name} = '
            f'{self.variable_name} === {other_str};'
        )
        expression_file_util.append_js_expression(expression=expression)

    def __ne__(self, other: Any) -> Any:
        """
        Comparison method for not equal condition.

        Parameters
        ----------
        other : *
            Other value to compare (Boolean, bool, int, or Int).

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        result: Boolean = self == other
        result = result.not_
        if isinstance(other, (Boolean, Int)):
            self._append_ne_expression(result=result, other=other)
        return result

    def _append_ne_expression(
            self, result: VariableNameInterface,
            other: VariableNameInterface) -> None:
        """
        Append __ne__ method expression to file.

        Parameters
        ----------
        result : Boolean
            Result boolean value.
        other : Boolean or Int
            Other value to compare.
        """
        from apysc.expression import expression_file_util
        other_str: str = other.variable_name
        if isinstance(other, Int):
            other_str = f'Boolean({other_str});'
        expression: str = (
            f'{result.variable_name} = '
            f'{self.variable_name} !== {other_str};'
        )
        expression_file_util.append_js_expression(expression=expression)

    @property
    def not_(self) -> Any:
        """
        Get a not condition Boolean value.

        Returns
        -------
        result : Boolean
            Not condition Boolean value.
        """
        result: Boolean = Boolean(not self)
        self._append_not_prop_expression(result=result)
        return result

    def _append_not_prop_expression(
            self, result: VariableNameInterface) -> None:
        """
        Append not_ property expression to file.

        Parameters
        ----------
        result : Boolean
            Result Boolean value.
        """
        from apysc.expression import expression_file_util
        expression: str = (
            f'{result.variable_name} = '
            f'!{self.variable_name};'
        )
        expression_file_util.append_js_expression(expression=expression)
