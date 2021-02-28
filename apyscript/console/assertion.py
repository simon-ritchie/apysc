"""Each js assertion (console.assert) interface implementations.
"""

from typing import Any

from apyscript.expression import expression_file_util
from apyscript.console.trace import trace
from apyscript.type import value_util
from apyscript.string import string_util


def assert_equal(expected: Any, actual: Any, msg: str = '') -> None:
    """
    Assertion interface for equal condition.

    Parameters
    ----------
    expected : *
        Expected value.
    actual : *
        Actual value.
    msg : str
        Message to display when assertion failed.
    """
    _trace_info(
        interface_label='assert_equal', expected=expected, actual=actual)

    expected_str: str = value_util.get_value_str_for_expression(
        value=expected)
    actual_str: str = value_util.get_value_str_for_expression(value=actual)

    msg = string_util.escape_str(string=msg)
    expression: str = (
        f'console.assert({expected_str} === {actual_str}, "{msg}");'
    )
    expression_file_util.wrap_by_script_tag_and_append_expression(
        expression=expression)


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
