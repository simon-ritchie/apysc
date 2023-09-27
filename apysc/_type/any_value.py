"""Class implementation of any value.
"""

from typing import Any
from typing import Dict
from typing import Optional

from typing_extensions import final

from apysc._event.custom_event_mixin import CustomEventMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.boolean import Boolean
from apysc._type.copy_mixin import CopyMixIn
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.to_string_mixin import ToStringMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos


class AnyValue(
    ToStringMixIn,
    CopyMixIn["AnyValue"],
    RevertMixIn,
    CustomEventMixIn,
    VariableNameSuffixMixIn,
):
    """
    Class implementation of any value (a value that can't
    determine type).

    Examples
    --------
    >>> import apysc as ap
    >>> any_value: ap.AnyValue = ap.AnyValue(10)
    >>> any_value.value
    10

    >>> any_value.value = 20
    >>> any_value.value
    20
    """

    _value: Any

    @final
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(self, value: Any, *, variable_name_suffix: str = "") -> None:
        """
        Class implementation of any value (a value that can't
        determine type).

        Parameters
        ----------
        value : *
            Initial any value.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Examples
        --------
        >>> import apysc as ap
        >>> any_value: ap.AnyValue = ap.AnyValue(10)
        >>> any_value.value
        10
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        self._variable_name_suffix = variable_name_suffix
        TYPE_NAME: str = var_names.ANY
        self._value = value
        self.variable_name = expression_variables_util.get_next_variable_name(
            type_name=TYPE_NAME
        )
        self._type_name = TYPE_NAME
        self._append_constructor_expression()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression.
        """
        from apysc._expression import expression_data_util
        from apysc._type import value_util

        expression: str = f"var {self.variable_name} = "
        if isinstance(self._value, VariableNameMixIn):
            expression += f"{self._value.variable_name};"
        else:
            value_str: str = value_util.get_value_str_for_expression(value=self._value)
            expression += f"{value_str};"
        expression_data_util.append_js_expression(expression=expression)

    @property
    @add_debug_info_setting(module_name=__name__)
    def value(self) -> Any:
        """
        Get a current value.

        Returns
        -------
        value : *
            Any value.

        Examples
        --------
        >>> import apysc as ap
        >>> any_value: ap.AnyValue = ap.AnyValue(10)
        >>> any_value.value = 20
        >>> any_value.value
        20
        """
        if isinstance(self._value, CopyMixIn):
            return self._value._copy()
        return self._value

    @value.setter
    @add_debug_info_setting(module_name=__name__)
    def value(self, value: Any) -> None:
        """
        Set a any value.

        Parameters
        ----------
        value : *
            Any value to set.
        """
        self._value = value
        self._append_value_setter_expression(value=value)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_value_setter_expression(self, *, value: Any) -> None:
        """
        Append value's setter expression.

        Parameters
        ----------
        value : *
            Any value to set.
        """
        from apysc._expression import expression_data_util

        expression: str = f"{self.variable_name} = "
        if isinstance(value, VariableNameMixIn):
            expression += f"{value.variable_name};"
        else:
            expression += f"{value};"
        expression_data_util.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_arithmetic_operation_expression(
        self, *, other: Any, operator: str
    ) -> VariableNameMixIn:
        """
        Append arithmetic operation (e.g., addition) expression.

        Parameters
        ----------
        other : Any
            Other value to use.
        operator : str
            JavaScript arithmetic operator, like '+', '*', and so on.

        Returns
        -------
        result : AnyValue
            Calculated result value.
        """
        from apysc._expression import expression_data_util
        from apysc._type.value_util import get_value_str_for_expression

        value_str: str = get_value_str_for_expression(value=other)
        result: AnyValue = self._copy()
        expression: str = (
            f"{result.variable_name} = " f"{self.variable_name} {operator} {value_str};"
        )
        expression_data_util.append_js_expression(expression=expression)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def __add__(self, other: Any) -> Any:
        """
        Method for addition.

        Parameters
        ----------
        other : Any
            Other value to add.

        Returns
        -------
        result : AnyValue
            Addition result value.
        """
        result: VariableNameMixIn = self._append_arithmetic_operation_expression(
            other=other, operator="+"
        )
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def __sub__(self, other: Any) -> Any:
        """
        Method for subtraction.

        Parameters
        ----------
        other : Any
            The other value to subtract.

        Returns
        -------
        result : AnyValue
            Subtraction result value.
        """
        result: VariableNameMixIn = self._append_arithmetic_operation_expression(
            other=other, operator="-"
        )
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def __mul__(self, other: Any) -> Any:
        """
        Method for multiplication.

        Parameters
        ----------
        other : Any
            Other value to multiply.

        Returns
        -------
        result : AnyValue
            Subtraction result value.
        """
        result: VariableNameMixIn = self._append_arithmetic_operation_expression(
            other=other, operator="*"
        )
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def __truediv__(self, other: Any) -> Any:
        """
        Method for true division.

        Parameters
        ----------
        other : Any
            Other value for true division.

        Returns
        -------
        result : AnyValue
            True division result value.
        """
        result: VariableNameMixIn = self._append_arithmetic_operation_expression(
            other=other, operator="/"
        )
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def __floordiv__(self, other: Any) -> Any:
        """
        Method for floor division.

        Parameters
        ----------
        other : Any
            Other value for floor division.

        Returns
        -------
        result : AnyValue
            Floor division result value.
        """
        from apysc._expression import expression_data_util
        from apysc._type.value_util import get_value_str_for_expression

        result: AnyValue = self._copy()
        value_str: str = get_value_str_for_expression(value=other)
        expression: str = (
            f"{result.variable_name} = "
            f"Math.trunc({self.variable_name} / {value_str});"
        )
        expression_data_util.append_js_expression(expression=expression)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_incremental_arithmetic_operation_expression(
        self, *, other: Any, operator: str
    ) -> None:
        """
        Append incremental arithmetic operation (e.g., incremental
        addition) expression.

        Parameters
        ----------
        other : Any
            Other value to use.
        operator : str
            JavaScript arithmetic operator, like '+=', '*=', and so on.
        """
        from apysc._expression import expression_data_util
        from apysc._type.value_util import get_value_str_for_expression

        value_str: str = get_value_str_for_expression(value=other)
        expression: str = f"{self.variable_name} {operator} {value_str};"
        expression_data_util.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def __iadd__(self, other: Any) -> Any:
        """
        Method for incremental addition.

        Parameters
        ----------
        other : Any
            Other value for incremental addition.

        Returns
        -------
        result : AnyValue
            Incremental addition result value.
        """
        self._append_incremental_arithmetic_operation_expression(
            other=other, operator="+="
        )
        return self

    @final
    @add_debug_info_setting(module_name=__name__)
    def __isub__(self, other: Any) -> Any:
        """
        Method for incremental subtraction.

        Parameters
        ----------
        other : Any
            Other value for incremental subtraction.

        Returns
        -------
        result : AnyValue
            Incremental subtraction result value.
        """
        self._append_incremental_arithmetic_operation_expression(
            other=other, operator="-="
        )
        return self

    @final
    @add_debug_info_setting(module_name=__name__)
    def __imul__(self, other: Any) -> Any:
        """
        Method for incremental multiplication.

        Parameters
        ----------
        other : Any
            Other value for incremental multiplication.

        Returns
        -------
        result : AnyValue
            Incremental multiplication result value.
        """
        self._append_incremental_arithmetic_operation_expression(
            other=other, operator="*="
        )
        return self

    @final
    @add_debug_info_setting(module_name=__name__)
    def __itruediv__(self, other: Any) -> Any:
        """
        Method for incremental true division.

        Parameters
        ----------
        other : Any
            Other value for incremental division.

        Returns
        -------
        result : AnyValue
            Incremental division result value.
        """
        self._append_incremental_arithmetic_operation_expression(
            other=other, operator="/="
        )
        return self

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_comparison_expression(
        self, *, comparison_operator: str, other: Any
    ) -> Boolean:
        """
        Append comparison operation expression.

        Parameters
        ----------
        comparison_operator : str
            JavaScript comparison operator (e.g., '===', '>=',
            and so on).
        other : Any
            The other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result. This value always becomes
            False on Python since the correct comparison
            is impossible.
        """
        from apysc._expression import expression_data_util
        from apysc._type.value_util import get_value_str_for_expression

        result: Boolean = Boolean(False)
        value_str: str = get_value_str_for_expression(value=other)
        expression: str = (
            f"{result.variable_name} = "
            f"{self.variable_name} {comparison_operator} {value_str};"
        )
        expression_data_util.append_js_expression(expression=expression)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def __eq__(self, other: Any) -> Any:
        """
        Equal comparison method.

        Parameters
        ----------
        other : Any
            The other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result. This value always becomes
            False on Python since the correct comparison
            is impossible.
        """
        result: Boolean = self._append_comparison_expression(
            comparison_operator="===", other=other
        )
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def __ne__(self, other: Any) -> Any:
        """
        Not equal comparison method.

        Parameters
        ----------
        other : Any
            The other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result. This value always becomes
            False on Python since the correct comparison
            is impossible.
        """
        result: Boolean = self._append_comparison_expression(
            comparison_operator="!==", other=other
        )
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def __lt__(self, other: Any) -> Boolean:
        """
        Less than comparison method.

        Parameters
        ----------
        other : Any
            The other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result. This value always becomes
            False on Python since the correct comparison
            is impossible.
        """
        result: Boolean = self._append_comparison_expression(
            comparison_operator="<", other=other
        )
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def __le__(self, other: Any) -> Boolean:
        """
        Less than equal comparison method.

        Parameters
        ----------
        other : Any
            The other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result. This value always becomes
            False on Python since the correct comparison
            is impossible.
        """
        result: Boolean = self._append_comparison_expression(
            comparison_operator="<=", other=other
        )
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def __gt__(self, other: Any) -> Boolean:
        """
        Greater than comparison method.

        Parameters
        ----------
        other : Any
            The other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result. This value always becomes
            False on Python since the correct comparison
            is impossible.
        """
        result: Boolean = self._append_comparison_expression(
            comparison_operator=">", other=other
        )
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def __ge__(self, other: Any) -> Boolean:
        """
        Greater than equal comparison method.

        Parameters
        ----------
        other : Any
            The other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result. This value always becomes
            False on Python since the correct comparison is impossible.
        """
        result: Boolean = self._append_comparison_expression(
            comparison_operator=">=", other=other
        )
        return result

    _any_value_snapshots: Optional[Dict[str, Any]] = None

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._set_single_snapshot_val_to_dict(
            dict_name="_any_value_snapshots",
            value=self._value,
            snapshot_name=snapshot_name,
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._value = self._get_snapshot_val_if_exists(
            current_value=self._value,
            snapshot_dict=self._any_value_snapshots,
            snapshot_name=snapshot_name,
        )
