"""Helper interfaces for the scale interfaces.
"""

from typing import Union

import apysc as ap
from apysc._type.expression_string import ExpressionString


def get_coordinate_key_for_expression(
        coordinate: Union[int, ap.Int]) -> ExpressionString:
    """
    Get a key string for the expression from the x or y coordinate.

    Parameters
    ----------
    coordinate : int or Int
        X or y coordinate.

    Returns
    -------
    key_exp_str : ExpressionString
        Key expression string.
    """
    from apysc._type.variable_name_interface import VariableNameInterface
    if isinstance(coordinate, VariableNameInterface):
        coordinate_str: str = coordinate.variable_name
    else:
        coordinate_str = str(coordinate)
    key_exp_str: ExpressionString = ExpressionString(
        value=f'String({coordinate_str})')
    return key_exp_str
