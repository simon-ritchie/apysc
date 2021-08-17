"""Helper module for the scale interfaces.
"""

from enum import Enum
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


class CoordinateType(Enum):
    X = 1
    Y = 2


def get_scale_updating_expression(
        coordinate: ap.Int,
        scale_dict: ap.Dictionary[str, ap.Number],
        interface_variable_name: str,
        coordinate_type: CoordinateType) -> str:
    """
    Get a scale updating expression string from a specified coordinate.

    Parameters
    ----------
    coordinate : Int
        X or y coordinate.
    scale_dict : Dictionary
        Scale value dictionary.
    interface_variable_name : str
        Scale interface instance variable name.
    coordinate_type : CoordinateType
        Coordinate type to identify the x or y target.

    Returns
    -------
    expression : str
        A scale updating expression string.
    """
    from apysc._display import scale_interface_helper
    from apysc._expression import expression_variables_util
    from apysc._expression import var_names
    from apysc._type import value_util
    before_value_name: str = expression_variables_util.\
        get_next_variable_name(type_name=var_names.NUMBER)
    key_exp_str_1: ExpressionString = scale_interface_helper.\
        get_coordinate_key_for_expression(coordinate=coordinate)
    key_exp_str_2: ExpressionString = scale_interface_helper.\
        get_coordinate_key_for_expression(coordinate=int(coordinate._value))
    after_value_str: str = value_util.get_value_str_for_expression(
        value=scale_dict._value[key_exp_str_2.value])
    coordinate_value_str: str = value_util.get_value_str_for_expression(
        value=coordinate)
    scale_from_point_value_str: str = value_util.\
        get_value_str_for_expression(value=scale_dict)
    if coordinate_type == CoordinateType.X:
        coordinate_exp: str = f'{coordinate_value_str}, 0'
        scale_resetting_exp: str = f'1 / {before_value_name}, 1'
        scale_result_exp: str = f'{after_value_str}, 1'
    else:
        coordinate_exp = f'0, {coordinate_value_str}'
        scale_resetting_exp = f'1, 1 / {before_value_name}'
        scale_result_exp = f'1, {after_value_str}'
    expression: str = (
        f'if ({key_exp_str_1.value} in '
        f'{scale_from_point_value_str}) {{'
        f'\n  var {before_value_name} = '
        f'{scale_from_point_value_str}[{key_exp_str_1.value}];'
        '\n}else {'
        f'\n  {before_value_name} = 1.0;'
        '\n}'
        f'\n{interface_variable_name}.scale('
        f'{scale_resetting_exp}, {coordinate_exp});'
        f'\n{interface_variable_name}.scale('
        f'{scale_result_exp}, {coordinate_exp});'
        f'\n{scale_from_point_value_str}[{key_exp_str_1.value}] = '
        f'{after_value_str};'
    )
    return expression
