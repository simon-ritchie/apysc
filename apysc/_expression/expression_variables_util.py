"""Implementations to manipulate expression variable name
related interface.

Mainly following interfaces are defined:

- get_next_variable_name: Get next variable name of specified type name.
- append_substitution_expression: Append substitution expression between
    two variables.
"""

from typing import Optional
from typing import Tuple

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
    _save_next_variable_name_count(type_name=type_name)
    return variable_name


def _save_next_variable_name_count(type_name: str) -> None:
    """
    Save a next variable name count value.

    Parameters
    ----------
    type_name : str
        Any type name, e.g., `sp`.
    """
    from apysc._expression import expression_data_util
    expression_data_util.initialize_sqlite_tables_if_not_initialized()
    next_variable_num: int = _get_next_variable_num(
        type_name=type_name)
    table_name: str = expression_data_util.TableName.VARIABLE_NAME_COUNT.value
    query: str = (
        f'DELETE FROM {table_name} '
        f"WHERE type_name = '{type_name}' LIMIT 1;"
    )
    expression_data_util.cursor.execute(query)
    query = (
        f'INSERT INTO {table_name}'
        '(type_name, count) '
        f"VALUES('{type_name}', {next_variable_num});"
    )
    expression_data_util.cursor.execute(query)
    expression_data_util.connection.commit()


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
    from apysc._expression import expression_data_util
    expression_data_util.initialize_sqlite_tables_if_not_initialized()
    table_name: str = expression_data_util.TableName.VARIABLE_NAME_COUNT.value
    query: str = (
        f'SELECT count FROM {table_name} '
        f"WHERE type_name = '{type_name}' LIMIT 1;"
    )
    expression_data_util.cursor.execute(query)
    result: Optional[Tuple[int]] = expression_data_util.cursor.fetchone()
    expression_data_util.connection.commit()
    if result is None:
        return 1
    next_variable_num: int = result[0] + 1
    return next_variable_num


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
    import apysc as ap
    expression: str = (
        f'{left_value.variable_name} = {right_value.variable_name};'
    )
    ap.append_js_expression(expression=expression)


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
    import apysc as ap
    if left_variable_name == '' or right_variable_name == '':
        return
    expression: str = (
        f'{left_variable_name} = {right_variable_name};'
    )
    ap.append_js_expression(expression=expression)
