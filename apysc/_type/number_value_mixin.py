"""Class implementation for number value mix-in.
"""

from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Dict
from typing import Generic
from typing import TypeVar
from typing import Union

from typing_extensions import final

from apysc._event.custom_event_mixin import CustomEventMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.copy_mixin import CopyMixIn
from apysc._type.initial_substitution_exp_mixin import InitialSubstitutionExpMixIn
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos

_NumType = Union[int, float, "NumberValueMixIn"]
_ValueType = TypeVar("_ValueType", int, float)
_InstanceType = TypeVar("_InstanceType", bound="NumberValueMixIn")


class NumberValueMixIn(
    CopyMixIn,
    RevertMixIn,
    CustomEventMixIn,
    VariableNameSuffixMixIn,
    InitialSubstitutionExpMixIn,
    Generic[_ValueType, _InstanceType],
    ABC,
):

    _initial_value: _NumType
    _value: _ValueType

    @arg_validation_decos.is_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self, *, value: _NumType, type_name: str, variable_name_suffix: str = ""
    ) -> None:
        """
        Class for number value interface.

        Parameters
        ----------
        value : NumberValueMixIn or int or float
            Initial number value.
        type_name : str
            This instance expression's type name (e.g., int, number).
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        self._variable_name_suffix = variable_name_suffix
        self._initial_value = value
        if isinstance(value, NumberValueMixIn):
            value_: _ValueType = value._value
        else:
            value_ = value  # type: ignore
        self._value = value_
        self._type_name = type_name

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_constructor_expression(self) -> None:
        """
        Append a current value's constructor expression.
        """
        import apysc as ap

        expression: str = self._create_initial_substitution_expression()

        expression = f"var {expression}"
        ap.append_js_expression(expression=expression)

    @final
    def _create_initial_substitution_expression(self) -> str:
        """
        Create an initial value's substitution expression string.

        Returns
        -------
        expression : str
            Created expression string.
        """
        if isinstance(self._initial_value, NumberValueMixIn):
            value_: Union[int, float, str] = self._initial_value.variable_name
        else:
            value_ = self._value
        expression: str = f"{self.variable_name} = {value_};"
        return expression

    @property
    @add_debug_info_setting(module_name=__name__)
    def value(self) -> _NumType:
        """
        Get a current number value.

        Returns
        -------
        value : int or float
            Current number value.

        References
        ----------
        - apysc fundamental data classes value interface
            - https://simon-ritchie.github.io/apysc/en/fundamental_data_classes_value_interface.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> int_val: ap.Int = ap.Int(10)
        >>> int_val.value
        10

        >>> int_val.value = 20
        >>> int_val.value
        20

        >>> int_val.value = ap.Int(30)
        >>> int_val.value
        30
        """
        return self._value

    @value.setter
    @arg_validation_decos.is_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def value(self, value: _NumType) -> None:
        """
        Set number value.

        Parameters
        ----------
        value : NumberValueMixIn or int or float
            Any number value to set.

        References
        ----------
        - apysc fundamental data classes value interface
            - https://simon-ritchie.github.io/apysc/en/fundamental_data_classes_value_interface.html  # noqa
        """
        self._set_value_and_skip_expression_appending(value=value)
        if isinstance(value, NumberValueMixIn):
            self._append_value_setter_expression(value=value)
        else:
            self._append_value_setter_expression(value=self._value)

    @abstractmethod
    def _set_value_and_skip_expression_appending(self, *, value: _NumType) -> None:
        """
        Update value attribute and skip expression appending.

        Parameters
        ----------
        value : NumberValueMixIn or int or float
            Any number value to set.
        """

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_value_setter_expression(self, *, value: _NumType) -> None:
        """
        Append value's setter-expresion.

        Parameters
        ----------
        value : NumberValueMixIn or int or float
            Any number value to set.
        """
        import apysc as ap

        if isinstance(value, NumberValueMixIn):
            right_value: Union[str, int, float] = value.variable_name
        else:
            right_value = value  # type: ignore
        expression: str = f"{self.variable_name} = {right_value};"
        ap.append_js_expression(expression=expression)

    @final
    @arg_validation_decos.is_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def __add__(self, other: _NumType) -> Any:
        """
        Method for addition.

        Parameters
        ----------
        other : NumberValueMixIn or int or float
            Other value to add.

        Returns
        -------
        result : NumberValueMixIn
            Addition result value.
        """
        if isinstance(other, NumberValueMixIn):
            value: _NumType = self._value + other._value
        else:
            value = self._value + other  # type: ignore
        result: NumberValueMixIn = self._copy()
        result._set_value_and_skip_expression_appending(value=value)
        self._append_addition_expression(result=result, other=other)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_addition_expression(
        self, *, result: VariableNameMixIn, other: _NumType
    ) -> None:
        """
        Append addition expression.

        Parameters
        ----------
        result : NumberValueMixIn
            Addition result value.
        other : NumberValueMixIn or int or float
            Other value to add.
        """
        import apysc as ap
        from apysc._type.value_util import get_value_str_for_expression

        right_value: str = get_value_str_for_expression(value=other)
        expression: str = (
            f"var {result.variable_name} = " f"{self.variable_name} + {right_value};"
        )
        ap.append_js_expression(expression=expression)

    @final
    @arg_validation_decos.is_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def __sub__(self, other: _NumType) -> Any:
        """
        Method for subtraction.

        Parameters
        ----------
        other : NumberValueMixIn or int or float
            The other value to subtract.

        Returns
        -------
        result : NumberValueMixIn
            Subtraction result value.
        """
        if isinstance(other, NumberValueMixIn):
            value: _NumType = self._value - other._value
        else:
            value = self._value - other  # type: ignore
        result: NumberValueMixIn = self._copy()
        result._set_value_and_skip_expression_appending(value=value)
        self._append_subtraction_expression(result=result, other=other)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_subtraction_expression(
        self, *, result: VariableNameMixIn, other: _NumType
    ) -> None:
        """
        Append subtraction expression.

        Parameters
        ----------
        result : NumberValueMixIn
            Subtraction result value.
        other : NumberValueMixIn or int or float
            Other value to subtract.
        """
        import apysc as ap
        from apysc._type.value_util import get_value_str_for_expression

        right_value: str = get_value_str_for_expression(value=other)
        expression: str = (
            f"var {result.variable_name} = " f"{self.variable_name} - {right_value};"
        )
        ap.append_js_expression(expression=expression)

    @final
    @arg_validation_decos.is_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def __mul__(self, other: _NumType) -> _InstanceType:
        """
        Method for multiplication.

        Parameters
        ----------
        other : NumberValueMixIn or int or float
            Other value to multiply.

        Returns
        -------
        result : NumberValueMixIn
            Multiplication result value.
        """
        if isinstance(other, NumberValueMixIn):
            value: _NumType = self._value * other._value
        else:
            value = self._value * other  # type: ignore
        result: _InstanceType = self._copy()
        result._set_value_and_skip_expression_appending(value=value)
        self._append_multiplication_expression(result=result, other=other)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_multiplication_expression(
        self, *, result: VariableNameMixIn, other: _NumType
    ) -> None:
        """
        Append multiplication expression.

        Parameters
        ----------
        result : NumberValueMixIn
            Multiplication result value.
        other : NumberValueMixIn or int or float
            Other value to multiply.
        """
        import apysc as ap
        from apysc._type.value_util import get_value_str_for_expression

        right_value: str = get_value_str_for_expression(value=other)
        expression: str = (
            f"var {result.variable_name} = " f"{self.variable_name} * {right_value};"
        )
        ap.append_js_expression(expression=expression)

    @final
    @arg_validation_decos.is_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def __truediv__(self, other: _NumType) -> Any:
        """
        Method for true division (returns floating-point number).

        Parameters
        ----------
        other : NumberValueMixIn or int or float
            Other value for true-division.

        Returns
        -------
        result : Number
            True division result value.
        """
        import apysc as ap

        result: ap.Number = ap.Number(value=self)
        if isinstance(other, NumberValueMixIn):
            value: _NumType = result._value / other._value
        else:
            value = result._value / other  # type: ignore
        result._set_value_and_skip_expression_appending(value=value)
        self._append_true_division_expression(result=result, other=other)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_true_division_expression(
        self, *, result: VariableNameMixIn, other: _NumType
    ) -> None:
        """
        Append true division expression.

        Parameters
        ----------
        result : NumberValueMixIn
            True division result value.
        other : NumberValueMixIn or int or float
            Other value for true division.
        """
        import apysc as ap
        from apysc._type.value_util import get_value_str_for_expression

        right_value: str = get_value_str_for_expression(value=other)
        expression: str = (
            f"{result.variable_name} = {self.variable_name} / " f"{right_value};"
        )
        ap.append_js_expression(expression=expression)

    @final
    @arg_validation_decos.is_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def __floordiv__(self, other: _NumType) -> Any:
        """
        Method for floor division (return integer).

        Parameters
        ----------
        other : NumberValueMixIn or int or float
            Other value for floor division.

        Returns
        -------
        result : Int
            Floor division result value.
        """
        import apysc as ap

        result: ap.Int = ap.Int(value=self)
        if isinstance(other, NumberValueMixIn):
            value: _NumType = self._value // other._value
        else:
            value = self._value // other  # type: ignore
        result._set_value_and_skip_expression_appending(value=value)
        self._append_floor_division_expression(result=result, other=other)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_floor_division_expression(
        self, *, result: VariableNameMixIn, other: _NumType
    ) -> None:
        """
        Append floor division expression.

        Parameters
        ----------
        result : NumberValueMixIn
            Floor division result value.
        other : NumberValueMixIn or int or float
            Other value for floor division.
        """
        import apysc as ap
        from apysc._type.value_util import get_value_str_for_expression

        right_value: str = get_value_str_for_expression(value=other)
        expression: str = (
            f"{result.variable_name} = "
            f"Math.trunc({self.variable_name} / {right_value});"
        )
        ap.append_js_expression(expression=expression)

    _incremental_calc_prev_name: str = ""

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_incremental_calc_substitution_expression(self) -> None:
        """
        Append an incremental calculation's substitution expression.
        Each interface call this method.
        """
        from apysc._expression import expression_variables_util

        expression_variables_util.append_substitution_expression_with_names(
            left_variable_name=self._incremental_calc_prev_name,
            right_variable_name=self.variable_name,
        )
        self._incremental_calc_prev_name = ""

    @final
    @arg_validation_decos.is_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def __iadd__(self, other: _NumType) -> _InstanceType:
        """
        Method for incremental addition.

        Parameters
        ----------
        other : NumberValueMixIn or int or float
            Other value for` incremental addition.

        Returns
        -------
        result : NumberValueMixIn
            Incremental addition result value.
        """
        from apysc._expression import expression_variables_util

        self._incremental_calc_prev_name = self._get_previous_variable_name()
        result: _InstanceType = self + other
        expression_variables_util.append_substitution_expression(
            left_value=self, right_value=result
        )
        result.variable_name = self.variable_name
        return result

    @final
    @arg_validation_decos.is_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def __isub__(self, other: _NumType) -> Any:
        """
        Method for incremental subtraction.

        Parameters
        ----------
        other : NumberValueMixIn or int or float
            Other value for incremental subtraction.

        Returns
        -------
        result : NumberValueMixIn
            Incremental subtraction result value.
        """
        from apysc._expression import expression_variables_util

        self._incremental_calc_prev_name = self._get_previous_variable_name()
        result: NumberValueMixIn = self - other
        expression_variables_util.append_substitution_expression(
            left_value=self, right_value=result
        )
        result.variable_name = self.variable_name
        return result

    @final
    @arg_validation_decos.is_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def __imul__(self, other: _NumType) -> _InstanceType:
        """
        Method for incremental multiplication.

        Parameters
        ----------
        other : NumberValueMixIn or int or float
            Other value for incremental multiplication.

        Returns
        -------
        result : NumberValueMixIn
            Incremental multiplication result value.
        """
        from apysc._expression import expression_variables_util

        self._incremental_calc_prev_name = self._get_previous_variable_name()
        result: _InstanceType = self * other
        expression_variables_util.append_substitution_expression(
            left_value=self, right_value=result
        )
        result.variable_name = self.variable_name
        return result

    @final
    @arg_validation_decos.is_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def __itruediv__(self, other: _NumType) -> Any:
        """
        Method for incremental true division.

        Parameters
        ----------
        other : NumberValueMixIn or int or float
            Other value for incremental true division.

        Returns
        -------
        result : NumberValueMixIn
            The other value for incremental-true division.
        """
        from apysc._expression import expression_variables_util

        self._incremental_calc_prev_name = self._get_previous_variable_name()
        result: NumberValueMixIn = self / other
        result._incremental_calc_prev_name = self._incremental_calc_prev_name
        expression_variables_util.append_substitution_expression(
            left_value=self, right_value=result
        )
        result.variable_name = self.variable_name
        return result

    @final
    @arg_validation_decos.is_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def __mod__(self, other: _NumType) -> _InstanceType:
        """
        Method for the modulo operation.

        Parameters
        ----------
        other : NumberValueMixIn or int or float
            The other value to use in the modulo operation.

        Returns
        -------
        result : NumberValueMixIn
            Modulo operation result value.
        """
        if isinstance(other, NumberValueMixIn):
            value: Union[int, float] = self._value % other._value
        else:
            value = self._value % other  # type: ignore
        result: _InstanceType = self._copy()
        result._set_value_and_skip_expression_appending(value=value)
        self._append_modulo_expression(result=result, other=other)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_modulo_expression(
        self, *, result: VariableNameMixIn, other: _NumType
    ) -> None:
        """
        Append a module expression.

        Parameters
        ----------
        result : NumberValueMixIn
            Modulo operation result value.
        other : NumberValueMixIn or int or float
            The other value to use in the modulo operation.
        """
        import apysc as ap
        from apysc._type.value_util import get_value_str_for_expression

        right_value: str = get_value_str_for_expression(value=other)
        expression: str = (
            f"var {result.variable_name} = " f"{self.variable_name} % {right_value};"
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
        if not hasattr(self, "_value"):
            return "0"
        return str(self._value)

    @final
    def __int__(self) -> int:
        """
        Integer conversion method.

        Returns
        -------
        integer : int
            Converted integer value.
        """
        return int(self._value)

    @final
    def __float__(self) -> float:
        """
        Float conversion method.

        Returns
        -------
        float_ : float
            Converted float value.
        """
        return float(self._value)

    @final
    @add_debug_info_setting(module_name=__name__)
    def __eq__(self, other: Any) -> Any:
        """
        Equal comparison method.

        Parameters
        ----------
        other : *
            The other value to compare. Builtin types, Int,
            and Number class instances are acceptable.

        Returns
        -------
        result : Boolean
            If a specified value is the same amount, this interface
            returns True.
        """
        import apysc as ap

        if isinstance(other, NumberValueMixIn):
            result: ap.Boolean = ap.Boolean(
                self._value == other._value,
                variable_name_suffix=self._variable_name_suffix,
            )
        else:
            result = ap.Boolean(
                self._value == other, variable_name_suffix=self._variable_name_suffix
            )
        other = self._convert_other_val_to_int_or_number(other=other)
        if isinstance(other, VariableNameMixIn):
            self._append_eq_expression(result=result, other=other)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _convert_other_val_to_int_or_number(self, *, other: Any) -> Any:
        """
        Convert a specified other value if comparison
        its type is an int or float, then convert it
        to Int or Number.

        Parameters
        ----------
        other : *
            Other comparison value.

        Returns
        -------
        converted_val : *
            Converted value. If an int is specified, this
            interface converts it to an Int. Similarly, if a
            float is specified, this interface converts it
            to a Number value. This interface returns the
            other type directly (not to be converted).
        """
        import apysc as ap

        if isinstance(other, int):
            return ap.Int(other, variable_name_suffix=self._variable_name_suffix)
        if isinstance(other, float):
            return ap.Number(other, variable_name_suffix=self._variable_name_suffix)
        return other

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_eq_expression(
        self, *, result: VariableNameMixIn, other: VariableNameMixIn
    ) -> None:
        """
        Append __eq__ method expression.

        Parameters
        ----------
        result : Boolean
            Result boolean value.
        other : VariableNameMixIn
            The other value to compare.
        """
        import apysc as ap

        expression: str = (
            f"{result.variable_name} = "
            f"{self.variable_name} === {other.variable_name};"
        )
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def __ne__(self, other: Any) -> Any:
        """
        Not equal comparison method.

        Parameters
        ----------
        other : *
            The other value to compare. Builtin types, Int,
            and Number class instances are acceptable.

        Returns
        -------
        result : Boolean
            If a specified value is not the same amount, this interface
            returns True.
        """
        import apysc as ap

        if isinstance(other, NumberValueMixIn):
            result: ap.Boolean = ap.Boolean(
                self._value != other._value,
                variable_name_suffix=self._variable_name_suffix,
            )
        else:
            result = ap.Boolean(
                self._value != other, variable_name_suffix=self._variable_name_suffix
            )
        other = self._convert_other_val_to_int_or_number(other=other)
        if isinstance(other, VariableNameMixIn):
            self._append_ne_expression(result=result, other=other)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_ne_expression(
        self, *, result: VariableNameMixIn, other: VariableNameMixIn
    ) -> None:
        """
        Append __ne__ method expression.

        Parameters
        ----------
        result : Boolean
            Result boolean value.
        other : VariableNameMixIn
            The other value to compare.
        """
        import apysc as ap

        expression: str = (
            f"{result.variable_name} = "
            f"{self.variable_name} !== {other.variable_name};"
        )
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def __lt__(self, other: Any) -> Any:
        """
        Less than comparison method.

        Parameters
        ----------
        other : *
            The other value to compare. Builtin types, Int,
            and Number class instances are acceptable.

        Returns
        -------
        result : Boolean
            If this value is less than a specified value,
            this interface returns True.
        """
        import apysc as ap

        if isinstance(other, NumberValueMixIn):
            result: ap.Boolean = ap.Boolean(
                self._value < other._value,
                variable_name_suffix=self._variable_name_suffix,
            )
        else:
            result = ap.Boolean(
                self._value < other, variable_name_suffix=self._variable_name_suffix
            )
        other = self._convert_other_val_to_int_or_number(other=other)
        if isinstance(other, VariableNameMixIn):
            self._append_lt_expression(result=result, other=other)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_lt_expression(
        self, *, result: VariableNameMixIn, other: VariableNameMixIn
    ) -> None:
        """
        Append __lt__ method expression.

        Parameters
        ----------
        result : Boolean
            Result boolean value.
        other : VariableNameMixIn
            The other value to compare.
        """
        import apysc as ap

        expression: str = (
            f"{result.variable_name} = "
            f"{self.variable_name} < {other.variable_name};"
        )
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def __le__(self, other: Any) -> Any:
        """
        Less than equal comparison method.

        Parameters
        ----------
        other : *
            The other value to compare. Builtin types, Int,
            and Number class instances are acceptable.

        Returns
        -------
        result : Boolean
            If this value is less than or equal to a specified
            value, this interface returns True.
        """
        import apysc as ap

        if isinstance(other, NumberValueMixIn):
            result: ap.Boolean = ap.Boolean(
                self._value <= other._value,
                variable_name_suffix=self._variable_name_suffix,
            )
        else:
            result = ap.Boolean(
                self._value <= other, variable_name_suffix=self._variable_name_suffix
            )
        other = self._convert_other_val_to_int_or_number(other=other)
        if isinstance(other, VariableNameMixIn):
            self._append_le_expression(result=result, other=other)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_le_expression(
        self, *, result: VariableNameMixIn, other: VariableNameMixIn
    ) -> None:
        """
        Append __le__ method expression.

        Parameters
        ----------
        result : Boolean
            Result boolean value.
        other : VariableNameMixIn
            The other value to compare.
        """
        import apysc as ap

        expression: str = (
            f"{result.variable_name} = "
            f"{self.variable_name} <= {other.variable_name};"
        )
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def __gt__(self, other: Any) -> Any:
        """
        Greater than comparison method.

        Parameters
        ----------
        other : *
            The other value to compare. Builtin types, Int,
            and Number class instances are acceptable.

        Returns
        -------
        result : Boolean
            If this value is greater than a specified value,
            this interface returns True.
        """
        import apysc as ap

        if isinstance(other, NumberValueMixIn):
            result: ap.Boolean = ap.Boolean(
                self._value > other._value,
                variable_name_suffix=self._variable_name_suffix,
            )
        else:
            result = ap.Boolean(
                self._value > other, variable_name_suffix=self._variable_name_suffix
            )
        other = self._convert_other_val_to_int_or_number(other=other)
        if isinstance(other, NumberValueMixIn):
            self._append_gt_expression(result=result, other=other)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_gt_expression(
        self, *, result: VariableNameMixIn, other: VariableNameMixIn
    ) -> None:
        """
        Append __gt__ expression.

        Parameters
        ----------
        result : Boolean
            Result boolean value.
        other : VariableNameMixIn
            The other value to compare.
        """
        import apysc as ap

        expression: str = (
            f"{result.variable_name} = "
            f"{self.variable_name} > {other.variable_name};"
        )
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def __ge__(self, other: Any) -> Any:
        """
        Greater than equal comparison method.

        Parameters
        ----------
        other : *
            The other value to compare. Builtin types, Int,
            and Number class instances are acceptable.

        Returns
        -------
        result : Boolean
            If this value is greater than or equal to a specified
            value, this interface returns True.
        """
        import apysc as ap

        if isinstance(other, NumberValueMixIn):
            result: ap.Boolean = ap.Boolean(
                self._value >= other._value,
                variable_name_suffix=self._variable_name_suffix,
            )
        else:
            result = ap.Boolean(
                self._value >= other, variable_name_suffix=self._variable_name_suffix
            )
        other = self._convert_other_val_to_int_or_number(other=other)
        if isinstance(other, VariableNameMixIn):
            self._append_ge_expression(result=result, other=other)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_ge_expression(
        self, *, result: VariableNameMixIn, other: VariableNameMixIn
    ) -> None:
        """
        Append __ge__ expression.

        Parameters
        ----------
        result : Boolean
            Result boolean value.
        other : VariableNameMixIn
            The other value to compare.
        """
        import apysc as ap

        expression: str = (
            f"{result.variable_name} = "
            f"{self.variable_name} >= {other.variable_name};"
        )
        ap.append_js_expression(expression=expression)

    _value_snapshots: Dict[str, _ValueType]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._set_single_snapshot_val_to_dict(
            dict_name="_value_snapshots", value=self._value, snapshot_name=snapshot_name
        )

    def _revert(self, *, snapshot_name: str) -> None:
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
