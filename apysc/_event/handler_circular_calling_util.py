"""Handler circular calling related utilities.
"""

from typing import List
from typing import Optional
from typing import Tuple


def is_handler_circular_calling(handler_name: str) -> bool:
    """
    Get a boolean value whether a specified handler is
    a circular call or not.

    Parameters
    ----------
    handler_name : str
        Targer handler name.

    Returns
    -------
    result : bool
        If a specified handler is a circular call, True will be returned.
    """
    from apysc._expression import event_handler_scope
    if _is_already_saved_circular_calling(handler_name=handler_name):
        return True
    original_handler_name: str = handler_name
    handler_name = event_handler_scope.remove_suffix_num_from_handler_name(
        handler_name=handler_name)
    handler_names: List[str] = _read_handler_names()
    handler_names = _append_handler_name_to_last_of_list(
        handler_name=handler_name, handler_names=handler_names)
    count: int = handler_names.count(handler_name)
    if count < 2:
        return False
    prev_handler_name: str = handler_names[-2]
    prev_handler_count: int = 0
    for i, handler_name_ in enumerate(handler_names):
        if i == 0:
            continue
        if handler_name_ != handler_name:
            continue
        prev_handler_name_: str = handler_names[i - 1]
        if prev_handler_name_ != prev_handler_name:
            continue
        prev_handler_count += 1
        if prev_handler_count == 2:
            break
    if prev_handler_count == 2:
        _save_circular_calling_handler_name(
            handler_name=original_handler_name)
        return True
    return False


def _is_already_saved_circular_calling(handler_name: str) -> bool:
    """
    Get a boolean indicating whether a specified handler name
    has been already saved as the circular calling handler or not.

    Parameters
    ----------
    handler_name : str
        Target handler's name.

    Returns
    -------
    result : bool
        If a specified handler name has already been saved as the
        circular calling handler then True will be returned
    """
    prev_handler_name: str = get_prev_handler_name(
        handler_name=handler_name)
    if prev_handler_name == '':
        return False
    return True


def get_prev_handler_name(handler_name: str) -> str:
    """
    Get a previous handler's name of a specified handler's
    one if it is a circular calling handler.

    Parameters
    ----------
    handler_name : str
        Target handler's name.

    Returns
    -------
    prev_handler_name : str
        A previous handler's name. If there is no previous one,
        then blank string will be returned.
    """
    from apysc._expression import expression_data_util
    table_name: str = expression_data_util.TableName.\
        CIRCULAR_CALLING_HANDLER_NAME.value
    query: str = (
        f'SELECT prev_handler_name FROM {table_name} '
        f"WHERE handler_name = '{handler_name}';"
    )
    expression_data_util.exec_query(sql=query)
    result: Optional[Tuple[str]] = expression_data_util.cursor.fetchone()
    if result is None:
        return ''
    return result[0]


def get_prev_variable_name(handler_name: str) -> str:
    """
    Get a previous handler binded instance's variable name if a
    specified handler is a circular calling handler.

    Parameters
    ----------
    handler_name : str
        Target handler's name.

    Returns
    -------
    prev_variable_name : str
        A previous handler binded instance's variable name.
        If there is no previous (same handler's name prefix) one
        then blank string will be returned.
    """
    from apysc._expression import expression_data_util
    table_name: str = expression_data_util.TableName.\
        CIRCULAR_CALLING_HANDLER_NAME.value
    query: str = (
        f'SELECT prev_variable_name FROM {table_name} '
        f"WHERE handler_name = '{handler_name}';"
    )
    expression_data_util.exec_query(sql=query)
    result: Optional[Tuple[str]] = expression_data_util.cursor.fetchone()
    if result is None:
        return ''
    return result[0]


def _save_circular_calling_handler_name(handler_name: str) -> None:
    """
    Save a circular calling handler name to the SQLite.

    Parameters
    ----------
    handler_name : str
        Target handler's name.
    """
    from apysc._expression import expression_data_util
    prev_hadler_name: str = _get_same_name_prev_hadler_name(
        handler_name=handler_name)
    prev_variable_name: str = _get_same_name_prev_variable_name(
        handler_name=handler_name)
    table_name: str = expression_data_util.TableName.\
        CIRCULAR_CALLING_HANDLER_NAME.value
    query: str = (
        f'INSERT INTO {table_name}'
        '(handler_name, prev_handler_name, prev_variable_name) '
        f"VALUES('{handler_name}', '{prev_hadler_name}', "
        f"'{prev_variable_name}');"
    )
    expression_data_util.exec_query(sql=query)


def _get_same_name_prev_hadler_name(handler_name: str) -> str:
    """
    Get a previous same name (but the suffix number is different)
    handler's name from the current stack.

    Parameters
    ----------
    handler_name : str
        Target handler's name.

    Returns
    -------
    same_name_prev_hadler_name : str
        A previous same name (but the suffix number is different)
        handler's name.
    """
    same_name_prev_hadler_name: str
    same_name_prev_hadler_name, _ = _get_same_name_prev_data(
        handler_name=handler_name)
    return same_name_prev_hadler_name


def _get_same_name_prev_variable_name(handler_name: str) -> str:
    """
    Get a previous same name (but the suffix number is different)
    handler binded variable name from the current stack.

    Parameters
    ----------
    handler_name : str
        Target handler's name.

    Returns
    -------
    prev_variable_name : str
        A previous handler binded instance's variable name.
    """
    prev_variable_name: str
    _, prev_variable_name = _get_same_name_prev_data(
        handler_name=handler_name)
    return prev_variable_name


def _get_same_name_prev_data(handler_name: str) -> Tuple[str, str]:
    """
    Get previous handler name and variable name values of the
    previous same name (but the suffix number is different) handler
    from the current stack.

    Parameters
    ----------
    handler_name : str
        Target handler's name.

    Returns
    -------
    prev_hadler_name : str
        A previous same name (but the suffix number is different)
        handler's name value.
    prev_variable_name : str
        A previous variable name value.

    Raises
    ------
    ValueError
        If there is no previous same name handler's name in the SQLite.
    """
    from apysc._expression import event_handler_scope
    from apysc._expression import expression_data_util
    table_name: str = expression_data_util.TableName.\
        HANDLER_CALLING_STACK.value
    query: str = (
        f'SELECT handler_name, variable_name FROM {table_name} '
        f'ORDER BY scope_count DESC'
    )
    expression_data_util.exec_query(sql=query)
    result: List[Tuple[str, str]] = expression_data_util.cursor.fetchall()
    for i, tpl in enumerate(result):
        handler_name_: str = tpl[0]
        if i == 0 and handler_name == handler_name_:
            continue
        no_suffix_handler_name: str = event_handler_scope.\
            remove_suffix_num_from_handler_name(handler_name=handler_name)
        no_suffix_handler_name_: str = event_handler_scope.\
            remove_suffix_num_from_handler_name(handler_name=handler_name_)
        if no_suffix_handler_name != no_suffix_handler_name_:
            continue
        prev_hadler_name: str = handler_name_
        prev_variable_name: str = tpl[1]
        return prev_hadler_name, prev_variable_name
    raise ValueError(
        'Previous same name handler does not exitst in the SQLite.'
        ' Please check the implementation of this function\'s calling.')


def _append_handler_name_to_last_of_list(
        handler_name: str, handler_names: List[str]) -> List[str]:
    """
    Append a specified handler's name to the last of the list
    if the last one is an other handler's name.

    This function is used to unify last value regardless of
    `HandlerScope` setting.

    Parameters
    ----------
    handler_name : str
        Targer handler name.
    handler_names : list of str
        List to be appended.

    Returns
    -------
    handler_names : list of str
        Result list value.
    """
    if not handler_names:
        return [handler_name]
    if handler_names[-1] == handler_name:
        return handler_names
    handler_names.append(handler_name)
    return handler_names


def _read_handler_names() -> List[str]:
    """
    Read the current handler names from the calling stack.

    Returns
    -------
    handler_names : list of str
        Target handler names.
    """
    from apysc._expression import event_handler_scope
    from apysc._expression import expression_data_util
    table_name: str = expression_data_util.TableName.\
        HANDLER_CALLING_STACK.value
    query: str = (
        f'SELECT handler_name FROM {table_name} '
        f'ORDER BY scope_count'
    )
    expression_data_util.exec_query(sql=query)
    result: List[Tuple[str]] = expression_data_util.cursor.fetchall()
    handler_names: List[str] = [
        event_handler_scope.remove_suffix_num_from_handler_name(
            handler_name=tpl[0])
        for tpl in result]
    return handler_names
