"""Each js assertion (console.assert) interface implementations.
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
