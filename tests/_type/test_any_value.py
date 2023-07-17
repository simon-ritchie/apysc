import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_mixin import VariableNameMixIn


class TestAnyValue:
    @apply_test_settings()
    def test___init__(self) -> None:
        any_value: ap.AnyValue = ap.AnyValue(100, variable_name_suffix="test_any_value")
        assert any_value._value == 100
        assert any_value.variable_name.startswith(var_names.ANY)
        assert any_value._variable_name_suffix == "test_any_value"

    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        any_value_1: ap.AnyValue = ap.AnyValue(100)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{any_value_1.variable_name} = 100;"
        assert expected in expression

        ap.Stage()
        int_1: ap.Int = ap.Int(10)
        any_value_2: ap.AnyValue = ap.AnyValue(int_1)
        expression = expression_data_util.get_current_expression()
        expected = f"{any_value_2.variable_name} = {int_1.variable_name};"
        assert expected in expression

        ap.Stage()
        any_value_3 = ap.AnyValue(None)
        expression = expression_data_util.get_current_expression()
        expected = f"var {any_value_3.variable_name} = null;"
        assert expected in expression

    @apply_test_settings()
    def test__append_value_setter_expression(self) -> None:
        any_value: ap.AnyValue = ap.AnyValue(100)
        any_value.value = 200
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{any_value.variable_name} = 200;"
        assert expected in expression

        int_1: ap.Int = ap.Int(300)
        any_value.value = int_1
        expression = expression_data_util.get_current_expression()
        expected = f"{any_value.variable_name} = {int_1.variable_name};"
        assert expected in expression

    @apply_test_settings()
    def test_value(self) -> None:
        any_value: ap.AnyValue = ap.AnyValue(100)
        any_value.value = 200
        assert any_value.value == 200

        int_val: ap.Int = ap.Int(10)
        any_value = ap.AnyValue(int_val)
        assert isinstance(any_value.value, ap.Int)
        assert any_value.value == 10
        assert any_value.value.variable_name != int_val.variable_name

    def _assert_arithmetic_operation_dunder_method_expression(
        self,
        any_value: ap.AnyValue,
        result: VariableNameMixIn,
        other: VariableNameMixIn,
        expected_operator: str,
    ) -> None:
        """
        Assert arithmetic operation dunder method (e.g., __add__)
        expression.

        Parameters
        ----------
        any_value : AnyValue
            AnyValue instance.
        result : VariableNameMixIn
            Result value instance.
        other : VariableNameMixIn
            Other value instance.
        expected_operator : str
            Expected arithmetic operator string, e.g., '+'.

        Raises
        ------
        AssertionError
            If saved expression is invalid.
        """
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = {any_value.variable_name} "
            f"{expected_operator} "
            f"{other.variable_name};"
        )
        assert expected in expression

    @apply_test_settings()
    def test___add__(self) -> None:
        any_value: ap.AnyValue = ap.AnyValue(100)
        int_1: ap.Int = ap.Int(200)
        result: VariableNameMixIn = any_value + int_1
        assert isinstance(result, ap.AnyValue)
        self._assert_arithmetic_operation_dunder_method_expression(
            any_value=any_value, result=result, other=int_1, expected_operator="+"
        )

    @apply_test_settings()
    def test___sub__(self) -> None:
        any_value: ap.AnyValue = ap.AnyValue(100)
        int_1: ap.Int = ap.Int(200)
        result: VariableNameMixIn = any_value - int_1
        assert isinstance(result, ap.AnyValue)
        self._assert_arithmetic_operation_dunder_method_expression(
            any_value=any_value, result=result, other=int_1, expected_operator="-"
        )

    @apply_test_settings()
    def test__append_arithmetic_operation_expression(self) -> None:
        any_value: ap.AnyValue = ap.AnyValue(100)
        int_1: ap.Int = ap.Int(200)
        result: VariableNameMixIn = any_value._append_arithmetic_operation_expression(
            other=int_1, operator="/"
        )
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"{any_value.variable_name} / {int_1.variable_name};"
        )
        assert expected in expression

    @apply_test_settings()
    def test___mul__(self) -> None:
        any_value: ap.AnyValue = ap.AnyValue(100)
        int_1: ap.Int = ap.Int(200)
        result: VariableNameMixIn = any_value * int_1
        assert isinstance(result, ap.AnyValue)
        self._assert_arithmetic_operation_dunder_method_expression(
            any_value=any_value, result=result, other=int_1, expected_operator="*"
        )

    @apply_test_settings()
    def test___truediv__(self) -> None:
        any_value: ap.AnyValue = ap.AnyValue(100)
        int_1: ap.Int = ap.Int(200)
        result: VariableNameMixIn = any_value / int_1
        assert isinstance(result, ap.AnyValue)
        self._assert_arithmetic_operation_dunder_method_expression(
            any_value=any_value, result=result, other=int_1, expected_operator="/"
        )

    @apply_test_settings()
    def test___floordiv__(self) -> None:
        any_value: ap.AnyValue = ap.AnyValue(200)
        int_1: ap.Int = ap.Int(100)
        result: VariableNameMixIn = any_value // int_1
        assert isinstance(result, ap.AnyValue)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"Math.trunc({any_value.variable_name} / {int_1.variable_name});"
        )
        assert expected in expression

    @apply_test_settings()
    def test__append_incremental_arithmetic_operation_expression(self) -> None:
        any_value: ap.AnyValue = ap.AnyValue(200)
        int_1: ap.Int = ap.Int(100)
        any_value._append_incremental_arithmetic_operation_expression(
            other=int_1, operator="*="
        )
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{any_value.variable_name} *= {int_1.variable_name};"
        assert expected in expression

    def _assert_incremental_arithmetic_operation_result(
        self,
        any_value: ap.AnyValue,
        before_var_name: str,
        other_value: VariableNameMixIn,
        expected_operator: str,
    ) -> None:
        """
        Assert incremental arithmetic operation result (check
        variable name and saved expression).

        Parameters
        ----------
        any_value : AnyValue
            Target AnyValue instance.
        before_var_name : str
            Variable name before incremental arithmetic operation.
        other_value : VariableNameMixIn
            Other value instance.
        expected_operator : str
            Expected incremental arithmetic operator, like '+=', '*=',
            and so on.
        """
        assert before_var_name == any_value.variable_name
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{any_value.variable_name} {expected_operator} "
            f"{other_value.variable_name};"
        )
        assert expected in expression

    @apply_test_settings()
    def test___iadd__(self) -> None:
        any_value: ap.AnyValue = ap.AnyValue(200)
        before_var_name: str = any_value.variable_name
        int_1: ap.Int = ap.Int(100)
        any_value += int_1
        self._assert_incremental_arithmetic_operation_result(
            any_value=any_value,
            before_var_name=before_var_name,
            other_value=int_1,
            expected_operator="+=",
        )

    @apply_test_settings()
    def test___isub__(self) -> None:
        any_value: ap.AnyValue = ap.AnyValue(200)
        before_var_name: str = any_value.variable_name
        int_1: ap.Int = ap.Int(100)
        any_value -= int_1
        self._assert_incremental_arithmetic_operation_result(
            any_value=any_value,
            before_var_name=before_var_name,
            other_value=int_1,
            expected_operator="-=",
        )

    @apply_test_settings()
    def test___imul__(self) -> None:
        any_value: ap.AnyValue = ap.AnyValue(200)
        before_var_name: str = any_value.variable_name
        int_1: ap.Int = ap.Int(100)
        any_value *= int_1
        self._assert_incremental_arithmetic_operation_result(
            any_value=any_value,
            before_var_name=before_var_name,
            other_value=int_1,
            expected_operator="*=",
        )

    @apply_test_settings()
    def test___itruediv__(self) -> None:
        any_value: ap.AnyValue = ap.AnyValue(200)
        before_var_name: str = any_value.variable_name
        int_1: ap.Int = ap.Int(100)
        any_value /= int_1
        self._assert_incremental_arithmetic_operation_result(
            any_value=any_value,
            before_var_name=before_var_name,
            other_value=int_1,
            expected_operator="/=",
        )

    def _assert_comparison_operation_result(
        self,
        any_value: ap.AnyValue,
        result: ap.Boolean,
        other: VariableNameMixIn,
        expected_comparison_operator: str,
    ) -> None:
        """
        Assert comparison operation result (type checking
        and saved expression).

        Parameters
        ----------
        any_value : AnyValue
            Target AnyValue instance.
        result : Boolean
            Comparison result value.
        other : VariableNameMixIn
            Other value to compare.
        expected_comparison_operator : str
            Expected comparison operator string, like '!==', '>=',
            and so on.
        """
        assert isinstance(result, ap.Boolean)
        expression = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = {any_value.variable_name} "
            f"{expected_comparison_operator} {other.variable_name};"
        )
        assert expected in expression

    @apply_test_settings()
    def test__append_comparison_expression(self) -> None:
        any_value: ap.AnyValue = ap.AnyValue(200)
        int_1: ap.Int = ap.Int(100)
        result: ap.Boolean = any_value._append_comparison_expression(
            comparison_operator="<=", other=int_1
        )
        self._assert_comparison_operation_result(
            any_value=any_value,
            result=result,
            other=int_1,
            expected_comparison_operator="<=",
        )

    @apply_test_settings()
    def test___eq__(self) -> None:
        any_value: ap.AnyValue = ap.AnyValue(200)
        int_1: ap.Int = ap.Int(100)
        result: ap.Boolean = any_value == int_1
        self._assert_comparison_operation_result(
            any_value=any_value,
            result=result,
            other=int_1,
            expected_comparison_operator="===",
        )

    @apply_test_settings()
    def test___ne__(self) -> None:
        any_value: ap.AnyValue = ap.AnyValue(200)
        int_1: ap.Int = ap.Int(100)
        result: ap.Boolean = any_value != int_1
        self._assert_comparison_operation_result(
            any_value=any_value,
            result=result,
            other=int_1,
            expected_comparison_operator="!==",
        )

    @apply_test_settings()
    def test___lt__(self) -> None:
        any_value: ap.AnyValue = ap.AnyValue(200)
        int_1: ap.Int = ap.Int(100)
        result: ap.Boolean = any_value < int_1
        self._assert_comparison_operation_result(
            any_value=any_value,
            result=result,
            other=int_1,
            expected_comparison_operator="<",
        )

    @apply_test_settings()
    def test___le__(self) -> None:
        any_value: ap.AnyValue = ap.AnyValue(200)
        int_1: ap.Int = ap.Int(100)
        result: ap.Boolean = any_value <= int_1
        self._assert_comparison_operation_result(
            any_value=any_value,
            result=result,
            other=int_1,
            expected_comparison_operator="<=",
        )

    @apply_test_settings()
    def test___gt__(self) -> None:
        any_value: ap.AnyValue = ap.AnyValue(200)
        int_1: ap.Int = ap.Int(100)
        result: ap.Boolean = any_value > int_1
        self._assert_comparison_operation_result(
            any_value=any_value,
            result=result,
            other=int_1,
            expected_comparison_operator=">",
        )

    @apply_test_settings()
    def test___ge__(self) -> None:
        any_value: ap.AnyValue = ap.AnyValue(200)
        int_1: ap.Int = ap.Int(100)
        result: ap.Boolean = any_value >= int_1
        self._assert_comparison_operation_result(
            any_value=any_value,
            result=result,
            other=int_1,
            expected_comparison_operator=">=",
        )

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        any_value: ap.AnyValue = ap.AnyValue(200)
        snapshot_name: str = any_value._get_next_snapshot_name()
        any_value._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert any_value._any_value_snapshots == {snapshot_name: 200}

        any_value.value = 300
        any_value._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert any_value._any_value_snapshots == {snapshot_name: 200}

    @apply_test_settings()
    def test__revert(self) -> None:
        any_value: ap.AnyValue = ap.AnyValue(200)
        snapshot_name: str = any_value._get_next_snapshot_name()
        any_value._run_all_revert_methods(snapshot_name=snapshot_name)

        any_value._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        any_value.value = 300
        any_value._run_all_revert_methods(snapshot_name=snapshot_name)
        assert any_value.value == 200
