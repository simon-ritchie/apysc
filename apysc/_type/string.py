"""Class implementation for string.
"""

from typing import Any
from typing import Dict
from typing import Union

from apysc._event.custom_event_interface import CustomEventInterface
from apysc._type.copy_interface import CopyInterface
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class String(CopyInterface, RevertInterface, CustomEventInterface):
    """
    String class for apysc library.

    References
    ----------
    - String document
        - https://simon-ritchie.github.io/apysc/string.html
    - String class comparison operations document
        - https://bit.ly/3ewROEr
    - String class addition and multiplication operations document
        - https://bit.ly/2URRhWL
    """

    _initial_value: Union[str, Any]
    _value: str

    def __init__(self, value: Union[str, Any]) -> None:
        """
        String class for apysc library.

        Parameters
        ----------
        value : str or String
            Initial string value.

        References
        ----------
        - String document
            - https://simon-ritchie.github.io/apysc/string.html
        - String class comparison operations document
            - https://bit.ly/3ewROEr
        - String class addition and multiplication operations document
            - https://bit.ly/2URRhWL
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=String):
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            from apysc._expression.event_handler_scope import \
                TemporaryNotHandlerScope
            from apysc._validation import string_validation
            with TemporaryNotHandlerScope():
                TYPE_NAME: str = var_names.STRING
                string_validation.validate_string_type(string=value)
                self._initial_value = value
                self._type_name = TYPE_NAME
                self._value = self._get_str_value(value=value)
                self.variable_name = expression_variables_util.\
                    get_next_variable_name(type_name=TYPE_NAME)
                self._append_constructor_expression()

    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression to file.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_constructor_expression,
                locals_=locals(),
                module_name=__name__, class_=String):
            expression: str = f'var {self.variable_name} = '
            if isinstance(self._initial_value, String):
                expression += f'{self._initial_value.variable_name};'
            else:
                expression += f'"{self._value}";'
            ap.append_js_expression(expression=expression)

    def _get_str_value(self, value: Union[str, Any]) -> str:
        """
        Get a (Python's) str value from specified value.

        Parameters
        ----------
        value : str or String
            Target string value.

        Returns
        -------
        value : str
            Python's builtin str value.
        """
        if isinstance(value, String):
            return value._value
        return value

    @property
    def value(self) -> Union[str, Any]:
        """
        Get a current string value.

        Returns
        -------
        value : str
            Current string value.

        References
        ----------
        - apysc basic data classes common value interface
            - https://bit.ly/3Be1aij
        """
        return self._value

    @value.setter
    def value(self, value: Union[str, Any]) -> None:
        """
        Set string value.

        Parameters
        ----------
        value : str or String
            Any string value to set.

        References
        ----------
        apysc basic data classes common value interface
            https://bit.ly/3Be1aij
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='value', locals_=locals(),
                module_name=__name__, class_=String):
            from apysc._validation import string_validation
            string_validation.validate_string_type(string=value)
            self._value = self._get_str_value(value=value)
            self._append_value_setter_expression(value=value)

    def _append_value_setter_expression(
            self, value: Union[str, Any]) -> None:
        """
        Append value's setter expression to file.

        Parameters
        ----------
        value : str or String
            Any string value to set.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_value_setter_expression,
                locals_=locals(),
                module_name=__name__, class_=String):
            expression: str = f'{self.variable_name} = '
            if isinstance(value, String):
                expression += f'{value.variable_name};'
            else:
                expression += f'"{value}";'
            ap.append_js_expression(expression=expression)

    def __add__(self, other: Union[str, Any]) -> Any:
        """
        Method for addition (string concatenation).

        Parameters
        ----------
        other : str or String
            Other string value to concatenate.

        Returns
        -------
        result : String
            Concatenated result string.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__add__', locals_=locals(),
                module_name=__name__, class_=String):
            from apysc._validation import string_validation
            string_validation.validate_string_type(string=other)
            if isinstance(other, String):
                value: str = self._value + other.value
            else:
                value = self._value + other
            result: String = self._copy()
            result._value = value
            self._append_addition_expression(result=result, other=other)
            return result

    def _append_addition_expression(
            self, result: VariableNameInterface,
            other: Union[str, Any]) -> None:
        """
        Append addition (string concatenation) expression to file.

        Parameters
        ----------
        result : String
            Addition result value.
        other : str or String
            Other string value to concatenate.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_addition_expression,
                locals_=locals(),
                module_name=__name__, class_=String):
            from apysc._type.value_util import get_value_str_for_expression
            right_value: str = get_value_str_for_expression(value=other)
            expression: str = (
                f'var {result.variable_name} = '
                f'{self.variable_name} + {right_value};'
            )
            ap.append_js_expression(expression=expression)

    def __mul__(self, other: Union[int, Any]) -> Any:
        """
        Method for multiplication (string repetition).

        Parameters
        ----------
        other : int or Int
            String repetition number.

        Returns
        -------
        result : String
            Repeated result string.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__mul__', locals_=locals(),
                module_name=__name__, class_=String):
            from apysc._validation import number_validation
            number_validation.validate_integer(integer=other)
            if isinstance(other, ap.Int):
                value: int = other.value  # type: ignore
            else:
                value = other
            result: String = self._copy()
            result._value = result._value * value
            self._append_multiplication_expression(result=result, other=other)
            return result

    def _append_multiplication_expression(
            self, result: VariableNameInterface,
            other: Union[int, Any]) -> None:
        """
        Append multiplication (string repetition) expression to file.

        Parameters
        ----------
        result : String
            Multiplication result value.
        other : int or Int
            String repetition number.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_multiplication_expression,
                locals_=locals(),
                module_name=__name__, class_=String):
            expression: str = f'var {result.variable_name} = "";'
            expression += '\nfor (var i = 0; i < '
            if isinstance(other, ap.Int):
                expression += f'{other.variable_name}'
            else:
                expression += f'{other}'
            expression += '; i++) {'
            expression += (
                f'\n  {result.variable_name} += {self.variable_name};')
            expression += '\n}'
            ap.append_js_expression(expression=expression)

    def __iadd__(self, other: Union[str, Any]) -> Any:
        """
        Method for incremental addition (string concatenation).

        Parameters
        ----------
        other : str or String
            Other string value to concatenate.

        Returns
        -------
        result : String
            Concatenated result string.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__iadd__', locals_=locals(),
                module_name=__name__, class_=String):
            from apysc._expression import expression_variables_util
            result: String = self + other
            expression_variables_util.append_substitution_expression(
                left_value=self, right_value=result)
            result.variable_name = self.variable_name
            return result

    def __imul__(self, other: Union[int, Any]) -> Any:
        """
        Method for incremental multiplication (string repetition).

        Parameters
        ----------
        other : int or Int
            String repetition number.

        Returns
        -------
        result : String
            Repetition result string.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__imul__', locals_=locals(),
                module_name=__name__, class_=String):
            from apysc._expression import expression_variables_util
            result: String = self * other
            expression_variables_util.append_substitution_expression(
                left_value=self, right_value=result)
            result.variable_name = self.variable_name
            return result

    def __str__(self) -> str:
        """
        Method for str conversion.

        Returns
        -------
        result : str
            Python builtins str value.
        """
        if not hasattr(self, '_value'):
            return ''
        return self._value

    def __eq__(self, other: Any) -> Any:
        """
        Method for equal comparison.

        Parameters
        ----------
        other : *
            Any value to compare.

        Returns
        -------
        result : Boolean
            Comparison result. If same value of str or String
            is specified, True will be returned.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__eq__', locals_=locals(),
                module_name=__name__, class_=String):
            if isinstance(other, str):
                result: ap.Boolean = ap.Boolean(self._value == other)
            elif isinstance(other, String):
                result = ap.Boolean(self._value == other._value)
            else:
                result = ap.Boolean(False)
            other = self._convert_other_val_to_string(other=other)
            if isinstance(other, VariableNameInterface):
                self._append_eq_expression(result=result, other=other)
            return result

    def _convert_other_val_to_string(self, other: Any) -> Any:
        """
        If comparison other value is string, then convert it to
        String.

        Parameters
        ----------
        other : *
            Other comparison value.

        Returns
        -------
        converted_val : *
            Converted value. If other value is string, then this
            will be String instance. Other type will be returned
            directly (not to be converted).
        """
        if isinstance(other, str):
            return String(other)
        return other

    def _append_eq_expression(
            self, result: VariableNameInterface,
            other: VariableNameInterface) -> None:
        """
        Append __eq__ method expression to file.

        Parameters
        ----------
        result : Boolean
            Result boolean value.
        other : VariableNameInterface
            Other value to compare.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_eq_expression, locals_=locals(),
                module_name=__name__, class_=String):
            expression: str = (
                f'{result.variable_name} = '
                f'{self.variable_name} === {other.variable_name};'
            )
            ap.append_js_expression(expression=expression)

    def __ne__(self, other: Any) -> Any:
        """
        Method for not equal comparison.

        Parameters
        ----------
        other : *
            Any value to compare.

        Returns
        -------
        result : Boolean
            Comparison result. If not same value of str or String
            is specified, True will be returned.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__ne__', locals_=locals(),
                module_name=__name__, class_=String):
            if isinstance(other, str):
                result: ap.Boolean = ap.Boolean(self._value != other)
            elif isinstance(other, String):
                result = ap.Boolean(self._value != other._value)
            else:
                result = ap.Boolean(True)
            other = self._convert_other_val_to_string(other=other)
            if isinstance(other, VariableNameInterface):
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
        other : VariableNameInterface
            Other value to compare.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_ne_expression, locals_=locals(),
                module_name=__name__, class_=String):
            expression: str = (
                f'{result.variable_name} = '
                f'{self.variable_name} !== {other.variable_name};'
            )
            ap.append_js_expression(expression=expression)

    def __lt__(self, other: Union[str, Any]) -> Any:
        """
        Method for less than comparison.

        Parameters
        ----------
        other : str or String
            String value to compare.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__lt__', locals_=locals(),
                module_name=__name__, class_=String):
            from apysc._validation import string_validation
            string_validation.validate_string_type(string=other)
            value: str = self._get_str_value(value=other)
            result: ap.Boolean = ap.Boolean(self._value < value)
            other = self._convert_other_val_to_string(other=other)
            if isinstance(other, VariableNameInterface):
                self._append_lt_expression(result=result, other=other)
            return result

    def _append_lt_expression(
            self, result: VariableNameInterface,
            other: VariableNameInterface) -> None:
        """
        Append __lt__ method expression to file.

        Parameters
        ----------
        result : Boolean
            Result boolean value.
        other : VariableNameInterface
            Other value to compare.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_lt_expression, locals_=locals(),
                module_name=__name__, class_=String):
            expression: str = (
                f'{result.variable_name} = '
                f'{self.variable_name} < {other.variable_name};'
            )
            ap.append_js_expression(expression=expression)

    def __le__(self, other: Union[str, Any]) -> Any:
        """
        Method for less than or equal comparison.

        Parameters
        ----------
        other : str or String
            String value to compare.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__le__', locals_=locals(),
                module_name=__name__, class_=String):
            from apysc._validation import string_validation
            string_validation.validate_string_type(string=other)
            value: str = self._get_str_value(value=other)
            result: ap.Boolean = ap.Boolean(self._value <= value)
            other = self._convert_other_val_to_string(other=other)
            if isinstance(other, VariableNameInterface):
                self._append_le_expression(result=result, other=other)
            return result

    def _append_le_expression(
            self, result: VariableNameInterface,
            other: VariableNameInterface) -> None:
        """
        Append __le__ method expression to file.

        Parameters
        ----------
        result : Boolean
            Result boolean value.
        other : VariableNameInterface
            Other value to compare.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_le_expression, locals_=locals(),
                module_name=__name__, class_=String):
            expression: str = (
                f'{result.variable_name} = '
                f'{self.variable_name} <= {other.variable_name};'
            )
            ap.append_js_expression(expression=expression)

    def __gt__(self, other: Union[str, Any]) -> Any:
        """
        Method for greater than comparison.

        Parameters
        ----------
        other : str or String
            String value to compare.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__gt__', locals_=locals(),
                module_name=__name__, class_=String):
            from apysc._validation import string_validation
            string_validation.validate_string_type(string=other)
            value: str = self._get_str_value(value=other)
            result: ap.Boolean = ap.Boolean(self._value > value)
            other = self._convert_other_val_to_string(other=other)
            if isinstance(other, VariableNameInterface):
                self._append_gt_expression(result=result, other=other)
            return result

    def _append_gt_expression(
            self, result: VariableNameInterface,
            other: VariableNameInterface) -> None:
        """
        Append __gt__ method expression to file.

        Parameters
        ----------
        result : Boolean
            Result boolean value.
        other : VariableNameInterface
            Other value to compare.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_gt_expression, locals_=locals(),
                module_name=__name__, class_=String):
            expression: str = (
                f'{result.variable_name} = '
                f'{self.variable_name} > {other.variable_name};'
            )
            ap.append_js_expression(expression=expression)

    def __ge__(self, other: Union[str, Any]) -> Any:
        """
        Method for greater than or equal comparison.

        Parameters
        ----------
        other : str or String
            String value to compare.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__ge__', locals_=locals(),
                module_name=__name__, class_=String):
            from apysc._validation import string_validation
            string_validation.validate_string_type(string=other)
            value: str = self._get_str_value(value=other)
            result: ap.Boolean = ap.Boolean(self._value >= value)
            other = self._convert_other_val_to_string(other=other)
            if isinstance(other, VariableNameInterface):
                self._append_ge_expression(result=result, other=other)
            return result

    def _append_ge_expression(
            self, result: VariableNameInterface,
            other: VariableNameInterface) -> None:
        """
        Append __ge__ method expression to file.

        Parameters
        ----------
        result : Boolean
            Result boolean value.
        other : VariableNameInterface
            Other value to compare.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_ge_expression, locals_=locals(),
                module_name=__name__, class_=String):
            expression: str = (
                f'{result.variable_name} = '
                f'{self.variable_name} >= {other.variable_name};'
            )
            ap.append_js_expression(expression=expression)

    def __int__(self) -> int:
        """
        Method for integer conversion.

        Returns
        -------
        result : int
            Converted integer value.
        """
        result: int = int(self._value)
        return result

    def __float__(self) -> float:
        """
        Method for float conversion.

        Returns
        -------
        result : float
            Converted float value.
        """
        result: float = float(self._value)
        return result

    def __repr__(self) -> str:
        """
        Get a representation string of this instance.

        Returns
        -------
        repr_str : str
            Representation string of this instance.
        """
        if not hasattr(self, '_value'):
            repr_str: str = "String('')"
        else:
            repr_str = f"String('{self._value}')"
        return repr_str

    _value_snapshots: Dict[str, str]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

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
