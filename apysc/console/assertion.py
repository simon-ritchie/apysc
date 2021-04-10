"""Each js assertion (console.assert) interface implementations.

Mainly following interfaces are defined:

- assert_equal
    JavaScript assertion interface for equal condition.
- assert_not_equal
    JavaScript assertion interface for not equal condition.
- assert_true
    JavaScript assertion interface for true condition.
- assert_false
    JavaScript assertion interface for false condition.
- assert_arrays_equal
    JavaScript assertion interface for Array values equal condition.
- assert_arrays_not_equal
    JavaScript assertion interface for Array values not equal condition.
- assert_defined
    JavaScript assertion interface for defined (not undefined)
    value condition.
- assert_undefined
    JavaScript assertion interface for undefined value condition.
"""

from typing import Any
from typing import Tuple


def assert_equal(expected: Any, actual: Any, msg: str = '') -> None:
    """
    JavaScript assertion interface for equal condition.

    Notes
    -----
    - If specified actual value is type of Array (or list, etc),
        then assert_arrays_equal function will be called instead of
        this function.

    Parameters
    ----------
    expected : *
        Expected value.
    actual : *
        Actual value.
    msg : str, optional
        Message to display when assertion failed.
    """
    from apysc.expression import expression_file_util
    from apysc.string import string_util
    if _actual_value_type_is_array(actual=actual):
        assert_arrays_equal(expected=expected, actual=actual, msg=msg)
        return

    _trace_info(
        interface_label='assert_equal', expected=expected, actual=actual)

    expected_str, actual_str = _get_expected_and_actual_strs(
        expected=expected, actual=actual)

    msg = string_util.escape_str(string=msg)
    expression: str = (
        f'console.assert({expected_str} === {actual_str}, "{msg}");'
    )
    expression_file_util.append_js_expression(expression=expression)


def assert_not_equal(expected: Any, actual: Any, msg: str = '') -> None:
    """
    JavaScript assertion interface for not equal condition.

    Notes
    -----
    - If specified actual value is type of Array (or list, etc),
        then assert_not_arrays_equal function will be called instead
        of this function.

    Parameters
    ----------
    expected : *
        Expected value.
    actual : *
        Actual value.
    msg : str, optional
        Message to display when assertion failed.
    """
    from apysc.expression import expression_file_util
    from apysc.string import string_util
    if _actual_value_type_is_array(actual=actual):
        assert_arrays_not_equal(expected=expected, actual=actual, msg=msg)
        return

    _trace_info(
        interface_label='assert_not_equal', expected=expected, actual=actual)
    expected_str, actual_str = _get_expected_and_actual_strs(
        expected=expected, actual=actual)

    msg = string_util.escape_str(string=msg)
    expression: str = (
        f'console.assert({expected_str} !== {actual_str}, "{msg}");'
    )
    expression_file_util.append_js_expression(expression=expression)


def assert_true(
        actual: Any, type_strict: bool = True, msg: str = '') -> None:
    """
    JavaScript assertion interface for true condition.

    Parameters
    ----------
    actual : *
        Actual value.
    type_strict : bool, default True
        Whether strictly check actual value or not.
        For example, if type_strict is True, interger 1 will
        fail, on the contrary (if type_strict is False), integer 1
        will pass test.
    msg : str, optional
        Message to display when assertion failed.
    """
    from apysc.expression import expression_file_util
    from apysc.string import string_util
    _trace_info(
        interface_label='assert_true', expected='true', actual=actual)
    _, actual_str = _get_expected_and_actual_strs(
        expected='true', actual=actual)

    msg = string_util.escape_str(string=msg)
    expression: str = (
        f'console.assert({actual_str} =='
    )
    expression = _add_equal_if_type_strict_setting_is_true(
        expression=expression, type_strict=type_strict)
    expression += f' true, "{msg}");'
    expression_file_util.append_js_expression(expression=expression)


def assert_false(
        actual: Any, type_strict: bool = True, msg: str = '') -> None:
    """
    JavaScript assertion interface for false condition.

    Parameters
    ----------
    actual : *
        Actual value.
    type_strict : bool, default True
        Whether strictly check actual value or not.
        For example, if type_strict is True, interger 0 will
        fail, on the contrary (if type_strict is False), integer 0
        will pass test.
    msg : str, optional
        Message to display when assertion failed.
    """
    from apysc.expression import expression_file_util
    from apysc.string import string_util
    _trace_info(
        interface_label='assert_false', expected='false', actual=actual)
    _, actual_str = _get_expected_and_actual_strs(
        expected='false', actual=actual)

    msg = string_util.escape_str(string=msg)
    expression: str = (
        f'console.assert({actual_str} =='
    )
    expression = _add_equal_if_type_strict_setting_is_true(
        expression=expression, type_strict=type_strict)
    expression += f' false, "{msg}");'
    expression_file_util.append_js_expression(expression=expression)


def assert_arrays_equal(
        expected: Any, actual: Any, msg: str = '') -> None:
    """
    JavaScript assertion interface for Array values equal condition.

    Notes
    -----
    This is used instead of assert_equal for Array class
    comparison (JavaScript can not compare arrays directly, like
    a Python, for example, `[1, 2] === [1, 2]` will be false).

    Parameters
    ----------
    expected : *
        Expected value.
    actual : *
        Actual value.
    msg : str, optional
        Message to display when assertion failed.
    """
    from apysc.expression import expression_file_util
    _trace_arrays_assertion_info(
        interface_label='assert_arrays_equal',
        expected=expected, actual=actual)

    expression: str = _make_arrays_comparison_expression(
        expected=expected, actual=actual, msg=msg, not_condition=False)
    expression_file_util.append_js_expression(expression=expression)


def assert_arrays_not_equal(
        expected: Any, actual: Any, msg: str = '') -> None:
    """
    JavaScript assertion interface for Array values not equal condition.

    Notes
    -----
    This is used instead of assert_not_equal for Array class
    comparison (JavaScript can not compare arrays directly, like
    a Python, for example, `[1, 2] === [1, 2]` will be false).

    Parameters
    ----------
    expected : *
        Expected value.
    actual : *
        Actual value.
    msg : str, optional
        Message to display when assertion failed.
    """
    from apysc.expression import expression_file_util
    _trace_arrays_assertion_info(
        interface_label='assert_arrays_not_equal',
        expected=expected, actual=actual)

    expression: str = _make_arrays_comparison_expression(
        expected=expected, actual=actual, msg=msg, not_condition=True)
    expression_file_util.append_js_expression(expression=expression)


def assert_defined(actual: Any, msg: str = '') -> None:
    """
    JavaScript assertion interface for defined (not undefined)
    value condition.

    Parameters
    ----------
    actual : *
        Actual value.
    msg : str, optional
        Message to display when assertion failed.
    """
    from apysc.expression import expression_file_util
    from apysc.string import string_util
    _trace_info(
        interface_label='assert_defined', expected='other than undefined',
        actual=actual)
    _, actual_str = _get_expected_and_actual_strs(
        expected='other than undefined', actual=actual)

    msg = string_util.escape_str(string=msg)
    expression: str = (
        f'console.assert(!_.isUndefined({actual_str}), "{msg}");'
    )
    expression_file_util.append_js_expression(expression=expression)


def assert_undefined(actual: Any, msg: str = '') -> None:
    """
    JavaScript assertion interface for undefined value condition.

    Parameters
    ----------
    actual : *
        Actual value.
    msg : str, optional
        Message to display when assertion failed.
    """
    from apysc.expression import expression_file_util
    from apysc.string import string_util
    _trace_info(
        interface_label='assert_undefined', expected='undefined',
        actual=actual)
    _, actual_str = _get_expected_and_actual_strs(
        expected='undefined', actual=actual)

    msg = string_util.escape_str(string=msg)
    expression: str = (
        f'console.assert(_.isUndefined({actual_str}), "{msg}");'
    )
    expression_file_util.append_js_expression(expression=expression)


def _make_arrays_comparison_expression(
        expected: Any, actual: Any, msg: str,
        not_condition: bool) -> str:
    """
    Make arrays comparison (assert_arrays_equal or
    assert_arrays_not_equal) expression string.

    Parameters
    ----------
    expected : *
        Expected value.
    actual : *
        Actual value.
    msg : str, optional
        Message to display when assertion failed.
    not_condition : bool
        Boolean value whether this expression is not condition
        (assert_arrays_not_equal) or not.

    Returns
    -------
    expression : str
        Result expression string.
    """
    from apysc.string import string_util
    from apysc.type import value_util
    expected_exp_str: str = value_util.get_value_str_for_expression(
        value=expected)
    actual_exp_str: str = value_util.get_value_str_for_expression(
        value=actual)
    msg = string_util.escape_str(string=msg)
    if not_condition:
        not_condition_str: str = '!'
    else:
        not_condition_str = ''
    expression: str = (
        f'console.assert({not_condition_str}_.isEqual({expected_exp_str}, '
        f'{actual_exp_str}), "{msg}");'
    )
    return expression


def _trace_arrays_assertion_info(
        interface_label: str, expected: Any, actual: Any) -> None:
    """
    Append arrays values information trace expression.

    Parameters
    ----------
    interface_label : str
        Target assertion interface label, e.g., 'assert_arrays_equal'.
    expected : *
        Expected value.
    actual : *
        Actual value.
    """
    from apysc import Array
    from apysc.type import value_util
    expected_exp_str: str = value_util.get_value_str_for_expression(
        value=expected)
    actual_exp_str: str = value_util.get_value_str_for_expression(
        value=actual)
    if isinstance(expected, Array):
        expected_info_str: str = f'{expected_exp_str} ({expected.value})'
    else:
        expected_info_str = expected_exp_str
    actual_info_str = actual_exp_str
    _trace_info(
        interface_label=interface_label,
        expected=expected_info_str,
        actual=actual_info_str)


def _actual_value_type_is_array(actual: Any) -> bool:
    """
    Get a boolean value whether specified actual value is
    Array type or not.

    Parameters
    ----------
    actual : *
        Actual value.

    Returns
    -------
    result : bool
        If actual value type is Array, True will be returned.
    """
    from apysc import Array
    if isinstance(actual, Array):
        return True
    return False


def _add_equal_if_type_strict_setting_is_true(
        expression: str, type_strict: bool) -> str:
    """
    Add single equal character to expression if type_string setting
    is True.

    Parameters
    ----------
    expression : str
        Expression to be added.
    type_strict: bool
        Type strict setting value.

    Returns
    -------
    expression : str
        If type_string setting is true, then single equal character
        will be added to tail.
    """
    if not type_strict:
        return expression
    expression += '='
    return expression


def _get_expected_and_actual_strs(
        expected: Any, actual: Any) -> Tuple[str, str]:
    """
    Get expected and actual value strings from specified values.

    Parameters
    ----------
    expected : *
        Expected value.
    actual : *
        Actual value.

    Returns
    -------
    expected_str : str
        Expected value's string. If value is string, this will be
        wrapped by double quotation.
    actual_str : str
        Actual value's string. If value is string, this will be
        wrapped by double quotation.
    """
    from apysc.type import value_util
    expected_str: str = value_util.get_value_str_for_expression(
        value=expected)
    actual_str: str = value_util.get_value_str_for_expression(value=actual)
    return expected_str, actual_str


def _trace_info(interface_label: str, expected: Any, actual: Any) -> None:
    """
    Append trace expression of specified values.

    Parameters
    ----------
    interface_label : str
        Target assertion interface label, e.g., 'assert_equal'.
    expected : *
        Expected value.
    actual : *
        Actual value.
    """
    from apysc import trace
    from apysc.type.variable_name_interface import VariableNameInterface
    info: str = f'[{interface_label}]'
    if isinstance(expected, VariableNameInterface):
        info += f'\nExpected variable name: {expected.variable_name}'
    if isinstance(actual, VariableNameInterface):
        info += f'\nActual variable name: {actual.variable_name}'
    trace(info, '\nExpected:', expected, 'actual:', actual)
