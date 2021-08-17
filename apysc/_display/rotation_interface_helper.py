"""Helper module for the rotation interfaces.
"""

from typing import Union

import apysc as ap
from apysc._type.expression_string import ExpressionString


def get_coordinates_key_for_expression(
        x: Union[int, ap.Int],
        y: Union[int, ap.Int]) -> ExpressionString:
    """
    Get a key string for the expression from the x and y coordinates.

    Parameters
    ----------
    x : int or Int
        X-coordinate.
    y : int or Int
        Y-coordinate.

    Returns
    -------
    key_exp_str : ExpressionString
        Key expression string.
    """
    from apysc._type.variable_name_interface import VariableNameInterface
    if isinstance(x, VariableNameInterface):
        x_str: str = x.variable_name
    else:
        x_str = str(x)
    if isinstance(y, VariableNameInterface):
        y_str: str = y.variable_name
    else:
        y_str = str(y)
    key_exp_str: ExpressionString = ExpressionString(
        value=f'String({x_str}) + "_" + String({y_str})')
    return key_exp_str
