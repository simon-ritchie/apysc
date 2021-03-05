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
"""

from typing import Any
from typing import Tuple

from apyscript.console.trace import trace
from apyscript.expression import expression_file_util
from apyscript.string import string_util
from apyscript.type import value_util


def assert_equal(expected: Any, actual: Any, msg: str = '') -> None:
    """
    JavaScript assertion interface for equal condition.

    Parameters
    ----------
    expected : *
        Expected value.
    actual : *
        Actual value.
    msg : str, optional
        Message to display when assertion failed.
    """
    _trace_info(
        interface_label='assert_equal', expected=expected, actual=actual)

    expected_str, actual_str = _get_expected_and_actual_strs(
        expected=expected, actual=actual)

    msg = string_util.escape_str(string=msg)
    expression: str = (
        f'console.assert({expected_str} === {actual_str}, "{msg}");'
    )
    expression_file_util.wrap_by_script_tag_and_append_expression(
        expression=expression)


def assert_not_equal(expected: Any, actual: Any, msg: str = '') -> None:
    """
    JavaScript assertion interface for not equal condition.

    Parameters
    ----------
    expected : *
        Expected value.
    actual : *
        Actual value.
    msg : str, optional
        Message to display when assertion failed.
    """
    _trace_info(
        interface_label='assert_not_equal', expected=expected, actual=actual)
    expected_str, actual_str = _get_expected_and_actual_strs(
        expected=expected, actual=actual)

    msg = string_util.escape_str(string=msg)
    expression: str = (
        f'console.assert({expected_str} !== {actual_str}, "{msg}");'
    )
    expression_file_util.wrap_by_script_tag_and_append_expression(
        expression=expression)


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
    expression_file_util.wrap_by_script_tag_and_append_expression(
        expression=expression)


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
    expression_file_util.wrap_by_script_tag_and_append_expression(
        expression=expression)


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
    expected = string_util.wrap_by_double_quotation_if_value_is_string(
        value=expected)
    actual = string_util.wrap_by_double_quotation_if_value_is_string(
        value=actual)
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
    from apyscript.type.variable_name_interface import VariableNameInterface
    info: str = f'[{interface_label}]'
    if isinstance(expected, VariableNameInterface):
        info += f'\nExpected variable name: {expected.variable_name}'
    if isinstance(actual, VariableNameInterface):
        info += f'\nActual variable name: {actual.variable_name}'
    trace(info, '\nExpected:', expected, 'actual:', actual)
