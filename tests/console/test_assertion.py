from random import randint

from retrying import retry

from apysc.console import assertion
from apysc.expression import expression_file_util
from apysc.type import Array
from apysc.type import Boolean
from apysc.type import Int


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
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

    expression_file_util.remove_expression_file()
    assertion.assert_equal(expected=[1, 2, 3], actual=Array([1, 2, 3]))
    expression = expression_file_util.get_current_expression()
    assert 'assert_arrays_equal' in expression
    assert 'assert_equal' not in expression


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
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


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
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

    expression_file_util.remove_expression_file()
    assertion.assert_not_equal(expected=[1, 2], actual=Array([1, 2, 3]))
    expression = expression_file_util.get_current_expression()
    assert 'assert_arrays_not_equal' in expression
    assert 'assert_not_equal' not in expression


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
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


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
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


def test__add_equal_if_type_strict_setting_is_true() -> None:
    expression: str = assertion._add_equal_if_type_strict_setting_is_true(
        expression='a ==', type_strict=True)
    assert expression == 'a ==='

    expression = assertion._add_equal_if_type_strict_setting_is_true(
        expression='a ==', type_strict=False)
    assert expression == 'a =='


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_assert_false() -> None:
    expression_file_util.remove_expression_file()
    boolean_1: Boolean = Boolean(False)
    assertion.assert_false(boolean_1, msg='Value is not false.')
    expression: str = expression_file_util.get_current_expression()
    expected: str = (
        f'console.assert({boolean_1.variable_name} === false, '
        '"Value is not false.");'
    )
    assert expected in expression


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test__actual_value_type_is_array() -> None:
    result: bool = assertion._actual_value_type_is_array(actual=100)
    assert not result

    result = assertion._actual_value_type_is_array(Array([100, 200]))
    assert result


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_assert_arrays_equal() -> None:
    expression_file_util.remove_expression_file()
    array_1: Array = Array([1, 2, 3])
    assertion.assert_arrays_equal(
        expected=[1, 2, 3], actual=array_1,
        msg='Array values are not equal.')
    expression: str = expression_file_util.get_current_expression()
    expected: str = (
        f'console.assert(_.isEqual([1, 2, 3], {array_1.variable_name}), '
        f'"Array values are not equal.");'
    )
    assert expected in expression


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test__trace_arrays_assertion_info() -> None:
    expression_file_util.remove_expression_file()
    array_1: Array = Array([1, 2, 3])
    assertion._trace_arrays_assertion_info(
        interface_label='assert_arrays_equal',
        expected=[1, 2, 3], actual=array_1)
    expression: str = expression_file_util.get_current_expression()
    assert '[assert_arrays_equal]' in expression
    assert '"\\nExpected:", "[1, 2, 3]"' in expression
    expected = f'"actual:", "{array_1.variable_name} ([1, 2, 3])"'
    assert expected in expression

    expression_file_util.remove_expression_file()
    assertion._trace_arrays_assertion_info(
        interface_label='assert_arrays_not_equal',
        expected=array_1, actual=[1, 2, 3])
    expression = expression_file_util.get_current_expression()
    expected = f'"\\nExpected:", "{array_1.variable_name} ([1, 2, 3])"'
    assert expected in expression
    assert '"actual:", "[1, 2, 3]"' in expression


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test__make_arrays_comparison_expression() -> None:
    expression_file_util.remove_expression_file()
    array_1: Array = Array([1, 2, 3])
    expression: str = assertion._make_arrays_comparison_expression(
        expected=[1, 2, 3],
        actual=array_1,
        msg='Array values is not equal.',
        not_condition=False)
    expected: str = (
        f'console.assert(_.isEqual([1, 2, 3], {array_1.variable_name}), '
        '"Array values is not equal.");'
    )
    assert expression == expected

    expression = assertion._make_arrays_comparison_expression(
        expected=[1, 2, 3],
        actual=[1],
        msg='',
        not_condition=True)
    expected = (
        'console.assert(!_.isEqual([1, 2, 3], [1]), "");')
    assert expression == expected


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_assert_arrays_not_equal() -> None:
    expression_file_util.remove_expression_file()
    array_1: Array = Array([1, 2, 3])
    assertion.assert_arrays_not_equal(
        expected=[1, 2], actual=array_1,
        msg='Array values are equal.')
    expression: str = expression_file_util.get_current_expression()
    expected: str = (
        f'console.assert(!_.isEqual([1, 2], {array_1.variable_name}), '
        f'"Array values are equal.");'
    )
    assert expected in expression


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_assert_defined() -> None:
    expression_file_util.remove_expression_file()
    int_1: Int = Int(3)
    assertion.assert_defined(actual=int_1, msg='value is undefined.')
    expression: str = expression_file_util.get_current_expression()
    expected: str = (
        f'console.assert(!_.isUndefined({int_1.variable_name}), '
        '"value is undefined.");'
    )
    assert expected in expression


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_assert_undefined() -> None:
    expression_file_util.remove_expression_file()
    int_1: Int = Int(3)
    assertion.assert_undefined(actual=int_1, msg='value is not undefined.')
    expression: str = expression_file_util.get_current_expression()
    expected: str = (
        f'console.assert(_.isUndefined({int_1.variable_name}), '
        '"value is not undefined.");'
    )
    assert expected in expression
