"""Each js assertion (console.assert) interface implementations.
"""

from typing import Any

from apyscript.expression import expression_file_util
from apyscript.console.trace import trace
from apyscript.type import value_util


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
    from apyscript.type.variable_name_interface import VariableNameInterface
    info: str = ''
    if isinstance(expected, VariableNameInterface):
        info += f'Expected variable name: {expected.variable_name}'
    if isinstance(actual, VariableNameInterface):
        if info != '':
            info += '\n'
        info += f'Actual variable name: {actual.variable_name}'
    trace(info, '\nExpected:', expected, 'actual:', actual)

    expected_str: str = value_util.get_value_str_for_expression(
        value=expected)
    actual_str: str = value_util.get_value_str_for_expression(value=actual)

    msg = repr(msg)[1:-1]
    expression: str = (
        f'console.assert({expected_str} === {actual_str}, "{msg}");'
    )
    expression_file_util.wrap_by_script_tag_and_append_expression(
        expression=expression)
