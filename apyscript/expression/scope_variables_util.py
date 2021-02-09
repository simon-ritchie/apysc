"""Implementations to manipulate each scopes variable name
related interface.
"""

import os
from typing import List

from apyscript.expression import expression_file_util, expression_scope
from apyscript.file import file_util


def get_current_scope_next_variable_name(type_name: str) -> str:
    """
    Get current scope's next variable name of specified type name.

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
        Current scope's next variable name.
    """
    pass


def _read_current_scope_variable_names(type_name: str) -> List[str]:
    """
    Read current scope's variable names from file.

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
    file_path: str = get_current_scope_variable_names_file_path(
        type_name=type_name)
    if not os.path.isfile(file_path):
        return []
    variables_str: str = file_util.read_txt(file_path=file_path)
    variables_str = variables_str.strip(',')
    variable_names: List[str] = variables_str.split(',')
    return variable_names


def _save_next_variable_name_to_current_scope_file(type_name: str) -> None:
    pass


def get_current_scope_variable_names_file_path(type_name: str) -> str:
    """
    Get current scope's file path of saving variable names.

    Parameters
    ----------
    type_name : str
        Any type name, e.g., `sprite`.

    Returns
    -------
    file_path : str
        Specified type name's target file path.
    """
    current_scope: str = expression_scope.get_current_scope()
    file_path: str = os.path.join(
        expression_file_util.EXPRESSION_ROOT_DIR,
        f'scope_variables_{current_scope}_{type_name}.txt',
    )
    return file_path
