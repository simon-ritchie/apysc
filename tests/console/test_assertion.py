from random import randint

from retrying import retry

from apyscript.console import assertion
from apyscript.expression import expression_file_util
from apyscript.type.int import Int


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
