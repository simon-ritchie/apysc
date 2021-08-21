"""The helper module for the flip interfaces.
"""

from enum import Enum

import apysc as ap


class Axis(Enum):
    X = 'x'
    Y = 'y'


def make_flip_update_expression(
        before_value: ap.Boolean, after_value: ap.Boolean,
        axis: Axis, interface_variable_name: str) -> str:
    """
    Make a flipping value updating expression.

    Parameters
    ----------
    before_value : Boolean
        Before updating flipping value.
    after_value : Boolean
        After updating flipping value.
    axis : Axis
        X or y axis value.
    interface_variable_name : str
        Interface instance variable name.

    Returns
    -------
    expression : str
        Made expression string.
    """
    from apysc._type import value_util
    before_value_str: str = value_util.get_value_str_for_expression(
        value=before_value)
    after_value_str: str = value_util.get_value_str_for_expression(
        value=after_value)
    expression: str = (
        f'if ({before_value_str}) {{'
        f'\n  {interface_variable_name}.flip("{axis.value}");'
        '\n}'
        f'\nif ({after_value_str}) {{'
        f'\n  {interface_variable_name}.flip("{axis.value}");'
        '\n}'
        f'\n{before_value_str} = {after_value_str};'
    )
    return expression
