"""Class implementation for number value interface.
"""

from typing import Any
from typing import Dict
from typing import Union

from apysc.type.copy_interface import CopyInterface
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface


class NumberValueInterface(CopyInterface, RevertInterface):

    _initial_value: Union[int, float, Any]
    _value: Union[int, float]

    def __init__(
            self, value: Union[int, float, Any], type_name: str) -> None:
        """
        Class for number value interface.

        Parameters
        ----------
        value : int or float or NumberValueInterface
            Initial number value.
        type_name : str
            This instance expression's type name (e.g., int, number).
        """
        from apysc.validation import number_validation
        number_validation.validate_num(num=value)
        self._initial_value = value
        if isinstance(value, NumberValueInterface):
            value_ = value._value
        else:
            value_ = value
        self._value = value_
        self._type_name = type_name

    def append_constructor_expression(self) -> None:
        """
        Append current value's constructor expression to file.
        """
        from apysc.expression import expression_file_util
        if isinstance(self._initial_value, NumberValueInterface):
            value_: Union[int, float, str] = self._initial_value.variable_name
        else:
            value_ = self.value
        expression: str = (
            f'var {self.variable_name} = {value_};'
        )
        expression_file_util.append_js_expression(expression=expression)

    @property
    def value(self) -> Union[int, float, Any]:
        """
        Get a current number value.

        Returns
        -------
        value : int or float
            Current number value.
        """
        return self._value

    @value.setter
    def value(self, value: Union[int, float, Any]) -> None:
        """
        Set number value.

        Parameters
        ----------
        value : int or float or NumberValueInterface
            Any number value to set.
        """
        self.set_value_and_skip_expression_appending(value=value)
        if isinstance(value, NumberValueInterface):
            self.append_value_setter_expression(value=value)
        else:
            self.append_value_setter_expression(value=self._value)

    def set_value_and_skip_expression_appending(
            self, value: Union[int, float, Any]) -> None:
        """
        Update value attribute and skip expression appending.

        Parameters
        ----------
        value : int or float or NumberValueInterface
            Any number value to set.
        """
        from apysc.validation import number_validation
        number_validation.validate_num(num=value)
        if isinstance(value, NumberValueInterface):
            value_ = value._value
        else:
            value_ = value
        self._value = value_

    def append_value_setter_expression(
            self, value: Union[int, float, Any]) -> None:
        """
        Append value's setter expresion to file.

        Parameters
        ----------
        value : int or float or NumberValueInterface
            Any number value to set.
        """
        from apysc.expression import expression_file_util
        if isinstance(value, NumberValueInterface):
            right_value: Union[str, int, float] = value.variable_name
        else:
            right_value = value
        expression: str = (
            f'{self.variable_name} = {right_value};'
        )
        expression_file_util.append_js_expression(expression=expression)

    def __add__(self, other: Union[int, float, Any]) -> Any:
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
        if isinstance(other, NumberValueInterface):
            value: Union[int, float, Any] = self._value + other.value
        else:
            value = self._value + other
        result: NumberValueInterface = self._copy()
        result.set_value_and_skip_expression_appending(value=value)
        self._append_addition_expression(result=result, other=other)
        return result

    def _append_addition_expression(
            self, result: VariableNameInterface,
            other: Union[int, float, Any]) -> None:
        """
        Append addition expression to file.

        Parameters
        ----------
        result : NumberValueInterface
            Addition result value.
        other : int or float or NumberValueInterface
            Other value to add.
        """
        from apysc.expression import expression_file_util
        from apysc.type.value_util import get_value_str_for_expression
        right_value: str = get_value_str_for_expression(value=other)
        expression: str = (
            f'var {result.variable_name} = '
            f'{self.variable_name} + {right_value};'
        )
        expression_file_util.append_js_expression(expression=expression)

    def __sub__(self, other: Union[int, float, Any]) -> Any:
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
        if isinstance(other, NumberValueInterface):
            value: Union[int, float, Any] = self._value - other.value
        else:
            value = self._value - other
        result: NumberValueInterface = self._copy()
        result.set_value_and_skip_expression_appending(value=value)
        self._append_subtraction_expression(result=result, other=other)
        return result

    def _append_subtraction_expression(
            self, result: VariableNameInterface,
            other: Union[int, float, Any]) -> None:
        """
        Append subtraction expression to file.

        Parameters
        ----------
        result : NumberValueInterface
            Subtraction result value.
        other : int or float or NumberValueInterface
            Other value to subtract.
        """
        from apysc.expression import expression_file_util
        from apysc.type.value_util import get_value_str_for_expression
        right_value: str = get_value_str_for_expression(value=other)
        expression: str = (
            f'var {result.variable_name} = '
            f'{self.variable_name} - {right_value};'
        )
        expression_file_util.append_js_expression(expression=expression)

    def __mul__(self, other: Union[int, float, Any]) -> Any:
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
        if isinstance(other, NumberValueInterface):
            value: Union[int, float, Any] = self._value * other.value
        else:
            value = self._value * other
        result: NumberValueInterface = self._copy()
        result.set_value_and_skip_expression_appending(value=value)
        self._append_multiplication_expression(result=result, other=other)
        return result

    def _append_multiplication_expression(
            self, result: VariableNameInterface,
            other: Union[int, float, Any]) -> None:
        """
        Append multiplication expression to file.

        Parameters
        ----------
        result : NumberValueInterface
            Multiplication result value.
        other : int or float or NumberValueInterface
            Other value to multiply.
        """
        from apysc.expression import expression_file_util
        from apysc.type.value_util import get_value_str_for_expression
        right_value: str = get_value_str_for_expression(value=other)
        expression: str = (
            f'var {result.variable_name} = '
            f'{self.variable_name} * {right_value};'
        )
        expression_file_util.append_js_expression(expression=expression)

    def __truediv__(self, other: Union[int, float, Any]) -> Any:
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
        from apysc import Number
        result: Number = Number(value=self)
        if isinstance(other, NumberValueInterface):
            value: Union[int, float, Any] = result._value / other.value
        else:
            value = result._value / other
        result.set_value_and_skip_expression_appending(value=value)
        self._append_true_division_expression(result=result, other=other)
        return result

    def _append_true_division_expression(
            self, result: VariableNameInterface,
            other: Union[int, float, Any]) -> None:
        """
        Append true division expression to file.

        Parameters
        ----------
        result : NumberValueInterface
            True division result value.
        other : int or float or NumberValueInterface
            Other value for true division.
        """
        from apysc.expression import expression_file_util
        from apysc.type.value_util import get_value_str_for_expression
        right_value: str = get_value_str_for_expression(value=other)
        expression: str = (
            f'{result.variable_name} = {result.variable_name} / '
            f'{right_value};'
        )
        expression_file_util.append_js_expression(expression=expression)

    def __floordiv__(self, other: Union[int, float, Any]) -> Any:
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
        from apysc import Int
        result: Int = Int(value=self)
        if isinstance(other, NumberValueInterface):
            value: Union[int, float, Any] = self._value // other.value
        else:
            value = self._value // other
        result.set_value_and_skip_expression_appending(value=value)
        self._append_floor_division_expression(result=result, other=other)
        return result

    def _append_floor_division_expression(
            self, result: VariableNameInterface,
            other: Union[int, float, Any]) -> None:
        """
        Append floor division expression to file.

        Parameters
        ----------
        result : NumberValueInterface
            Floor division result value.
        other : int or float or NumberValueInterface
            Other value for floor division.
        """
        from apysc.expression import expression_file_util
        from apysc.type.value_util import get_value_str_for_expression
        right_value: str = get_value_str_for_expression(value=other)
        expression: str = (
            f'{result.variable_name} = '
            f'parseInt({result.variable_name} / {right_value});'
        )
        expression_file_util.append_js_expression(expression=expression)

    def __iadd__(self, other: Union[int, float, Any]) -> Any:
        """
        Method for incremental addition.

        Parameters
        ----------
        other : int or float or NumberValueInterface
            Other value for incremental addition.

        Returns
        -------
        result : NumberValueInterface
            Incremental addition result value.
        """
        from apysc.expression import expression_variables_util
        result: NumberValueInterface = self + other
        expression_variables_util.append_substitution_expression(
            left_value=self, right_value=result)
        result.variable_name = self.variable_name
        return result

    def __isub__(self, other: Union[int, float, Any]) -> Any:
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
        from apysc.expression import expression_variables_util
        result: NumberValueInterface = self - other
        expression_variables_util.append_substitution_expression(
            left_value=self, right_value=result)
        result.variable_name = self.variable_name
        return result

    def __imul__(self, other: Union[int, float, Any]) -> Any:
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
        from apysc.expression import expression_variables_util
        result: NumberValueInterface = self * other
        expression_variables_util.append_substitution_expression(
            left_value=self, right_value=result)
        result.variable_name = self.variable_name
        return result

    def __itruediv__(self, other: Union[int, float, Any]) -> Any:
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
        from apysc.expression import expression_variables_util
        result: NumberValueInterface = self / other
        expression_variables_util.append_substitution_expression(
            left_value=self, right_value=result)
        result.variable_name = self.variable_name
        return result

    def __str__(self) -> str:
        """
        String conversion method.

        Returns
        -------
        string : str
            Converted value string.
        """
        return str(self.value)

    def __int__(self) -> int:
        """
        Integer conversion method.

        Returns
        -------
        integer : int
            Converted integer value.
        """
        return int(self.value)

    def __float__(self) -> float:
        """
        Float conversion method.

        Returns
        -------
        float_ : float
            Converted float value.
        """
        return float(self.value)

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
        from apysc import Boolean
        if isinstance(other, NumberValueInterface):
            result: Boolean = Boolean(self.value == other.value)
        else:
            result = Boolean(self.value == other)
        if isinstance(other, VariableNameInterface):
            self._append_eq_expression(result=result, other=other)
        return result

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
        from apysc.expression import expression_file_util
        expression: str = (
            f'{result.variable_name} = '
            f'{self.variable_name} === {other.variable_name};'
        )
        expression_file_util.append_js_expression(expression=expression)

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
        from apysc import Boolean
        if isinstance(other, NumberValueInterface):
            result: Boolean = Boolean(self.value != other.value)
        else:
            result = Boolean(self.value != other)
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
        from apysc.expression import expression_file_util
        expression: str = (
            f'{result.variable_name} = '
            f'{self.variable_name} !== {other.variable_name};'
        )
        expression_file_util.append_js_expression(expression=expression)

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
        from apysc import Boolean
        if isinstance(other, NumberValueInterface):
            result: Boolean = Boolean(self.value < other.value)
        else:
            result = Boolean(self.value < other)
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
        from apysc.expression import expression_file_util
        expression: str = (
            f'{result.variable_name} = '
            f'{self.variable_name} < {other.variable_name};'
        )
        expression_file_util.append_js_expression(expression=expression)

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
        from apysc import Boolean
        if isinstance(other, NumberValueInterface):
            result: Boolean = Boolean(self.value <= other.value)
        else:
            result = Boolean(self.value <= other)
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
        from apysc.expression import expression_file_util
        expression: str = (
            f'{result.variable_name} = '
            f'{self.variable_name} <= {other.variable_name};'
        )
        expression_file_util.append_js_expression(expression=expression)

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
        from apysc import Boolean
        if isinstance(other, NumberValueInterface):
            result: Boolean = Boolean(self.value > other.value)
        else:
            result = Boolean(self.value > other)
        if isinstance(other, NumberValueInterface):
            self._append_gt_expression(result=result, other=other)
        return result

    def _append_gt_expression(
            self, result: VariableNameInterface,
            other: VariableNameInterface) -> None:
        """
        Append __gt__ expression to file.

        Parameters
        ----------
        result : Boolean
            Result boolean value.
        other : VariableNameInterface
            Other value to compare.
        """
        from apysc.expression import expression_file_util
        expression: str = (
            f'{result.variable_name} = '
            f'{self.variable_name} > {other.variable_name};'
        )
        expression_file_util.append_js_expression(expression=expression)

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
        from apysc import Boolean
        if isinstance(other, NumberValueInterface):
            result: Boolean = Boolean(self.value >= other.value)
        else:
            result = Boolean(self.value >= other)
        if isinstance(other, VariableNameInterface):
            self._append_ge_expression(result=result, other=other)
        return result

    def _append_ge_expression(
            self, result: VariableNameInterface,
            other: VariableNameInterface) -> None:
        """
        Append __ge__ expression to file.

        Parameters
        ----------
        result : Boolean
            Result boolean value.
        other : VariableNameInterface
            Other value to compare.
        """
        from apysc.expression import expression_file_util
        expression: str = (
            f'{result.variable_name} = '
            f'{self.variable_name} >= {other.variable_name};'
        )
        expression_file_util.append_js_expression(expression=expression)

    _value_snapshots: Dict[str, Union[int, float]]

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
