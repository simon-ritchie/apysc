"""Implementations to manipulate expression variable name
related interface.

Mainly following interfaces are defined:

- get_next_variable_name: Get next variable name of specified type name.
- get_variable_names_file_path: Get a file path of saving variable names.
- append_substitution_expression: Append substitution expression between
    two variables.
"""

import os
from typing import List

from apysc._type.variable_name_interface import VariableNameInterface


def get_next_variable_name(type_name: str) -> str:
    """
    Get next variable name of specified type name.

    Notes
    -----
    If call this function multiple times, then returned number will be
    increased.

    Parameters
    ----------
    type_name : str
        Any type name, e.g., `sprite`.
        If `sprite` is specified and there is no `sprite` variable
        name in expression file, then `sprite_1` will be returned.
        If variable name of `sprite_1` is already used, then `sprite_2`
        will be returned.

    Returns
    -------
    variable_name : str
        Next variable name.
    """
    next_variable_num: int = _get_next_variable_num(
        type_name=type_name)
    variable_name = _make_variable_name(
        type_name=type_name, variable_num=next_variable_num)
    _save_next_variable_name_to_file(type_name=type_name)
    return variable_name


def _make_variable_name(type_name: str, variable_num: int) -> str:
    """
    Make variable name from type name and variable num.

    Parameters
    ----------
    type_name : str
        Any type name, e.g., `sprite`.
    variable_num : int
        Target variable number (start from 1).

    Returns
    -------
    variable_name : str
        Variable name that concatenated type name and variable number.
    """
    variable_name: str = f'{type_name}_{variable_num}'
    return variable_name


def _get_next_variable_num(type_name: str) -> int:
    """
    Get a next variable number.

    Parameters
    ----------
    type_name : str
        Any type name, e.g., `sprite`.

    Returns
    -------
    next_variable_num : int
        Next variable number (start from 1).
    """
    variable_names: List[str] = _read_variable_names(
        type_name=type_name)
    if not variable_names:
        return 1
    last_num: int = int(variable_names[-1].split('_')[-1])
    return last_num + 1


def _read_variable_names(type_name: str) -> List[str]:
    """
    Read variable names from file.

    Parameters
    ----------
    type_name : str
        Any type name, e.g., `sprite`.

    Returns
    -------
    variable_names : list of str
        Target type name's variable names.
        e.g., if type name is sprite, `['sprite_1', 'sprite_2', ...]`.
    """
    from apysc._file import file_util
    file_path: str = get_variable_names_file_path(
        type_name=type_name)
    if not os.path.isfile(file_path):
        return []
    variables_str: str = file_util.read_txt(file_path=file_path)
    variables_str = variables_str.strip(',')
    variable_names: List[str] = variables_str.split(',')
    return variable_names


def _save_next_variable_name_to_file(type_name: str) -> None:
    """
    Save next variable's name to file.

    Parameters
    ----------
    type_name : str
        Any type name, e.g., `sprite`.
    """
    from apysc._file import file_util
    file_path: str = get_variable_names_file_path(
        type_name=type_name)
    next_variable_num: int = _get_next_variable_num(
        type_name=type_name)
    variable_name: str = _make_variable_name(
        type_name=type_name, variable_num=next_variable_num)
    file_util.append_plain_txt(
        txt=f'{variable_name},', file_path=file_path)


def get_variable_names_file_path(type_name: str) -> str:
    """
    Get a file path of saving variable names.

    Parameters
    ----------
    type_name : str
        Any type name, e.g., `sprite`.

    Returns
    -------
    file_path : str
        Specified type name's target file path.
    """
    from apysc._expression import expression_file_util
    file_path: str = os.path.join(
        expression_file_util.EXPRESSION_ROOT_DIR,
        f'variables_{type_name}.txt',
    )
    return file_path


def append_substitution_expression(
        left_value: VariableNameInterface,
        right_value: VariableNameInterface) -> None:
    """
    Append a substitution expression between two variables.

    Parameters
    ----------
    left_value : VariableNameInterface
        Any left value.
    right_value : VariableNameInterface
        Any right value.
    """
    from apysc import append_js_expression
    expression: str = (
        f'{left_value.variable_name} = {right_value.variable_name};'
    )
    append_js_expression(expression=expression)


def append_substitution_expression_with_names(
        left_variable_name: str,
        right_variable_name: str) -> None:
    """
    Append a substitution expression between two variable names.

    Notes
    -----
    If the left or the right variable names are blank, then
    expression appending will be skipped.

    Parameters
    ----------
    left_variable_name : str
        Left-side variable name.
    right_variable_name : str
        Right-side variable name.
    """
    from apysc import append_js_expression
    if left_variable_name == '' or right_variable_name == '':
        return
    expression: str = (
        f'{left_variable_name} = {right_variable_name};'
    )
    append_js_expression(expression=expression)
