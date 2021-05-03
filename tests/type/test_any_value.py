from random import randint

from retrying import retry

from apysc import AnyValue, Boolean
from apysc import Int
from apysc.expression import expression_file_util
from apysc.expression import var_names
from apysc.type.variable_name_interface import VariableNameInterface


class TestAnyValue:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        any_value: AnyValue = AnyValue(100)
        assert any_value._value == 100
        assert any_value.variable_name.startswith(var_names.ANY)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_constructor_expression(self) -> None:
        expression_file_util.remove_expression_file()
        any_value_1: AnyValue = AnyValue(100)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{any_value_1.variable_name} = 100;'
        )
        assert expected in expression

        expression_file_util.remove_expression_file()
        int_1: Int = Int(10)
        any_value_2: AnyValue = AnyValue(int_1)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{any_value_2.variable_name} = {int_1.variable_name};'
        )
        assert expected in expression

        expression_file_util.remove_expression_file()
        any_value_3 = AnyValue(None)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'var {any_value_3.variable_name} = NaN;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_value_setter_expression(self) -> None:
        expression_file_util.remove_expression_file()
        any_value: AnyValue = AnyValue(100)
        any_value.value = 200
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{any_value.variable_name} = 200;'
        )
        assert expected in expression

        int_1: Int = Int(300)
        any_value.value = int_1
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{any_value.variable_name} = {int_1.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_value(self) -> None:
        any_value: AnyValue = AnyValue(100)
        any_value.value = 200
        assert any_value.value == 200

    def _assert_arithmetic_operation_dunder_method_expression(
            self, any_value: AnyValue, result: VariableNameInterface,
            other: VariableNameInterface,
            expected_operator: str) -> None:
        """
        Assert arithmetic operation dunder method (e.g., __add__)
        expression.

        Parameters
        ----------
        any_value : AnyValue
            AnyValue instance.
        result : VariableNameInterface
            Result value instance.
        other : VariableNameInterface
            Other value instance.
        expected_operator : str
            Expected arithmetic operator string, e.g., '+'.

        Raises
        ------
        AssertionError
            If saved expression is invalid.
        """
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{result.variable_name} = {any_value.variable_name} '
            f'{expected_operator} '
            f'{other.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___add__(self) -> None:
        expression_file_util.remove_expression_file()
        any_value: AnyValue = AnyValue(100)
        int_1: Int = Int(200)
        result: VariableNameInterface = any_value + int_1
        assert isinstance(result, AnyValue)
        self._assert_arithmetic_operation_dunder_method_expression(
            any_value=any_value, result=result, other=int_1,
            expected_operator='+')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___sub__(self) -> None:
        expression_file_util.remove_expression_file()
        any_value: AnyValue = AnyValue(100)
        int_1: Int = Int(200)
        result: VariableNameInterface = any_value - int_1
        assert isinstance(result, AnyValue)
        self._assert_arithmetic_operation_dunder_method_expression(
            any_value=any_value, result=result, other=int_1,
            expected_operator='-')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_arithmetic_operation_expression(self) -> None:
        expression_file_util.remove_expression_file()
        any_value: AnyValue = AnyValue(100)
        int_1: Int = Int(200)
        result: VariableNameInterface = \
            any_value._append_arithmetic_operation_expression(
                other=int_1, operator='/')
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{result.variable_name} = '
            f'{any_value.variable_name} / {int_1.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___mul__(self) -> None:
        expression_file_util.remove_expression_file()
        any_value: AnyValue = AnyValue(100)
        int_1: Int = Int(200)
        result: VariableNameInterface = any_value * int_1
        assert isinstance(result, AnyValue)
        self._assert_arithmetic_operation_dunder_method_expression(
            any_value=any_value, result=result, other=int_1,
            expected_operator='*')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___truediv__(self) -> None:
        expression_file_util.remove_expression_file()
        any_value: AnyValue = AnyValue(100)
        int_1: Int = Int(200)
        result: VariableNameInterface = any_value / int_1
        assert isinstance(result, AnyValue)
        self._assert_arithmetic_operation_dunder_method_expression(
            any_value=any_value, result=result, other=int_1,
            expected_operator='/')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___floordiv__(self) -> None:
        expression_file_util.remove_expression_file()
        any_value: AnyValue = AnyValue(200)
        int_1: Int = Int(100)
        result: VariableNameInterface = any_value // int_1
        assert isinstance(result, AnyValue)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{result.variable_name} = '
            f'parseInt({any_value.variable_name} / {int_1.variable_name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_incremental_arithmetic_operation_expression(
            self) -> None:
        expression_file_util.remove_expression_file()
        any_value: AnyValue = AnyValue(200)
        int_1: Int = Int(100)
        any_value._append_incremental_arithmetic_operation_expression(
            other=int_1, operator='*=')
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{any_value.variable_name} *= {int_1.variable_name};'
        )
        assert expected in expression

    def _assert_incremental_arithmetic_operation_result(
            self, any_value: AnyValue, before_var_name: str,
            other_value: VariableNameInterface,
            expected_operator: str) -> None:
        """
        Assert incremental arithmetic operation result (check
        variable name and saved expression).

        Parameters
        ----------
        any_value : AnyValue
            Target AnyValue instance.
        before_var_name : str
            Variable name before incremental arithmetic operation.
        other_value : VariableNameInterface
            Other value instance.
        expected_operator : str
            Expected incremental arithmetic operator, like '+=', '*=',
            and so on.
        """
        assert before_var_name == any_value.variable_name
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{any_value.variable_name} {expected_operator} '
            f'{other_value.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___iadd__(self) -> None:
        expression_file_util.remove_expression_file()
        any_value: AnyValue = AnyValue(200)
        before_var_name: str = any_value.variable_name
        int_1: Int = Int(100)
        any_value += int_1
        self._assert_incremental_arithmetic_operation_result(
            any_value=any_value, before_var_name=before_var_name,
            other_value=int_1, expected_operator='+=')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___isub__(self) -> None:
        expression_file_util.remove_expression_file()
        any_value: AnyValue = AnyValue(200)
        before_var_name: str = any_value.variable_name
        int_1: Int = Int(100)
        any_value -= int_1
        self._assert_incremental_arithmetic_operation_result(
            any_value=any_value, before_var_name=before_var_name,
            other_value=int_1, expected_operator='-=')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___imul__(self) -> None:
        expression_file_util.remove_expression_file()
        any_value: AnyValue = AnyValue(200)
        before_var_name: str = any_value.variable_name
        int_1: Int = Int(100)
        any_value *= int_1
        self._assert_incremental_arithmetic_operation_result(
            any_value=any_value, before_var_name=before_var_name,
            other_value=int_1, expected_operator='*=')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___itruediv__(self) -> None:
        expression_file_util.remove_expression_file()
        any_value: AnyValue = AnyValue(200)
        before_var_name: str = any_value.variable_name
        int_1: Int = Int(100)
        any_value /= int_1
        self._assert_incremental_arithmetic_operation_result(
            any_value=any_value, before_var_name=before_var_name,
            other_value=int_1, expected_operator='/=')

    def _assert_comparison_operation_result(
            self, any_value: AnyValue, result: Boolean,
            other: VariableNameInterface,
            expected_comparison_operator: str) -> None:
        """
        Assert comparison operation result (type checking
        and saved expression).

        Parameters
        ----------
        any_value : AnyValue
            Target AnyValue instance.
        result : Boolean
            Comparison result value.
        other : VariableNameInterface
            Other value to compare.
        expected_comparison_operator : str
            Expected comparison operator string, like '!==', '>=',
            and so on.
        """
        assert isinstance(result, Boolean)
        expression = expression_file_util.get_current_expression()
        expected: str = (
            f'{result.variable_name} = {any_value.variable_name} '
            f'{expected_comparison_operator} {other.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_comparison_expression(self) -> None:
        expression_file_util.remove_expression_file()
        any_value: AnyValue = AnyValue(200)
        int_1: Int = Int(100)
        result: Boolean = any_value._append_comparison_expression(
            comparison_operator='<=', other=int_1)
        self._assert_comparison_operation_result(
            any_value=any_value, result=result,
            other=int_1, expected_comparison_operator='<=')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___eq__(self) -> None:
        expression_file_util.remove_expression_file()
        any_value: AnyValue = AnyValue(200)
        int_1: Int = Int(100)
        result: Boolean = any_value == int_1
        self._assert_comparison_operation_result(
            any_value=any_value, result=result, other=int_1,
            expected_comparison_operator='===')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___ne__(self) -> None:
        expression_file_util.remove_expression_file()
        any_value: AnyValue = AnyValue(200)
        int_1: Int = Int(100)
        result: Boolean = any_value != int_1
        self._assert_comparison_operation_result(
            any_value=any_value, result=result, other=int_1,
            expected_comparison_operator='!==')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___lt__(self) -> None:
        expression_file_util.remove_expression_file()
        any_value: AnyValue = AnyValue(200)
        int_1: Int = Int(100)
        result: Boolean = any_value < int_1
        self._assert_comparison_operation_result(
            any_value=any_value, result=result, other=int_1,
            expected_comparison_operator='<')
