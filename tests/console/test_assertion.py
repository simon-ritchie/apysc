from random import randint

from retrying import retry

from apyscript.console import assertion
from apyscript.expression import expression_file_util
from apyscript.type import Int, Boolean


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test_assert_equal() -> None:
    expression_file_util.remove_expression_file()
    int_1: Int = Int(10)
    int_2: Int = Int(20)
    assertion.assert_equal(
        expected=int_1, actual=int_2,
        msg='Invalid int values.')

    expression: str = expression_file_util.get_current_expression()
    expected: str = (
        f'console.assert({int_1.variable_name} === {int_2.variable_name}, '
        '"Invalid int values.");'
    )
    assert expected in expression


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test__trace_info() -> None:
    expression_file_util.remove_expression_file()
    int_1: Int = Int(10)
    int_2: Int = Int(20)
    assertion.assert_equal(
        expected=int_1, actual=int_2,
        msg='Invalid int values.')
    expression: str = expression_file_util.get_current_expression()
    expected: str = (
        f'Expected variable name: {int_1.variable_name}'
    )
    assert expected in expression
    expected = (
        f'Actual variable name: {int_2.variable_name}'
    )
    assert expected in expression


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test_assert_not_equal() -> None:
    expression_file_util.remove_expression_file()
    int_1: Int = Int(10)
    assertion.assert_not_equal(
        expected=11, actual=int_1,
        msg='Invalid condition.')
    expression: str = expression_file_util.get_current_expression()
    expected: str = (
        f'console.assert(11 !== {int_1.variable_name}, "Invalid condition.");'
    )
    assert expected in expression


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test__get_expected_and_actual_strs() -> None:
    int_1: Int = Int(10)
    int_2: Int = Int(20)
    expected_str, actual_str = assertion._get_expected_and_actual_strs(
        expected=int_1, actual=int_2)
    assert expected_str == int_1.variable_name
    assert actual_str == int_2.variable_name

    expected_str, actual_str = assertion._get_expected_and_actual_strs(
        expected='Hello', actual='World!')
    assert expected_str == '"Hello"'
    assert actual_str == '"World!"'


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test_assert_true() -> None:
    expression_file_util.remove_expression_file()
    boolean_1: Boolean = Boolean(True)
    assertion.assert_true(
        actual=boolean_1,
        type_strict=True,
        msg='Value is not true.')
    expression: str = expression_file_util.get_current_expression()
    expected: str = (
        f'console.assert({boolean_1.variable_name} === true, '
        '"Value is not true.");'
    )
    assert expected in expression

    assertion.assert_true(actual=boolean_1, type_strict=False)
    expression = expression_file_util.get_current_expression()
    expected = (
        f'console.assert({boolean_1.variable_name} == true, "");'
    )
    assert expected in expression
