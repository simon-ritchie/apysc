"""This module is the helper module for the rotation interfaces.
"""

from typing import Union

from apysc._type.expression_string import ExpressionString
from apysc._type.int import Int


def get_coordinates_key_for_expression(
    *, x: Union[int, Int], y: Union[int, Int]
) -> ExpressionString:
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
    from apysc._type.variable_name_mixin import VariableNameMixIn

    if isinstance(x, VariableNameMixIn):
        x_str: str = x.variable_name
    else:
        x_str = str(x)
    if isinstance(y, VariableNameMixIn):
        y_str: str = y.variable_name
    else:
        y_str = str(y)
    key_exp_str: ExpressionString = ExpressionString(
        value=f'String({x_str}) + "_" + String({y_str})'
    )
    return key_exp_str
