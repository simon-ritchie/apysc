"""Class implementation for number value interface.
"""

from typing import Any
from typing import Dict
from typing import Generic
from typing import TypeVar
from typing import Union

from apysc._event.custom_event_interface import CustomEventInterface
from apysc._type.copy_interface import CopyInterface
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface

_NumType = Union[int, float, 'NumberValueInterface']
_V = TypeVar('_V', int, float)
_T = TypeVar('_T', bound='NumberValueInterface')


class NumberValueInterface(
        CopyInterface, RevertInterface, CustomEventInterface,
        Generic[_V, _T]):

    _initial_value: _NumType
    _value: _V

    def __init__(
            self, value: _NumType,
            type_name: str) -> None:
        """
        Class for number value interface.

        Parameters
        ----------
        value : int or float or NumberValueInterface
            Initial number value.
        type_name : str
            This instance expression's type name (e.g., int, number).
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            from apysc._validation import number_validation
            number_validation.validate_num(
                num=value)  # type: ignore
            self._initial_value = value
            if isinstance(value, NumberValueInterface):
                value_: _V = value._value
            else:
                value_ = value  # type: ignore
            self._value = value_
            self._type_name = type_name

    def append_constructor_expression(self) -> None:
        """
        Append current value's constructor expression.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.append_constructor_expression,
                locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            if isinstance(self._initial_value, NumberValueInterface):
                value_: Union[int, float, str] = \
                    self._initial_value.variable_name
            else:
                value_ = self._value
            expression: str = (
                f'var {self.variable_name} = {value_};'
            )
            ap.append_js_expression(expression=expression)

    @property
    def value(self) -> _NumType:
        """
        Get a current number value.

        Returns
        -------
        value : int or float
            Current number value.

        References
        ----------
        - apysc basic data classes common value interface
            - https://bit.ly/3Be1aij
        """
        return self._value

    @value.setter
    def value(self, value: _NumType) -> None:
        """
        Set number value.

        Parameters
        ----------
        value : int or float or NumberValueInterface
            Any number value to set.

        References
        ----------
        apysc basic data classes common value interface
            https://bit.ly/3Be1aij
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='value', locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            self._set_value_and_skip_expression_appending(value=value)
            if isinstance(value, NumberValueInterface):
                self._append_value_setter_expression(value=value)
            else:
                self._append_value_setter_expression(value=self._value)

    def _set_value_and_skip_expression_appending(
            self, value: _NumType) -> None:
        """
        Update value attribute and skip expression appending.

        Parameters
        ----------
        value : int or float or NumberValueInterface
            Any number value to set.
        """
        from apysc._validation import number_validation
        number_validation.validate_num(
            num=value)  # type: ignore
        if isinstance(value, NumberValueInterface):
            value_: _V = value._value
        else:
            value_ = value  # type: ignore
        self._value = value_

    def _append_value_setter_expression(
            self, value: _NumType) -> None:
        """
        Append value's setter expresion.

        Parameters
        ----------
        value : int or float or NumberValueInterface
            Any number value to set.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_value_setter_expression,
                locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            if isinstance(value, NumberValueInterface):
                right_value: Union[str, int, float] = value.variable_name
            else:
                right_value = value
            expression: str = (
                f'{self.variable_name} = {right_value};'
            )
            ap.append_js_expression(expression=expression)

    def __add__(self, other: _NumType) -> Any:
        """
        Method for addition.

        Parameters
        ----------
        other : int or float or NumberValueInterface
            Other value to add.

        Returns
        -------
        result : NumberValueInterface
            Addition result value.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__add__', locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            if isinstance(other, NumberValueInterface):
                value: _NumType = self._value + other._value
            else:
                value = self._value + other
            result: NumberValueInterface = self._copy()
            result._set_value_and_skip_expression_appending(value=value)
            self._append_addition_expression(result=result, other=other)
            return result

    def _append_addition_expression(
            self, result: VariableNameInterface,
            other: _NumType) -> None:
        """
        Append addition expression.

        Parameters
        ----------
        result : NumberValueInterface
            Addition result value.
        other : int or float or NumberValueInterface
            Other value to add.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_addition_expression, locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            from apysc._type.value_util import get_value_str_for_expression
            right_value: str = get_value_str_for_expression(value=other)
            expression: str = (
                f'var {result.variable_name} = '
                f'{self.variable_name} + {right_value};'
            )
            ap.append_js_expression(expression=expression)

    def __sub__(self, other: _NumType) -> Any:
        """
        Method for subtraction.

        Parameters
        ----------
        other : int or float or NumberValueInterface
            Other value to subtract.

        Returns
        -------
        result : NumberValueInterface
            Subtraction result value.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__sub__', locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            if isinstance(other, NumberValueInterface):
                value: _NumType = self._value - other._value
            else:
                value = self._value - other
            result: NumberValueInterface = self._copy()
            result._set_value_and_skip_expression_appending(value=value)
            self._append_subtraction_expression(result=result, other=other)
            return result

    def _append_subtraction_expression(
            self, result: VariableNameInterface,
            other: _NumType) -> None:
        """
        Append subtraction expression.

        Parameters
        ----------
        result : NumberValueInterface
            Subtraction result value.
        other : int or float or NumberValueInterface
            Other value to subtract.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_subtraction_expression,
                locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            from apysc._type.value_util import get_value_str_for_expression
            right_value: str = get_value_str_for_expression(value=other)
            expression: str = (
                f'var {result.variable_name} = '
                f'{self.variable_name} - {right_value};'
            )
            ap.append_js_expression(expression=expression)

    def __mul__(self, other: _NumType) -> _T:
        """
        Method for multiplication.

        Parameters
        ----------
        other : int or float or NumberValueInterface
            Other value to multiply.

        Returns
        -------
        result : NumberValueInterface
            Multiplication result value.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__mul__', locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            if isinstance(other, NumberValueInterface):
                value: _NumType = self._value * other._value
            else:
                value = self._value * other
            result: _T = self._copy()
            result._set_value_and_skip_expression_appending(value=value)
            self._append_multiplication_expression(result=result, other=other)
            return result

    def _append_multiplication_expression(
            self, result: VariableNameInterface,
            other: _NumType) -> None:
        """
        Append multiplication expression.

        Parameters
        ----------
        result : NumberValueInterface
            Multiplication result value.
        other : int or float or NumberValueInterface
            Other value to multiply.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_multiplication_expression,
                locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            from apysc._type.value_util import get_value_str_for_expression
            right_value: str = get_value_str_for_expression(value=other)
            expression: str = (
                f'var {result.variable_name} = '
                f'{self.variable_name} * {right_value};'
            )
            ap.append_js_expression(expression=expression)

    def __truediv__(self, other: _NumType) -> Any:
        """
        Method for true division (return floating point number).

        Parameters
        ----------
        other : int or float or NumberValueInterface
            Other value for true division.

        Returns
        -------
        result : Number
            True division result value.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__truediv__', locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            result: ap.Number = ap.Number(value=self)
            if isinstance(other, NumberValueInterface):
                value: _NumType = result._value / other._value
            else:
                value = result._value / other
            result._set_value_and_skip_expression_appending(value=value)
            self._append_true_division_expression(result=result, other=other)
            return result

    def _append_true_division_expression(
            self, result: VariableNameInterface,
            other: _NumType) -> None:
        """
        Append true division expression.

        Parameters
        ----------
        result : NumberValueInterface
            True division result value.
        other : int or float or NumberValueInterface
            Other value for true division.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_true_division_expression,
                locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            from apysc._type.value_util import get_value_str_for_expression
            right_value: str = get_value_str_for_expression(value=other)
            expression: str = (
                f'{result.variable_name} = {self.variable_name} / '
                f'{right_value};'
            )
            ap.append_js_expression(expression=expression)

    def __floordiv__(self, other: _NumType) -> Any:
        """
        Method for floor division (return integer).

        Parameters
        ----------
        other : int or float or NumberValueInterface
            Other value for floor division.

        Returns
        -------
        result : Int
            Floor division result value.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__floordiv__', locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            result: ap.Int = ap.Int(value=self)
            if isinstance(other, NumberValueInterface):
                value: _NumType = self._value // other._value
            else:
                value = self._value // other
            result._set_value_and_skip_expression_appending(value=value)
            self._append_floor_division_expression(result=result, other=other)
            return result

    def _append_floor_division_expression(
            self, result: VariableNameInterface,
            other: _NumType) -> None:
        """
        Append floor division expression.

        Parameters
        ----------
        result : NumberValueInterface
            Floor division result value.
        other : int or float or NumberValueInterface
            Other value for floor division.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_floor_division_expression,
                locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            from apysc._type.value_util import get_value_str_for_expression
            right_value: str = get_value_str_for_expression(value=other)
            expression: str = (
                f'{result.variable_name} = '
                f'parseInt({self.variable_name} / {right_value});'
            )
            ap.append_js_expression(expression=expression)

    _incremental_calc_prev_name: str = ''

    def _append_incremental_calc_substitution_expression(self) -> None:
        """
        Append a incremental calculation's substitution expression.
        This method will be called from the each interface.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_incremental_calc_substitution_expression,  # noqa
                locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            from apysc._expression import expression_variables_util
            expression_variables_util.\
                append_substitution_expression_with_names(
                    left_variable_name=self._incremental_calc_prev_name,
                    right_variable_name=self.variable_name)
            self._incremental_calc_prev_name = ''

    def __iadd__(self, other: _NumType) -> _T:
        """
        Method for incremental addition.

        Parameters
        ----------
        other : int or float or NumberValueInterface
            Other value for` incremental addition.

        Returns
        -------
        result : NumberValueInterface
            Incremental addition result value.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__iadd__', locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            from apysc._expression import expression_variables_util
            self._incremental_calc_prev_name = \
                self._get_previous_variable_name()
            result: _T = self + other
            expression_variables_util.append_substitution_expression(
                left_value=self, right_value=result)
            result.variable_name = self.variable_name
            return result

    def __isub__(self, other: _NumType) -> Any:
        """
        Method for incremental subtraction.

        Parameters
        ----------
        other : int or float or NumberValueInterface
            Other value for incremental subtraction.

        Returns
        -------
        result : NumberValueInterface
            Incremental subtraction result value.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__isub__', locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            from apysc._expression import expression_variables_util
            self._incremental_calc_prev_name = \
                self._get_previous_variable_name()
            result: NumberValueInterface = self - other
            expression_variables_util.append_substitution_expression(
                left_value=self, right_value=result)
            result.variable_name = self.variable_name
            return result

    def __imul__(self, other: _NumType) -> _T:
        """
        Method for incremental multiplication.

        Parameters
        ----------
        other : int or float or NumberValueInterface
            Other value for incremental multiplication.

        Returns
        -------
        result : NumberValueInterface
            Incremental multiplication result value.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__imul__', locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            from apysc._expression import expression_variables_util
            self._incremental_calc_prev_name = \
                self._get_previous_variable_name()
            result: _T = self * other
            expression_variables_util.append_substitution_expression(
                left_value=self, right_value=result)
            result.variable_name = self.variable_name
            return result

    def __itruediv__(self, other: _NumType) -> Any:
        """
        Method for incremental true division.

        Parameters
        ----------
        other : int or float or NumberValueInterface
            Other value for incremental true division.

        Returns
        -------
        result : NumberValueInterface
            Incremental true division result value.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__itruediv__', locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            from apysc._expression import expression_variables_util
            self._incremental_calc_prev_name = \
                self._get_previous_variable_name()
            result: NumberValueInterface = self / other
            result._incremental_calc_prev_name = \
                self._incremental_calc_prev_name
            expression_variables_util.append_substitution_expression(
                left_value=self, right_value=result)
            result.variable_name = self.variable_name
            return result

    def __mod__(self, other: _NumType) -> _T:
        """
        Method for the modulo operation.

        Parameters
        ----------
        other : int or float or NumberValueInterface
            Other value to be used in the modulo operation.

        Returns
        -------
        result : NumberValueInterface
            Modulo operation result value.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__mod__', locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            if isinstance(other, NumberValueInterface):
                value: Union[int, float] = self._value % other._value
            else:
                value = self._value % other
            result: _T = self._copy()
            result._set_value_and_skip_expression_appending(value=value)
            self._append_modulo_expression(result=result, other=other)
            return result

    def _append_modulo_expression(
            self, result: VariableNameInterface,
            other: _NumType) -> None:
        """
        Append a module expression.

        Parameters
        ----------
        result : NumberValueInterface
            Modulo operation result value.
        other : int or float or NumberValueInterface
            Other value to be used in the modulo operation.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_modulo_expression, locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            from apysc._type.value_util import get_value_str_for_expression
            right_value: str = get_value_str_for_expression(value=other)
            expression: str = (
                f'var {result.variable_name} = '
                f'{self.variable_name} % {right_value};'
            )
            ap.append_js_expression(expression=expression)

    def __str__(self) -> str:
        """
        String conversion method.

        Returns
        -------
        string : str
            Converted value string.
        """
        if not hasattr(self, '_value'):
            return '0'
        return str(self._value)

    def __int__(self) -> int:
        """
        Integer conversion method.

        Returns
        -------
        integer : int
            Converted integer value.
        """
        return int(self._value)

    def __float__(self) -> float:
        """
        Float conversion method.

        Returns
        -------
        float_ : float
            Converted float value.
        """
        return float(self._value)

    def __eq__(self, other: Any) -> Any:
        """
        Equal comparison method.

        Parameters
        ----------
        other : *
            Other value to compare. Builtin types, Int,
            and Number class instances are acceptable.

        Returns
        -------
        result : Boolean
            If specified value is same amount, True will be returned.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__eq__', locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            if isinstance(other, NumberValueInterface):
                result: ap.Boolean = ap.Boolean(self._value == other._value)
            else:
                result = ap.Boolean(self._value == other)
            other = self._convert_other_val_to_int_or_number(other=other)
            if isinstance(other, VariableNameInterface):
                self._append_eq_expression(result=result, other=other)
            return result

    def _convert_other_val_to_int_or_number(self, other: Any) -> Any:
        """
        If comparison other value is int or float, then
        convert it to Int or Number.

        Parameters
        ----------
        other : *
            Other comparison value.

        Returns
        -------
        converted_val : *
            Converted value. If int is specified, then this will be
            Int. float is specified, then Number.
            Other type will be returned directly (not to be converted).
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._convert_other_val_to_int_or_number,
                locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            if isinstance(other, int):
                return ap.Int(other)
            if isinstance(other, float):
                return ap.Number(other)
            return other

    def _append_eq_expression(
            self, result: VariableNameInterface,
            other: VariableNameInterface) -> None:
        """
        Append __eq__ method expression.

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
                module_name=__name__, class_=NumberValueInterface):
            expression: str = (
                f'{result.variable_name} = '
                f'{self.variable_name} === {other.variable_name};'
            )
            ap.append_js_expression(expression=expression)

    def __ne__(self, other: Any) -> Any:
        """
        Not equal comparison method.

        Parameters
        ----------
        other : *
            Other value to compare. Builtin types, Int,
            and Number class instances are acceptable.

        Returns
        -------
        result : Boolean
            If specified value is not same amount, True will be returned.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__ne__', locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            if isinstance(other, NumberValueInterface):
                result: ap.Boolean = ap.Boolean(self._value != other._value)
            else:
                result = ap.Boolean(self._value != other)
            other = self._convert_other_val_to_int_or_number(other=other)
            if isinstance(other, VariableNameInterface):
                self._append_ne_expression(result=result, other=other)
            return result

    def _append_ne_expression(
            self, result: VariableNameInterface,
            other: VariableNameInterface) -> None:
        """
        Append __ne__ method expression.

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
                module_name=__name__, class_=NumberValueInterface):
            expression: str = (
                f'{result.variable_name} = '
                f'{self.variable_name} !== {other.variable_name};'
            )
            ap.append_js_expression(expression=expression)

    def __lt__(self, other: Any) -> Any:
        """
        Less than comparison method.

        Parameters
        ----------
        other : *
            Other value to compare. Builtin types, Int,
            and Number class instances are acceptable.

        Returns
        -------
        result : Boolean
            If this value is less than a specified value, then
            True will be returned.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__lt__', locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            if isinstance(other, NumberValueInterface):
                result: ap.Boolean = ap.Boolean(self._value < other._value)
            else:
                result = ap.Boolean(self._value < other)
            other = self._convert_other_val_to_int_or_number(other=other)
            if isinstance(other, VariableNameInterface):
                self._append_lt_expression(result=result, other=other)
            return result

    def _append_lt_expression(
            self, result: VariableNameInterface,
            other: VariableNameInterface) -> None:
        """
        Append __lt__ method expression.

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
                module_name=__name__, class_=NumberValueInterface):
            expression: str = (
                f'{result.variable_name} = '
                f'{self.variable_name} < {other.variable_name};'
            )
            ap.append_js_expression(expression=expression)

    def __le__(self, other: Any) -> Any:
        """
        Less than equal comparison method.

        Parameters
        ----------
        other : *
            Other value to compare. Builtin types, Int,
            and Number class instances are acceptable.

        Returns
        -------
        result : Boolean
            If this value is less than or equal to a specified value,
            then True will be returned.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__le__', locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            if isinstance(other, NumberValueInterface):
                result: ap.Boolean = ap.Boolean(self._value <= other._value)
            else:
                result = ap.Boolean(self._value <= other)
            other = self._convert_other_val_to_int_or_number(other=other)
            if isinstance(other, VariableNameInterface):
                self._append_le_expression(result=result, other=other)
            return result

    def _append_le_expression(
            self, result: VariableNameInterface,
            other: VariableNameInterface) -> None:
        """
        Append __le__ method expression.

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
                module_name=__name__, class_=NumberValueInterface):
            expression: str = (
                f'{result.variable_name} = '
                f'{self.variable_name} <= {other.variable_name};'
            )
            ap.append_js_expression(expression=expression)

    def __gt__(self, other: Any) -> Any:
        """
        Greater than comparison method.

        Parameters
        ----------
        other : *
            Other value to compare. Builtin types, Int,
            and Number class instances are acceptable.

        Returns
        -------
        result : Boolean
            If this value is greater than a specified value, then
            True will be returned.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__gt__', locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            if isinstance(other, NumberValueInterface):
                result: ap.Boolean = ap.Boolean(self._value > other._value)
            else:
                result = ap.Boolean(self._value > other)
            other = self._convert_other_val_to_int_or_number(other=other)
            if isinstance(other, NumberValueInterface):
                self._append_gt_expression(result=result, other=other)
            return result

    def _append_gt_expression(
            self, result: VariableNameInterface,
            other: VariableNameInterface) -> None:
        """
        Append __gt__ expression.

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
                module_name=__name__, class_=NumberValueInterface):
            expression: str = (
                f'{result.variable_name} = '
                f'{self.variable_name} > {other.variable_name};'
            )
            ap.append_js_expression(expression=expression)

    def __ge__(self, other: Any) -> Any:
        """
        Greater than equal comparison method.

        Parameters
        ----------
        other : *
            Other value to compare. Builtin types, Int,
            and Number class instances are acceptable.

        Returns
        -------
        result : Boolean
            If this value is greater than or equal to a specified value,
            then True will be returned.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__ge__', locals_=locals(),
                module_name=__name__, class_=NumberValueInterface):
            if isinstance(other, NumberValueInterface):
                result: ap.Boolean = ap.Boolean(self._value >= other._value)
            else:
                result = ap.Boolean(self._value >= other)
            other = self._convert_other_val_to_int_or_number(other=other)
            if isinstance(other, VariableNameInterface):
                self._append_ge_expression(result=result, other=other)
            return result

    def _append_ge_expression(
            self, result: VariableNameInterface,
            other: VariableNameInterface) -> None:
        """
        Append __ge__ expression.

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
                module_name=__name__, class_=NumberValueInterface):
            expression: str = (
                f'{result.variable_name} = '
                f'{self.variable_name} >= {other.variable_name};'
            )
            ap.append_js_expression(expression=expression)

    _value_snapshots: Dict[str, _V]

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
        Revert value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._value = self._value_snapshots[snapshot_name]
