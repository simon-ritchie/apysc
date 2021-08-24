"""Class implementation of any value.
"""

from typing import Any
from typing import Dict

import apysc as ap
from apysc._event.custom_event_interface import CustomEventInterface
from apysc._type.copy_interface import CopyInterface
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class AnyValue(CopyInterface, RevertInterface, CustomEventInterface):
    """
    Class implementation of any value (value that can't determine type).
    """

    _value: Any

    def __init__(self, value: Any) -> None:
        """
        Class implementation of any value (value that can't determine
        type).

        Parameters
        ----------
        value : *
            Initial any value.
        """
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=AnyValue):
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            TYPE_NAME: str = var_names.ANY
            self._value = value
            self.variable_name = expression_variables_util.\
                get_next_variable_name(type_name=TYPE_NAME)
            self._type_name = TYPE_NAME
            self._append_constructor_expression()

    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression.
        """
        with ap.DebugInfo(
                callable_=self._append_constructor_expression,
                locals_=locals(),
                module_name=__name__, class_=AnyValue):
            from apysc._type import value_util
            expression: str = f'var {self.variable_name} = '
            if isinstance(self._value, VariableNameInterface):
                expression += f'{self._value.variable_name};'
            else:
                value_str: str = value_util.get_value_str_for_expression(
                    value=self._value)
                expression += f'{value_str};'
            ap.append_js_expression(expression=expression)

    @property
    def value(self) -> Any:
        """
        Get a current value.

        Returns
        -------
        value : *
            Any value.
        """
        return self._value

    @value.setter
    def value(self, value: Any) -> None:
        """
        Set a any value.

        Parameters
        ----------
        value : *
            Any value to set.
        """
        with ap.DebugInfo(
                callable_='value', locals_=locals(),
                module_name=__name__, class_=AnyValue):
            self._value = value
            self._append_value_setter_expression(value=value)

    def _append_value_setter_expression(self, value: Any) -> None:
        """
        Append value's setter expression.

        Parameters
        ----------
        value : *
            Any value to set.
        """
        with ap.DebugInfo(
                callable_=self._append_value_setter_expression,
                locals_=locals(),
                module_name=__name__, class_=AnyValue):
            expression: str = f'{self.variable_name} = '
            if isinstance(value, VariableNameInterface):
                expression += f'{value.variable_name};'
            else:
                expression += f'{value};'
            ap.append_js_expression(expression=expression)

    def _append_arithmetic_operation_expression(
            self, other: Any, operator: str) -> VariableNameInterface:
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
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_arithmetic_operation_expression,
                locals_=locals(),
                module_name=__name__, class_=AnyValue):
            from apysc._type.value_util import get_value_str_for_expression
            value_str: str = get_value_str_for_expression(value=other)
            result: AnyValue = self._copy()
            expression: str = (
                f'{result.variable_name} = '
                f'{self.variable_name} {operator} {value_str};'
            )
            ap.append_js_expression(expression=expression)
            return result

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
        with ap.DebugInfo(
                callable_='__add__', locals_=locals(),
                module_name=__name__, class_=AnyValue):
            result: VariableNameInterface = \
                self._append_arithmetic_operation_expression(
                    other=other, operator='+')
            return result

    def __sub__(self, other: Any) -> Any:
        """
        Method for subtraction.

        Parameters
        ----------
        other : Any
            Other value to subtract.

        Returns
        -------
        result : AnyValue
            Subtraction result value.
        """
        with ap.DebugInfo(
                callable_='__sub__', locals_=locals(),
                module_name=__name__, class_=AnyValue):
            result: VariableNameInterface = \
                self._append_arithmetic_operation_expression(
                    other=other, operator='-')
            return result

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
        with ap.DebugInfo(
                callable_='__mul__', locals_=locals(),
                module_name=__name__, class_=AnyValue):
            result: VariableNameInterface = \
                self._append_arithmetic_operation_expression(
                    other=other, operator='*')
            return result

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
        with ap.DebugInfo(
                callable_='__truediv__', locals_=locals(),
                module_name=__name__, class_=AnyValue):
            result: VariableNameInterface = \
                self._append_arithmetic_operation_expression(
                    other=other, operator='/')
            return result

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
        with ap.DebugInfo(
                callable_='__floordiv__', locals_=locals(),
                module_name=__name__, class_=AnyValue):
            from apysc._type.value_util import get_value_str_for_expression
            result: AnyValue = self._copy()
            value_str: str = get_value_str_for_expression(value=other)
            expression: str = (
                f'{result.variable_name} = '
                f'parseInt({self.variable_name} / {value_str});'
            )
            ap.append_js_expression(expression=expression)
            return result

    def _append_incremental_arithmetic_operation_expression(
            self, other: Any, operator: str) -> None:
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
        with ap.DebugInfo(
                callable_=self._append_incremental_arithmetic_operation_expression,  # noqa
                locals_=locals(),
                module_name=__name__, class_=AnyValue):
            from apysc._type.value_util import get_value_str_for_expression
            value_str: str = get_value_str_for_expression(value=other)
            expression: str = (
                f'{self.variable_name} {operator} {value_str};'
            )
            ap.append_js_expression(expression=expression)

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
        with ap.DebugInfo(
                callable_='__iadd__', locals_=locals(),
                module_name=__name__, class_=AnyValue):
            self._append_incremental_arithmetic_operation_expression(
                other=other, operator='+=')
            return self

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
        with ap.DebugInfo(
                callable_='__isub__', locals_=locals(),
                module_name=__name__, class_=AnyValue):
            self._append_incremental_arithmetic_operation_expression(
                other=other, operator='-=')
            return self

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
        with ap.DebugInfo(
                callable_='__imul__', locals_=locals(),
                module_name=__name__, class_=AnyValue):
            self._append_incremental_arithmetic_operation_expression(
                other=other, operator='*=')
            return self

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
        import apysc as ap
        with ap.DebugInfo(
                callable_='__itruediv__', locals_=locals(),
                module_name=__name__, class_=AnyValue):
            self._append_incremental_arithmetic_operation_expression(
                other=other, operator='/=')
            return self

    def _append_comparison_expression(
            self, comparison_operator: str, other: Any) -> ap.Boolean:
        """
        Append comparison operation expression.

        Parameters
        ----------
        comparison_operator : str
            JavaScript comparison operator (e.g., '===', '>=',
            and so on).
        other : Any
            Other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result. This will always be False on Python
            since correct comparison is not possible.
        """
        with ap.DebugInfo(
                callable_=self._append_comparison_expression,
                locals_=locals(),
                module_name=__name__, class_=AnyValue):
            from apysc._type.value_util import get_value_str_for_expression
            result: ap.Boolean = ap.Boolean(False)
            value_str: str = get_value_str_for_expression(value=other)
            expression: str = (
                f'{result.variable_name} = '
                f'{self.variable_name} {comparison_operator} {value_str};'
            )
            ap.append_js_expression(expression=expression)
            return result

    def __eq__(self, other: Any) -> Any:
        """
        Equal comparison method.

        Parameters
        ----------
        other : Any
            Other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result. This will always be False on Python
            since correct comparison is not possible.
        """
        with ap.DebugInfo(
                callable_='__eq__', locals_=locals(),
                module_name=__name__, class_=AnyValue):
            result: ap.Boolean = self._append_comparison_expression(
                comparison_operator='===', other=other)
            return result

    def __ne__(self, other: Any) -> Any:
        """
        Not equal comparison method.

        Parameters
        ----------
        other : Any
            Other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result. This will always be False on Python
            since correct comparison is not possible.
        """
        with ap.DebugInfo(
                callable_='__ne__', locals_=locals(),
                module_name=__name__, class_=AnyValue):
            result: ap.Boolean = self._append_comparison_expression(
                comparison_operator='!==', other=other)
            return result

    def __lt__(self, other: Any) -> ap.Boolean:
        """
        Less than comparison method.

        Parameters
        ----------
        other : Any
            Other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result. This will always be False on Python
            since correct comparison is not possible.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__lt__', locals_=locals(),
                module_name=__name__, class_=AnyValue):
            result: ap.Boolean = self._append_comparison_expression(
                comparison_operator='<', other=other)
            return result

    def __le__(self, other: Any) -> ap.Boolean:
        """
        Less than equal comparison method.

        Parameters
        ----------
        other : Any
            Other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result. This will always be False on Python
            since correct comparison is not possible.
        """
        with ap.DebugInfo(
                callable_='__le__', locals_=locals(),
                module_name=__name__, class_=AnyValue):
            result: ap.Boolean = self._append_comparison_expression(
                comparison_operator='<=', other=other)
            return result

    def __gt__(self, other: Any) -> ap.Boolean:
        """
        Greater than comparison method.

        Parameters
        ----------
        other : Any
            Other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result. This will always be False on Python
            since correct comparison is not possible.
        """
        with ap.DebugInfo(
                callable_='__gt__', locals_=locals(),
                module_name=__name__, class_=AnyValue):
            result: ap.Boolean = self._append_comparison_expression(
                comparison_operator='>', other=other)
            return result

    def __ge__(self, other: Any) -> ap.Boolean:
        """
        Greater than equal comparison method.

        Parameters
        ----------
        other : Any
            Other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result. This will always be False on Python
            since correct comparison is not possible.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__ge__', locals_=locals(),
                module_name=__name__, class_=AnyValue):
            result: ap.Boolean = self._append_comparison_expression(
                comparison_operator='>=', other=other)
            return result

    _any_value_snapshots: Dict[str, Any]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_any_value_snapshots'):
            self._any_value_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._any_value_snapshots[snapshot_name] = self._value

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
        self._value = self._any_value_snapshots[snapshot_name]
