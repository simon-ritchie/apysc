"""Handler circular calling related utilities.
"""


from typing import List, Tuple


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
    handler_names: List[str] = _read_handler_names()
    pass


def _read_handler_names() -> List[str]:
    """
    Read the current handler names from the calling stack.

    Returns
    -------
    handler_names : list of str
        Target handler names.
    """
    from apysc._expression import expression_data_util
    expression_data_util.initialize_sqlite_tables_if_not_initialized()
    table_name: str = expression_data_util.TableName.\
        HANDLER_CALLING_STACK.value
    query: str = (
        f'SELECT handler_name FROM {table_name} '
        f'ORDER BY scope_count'
    )
    expression_data_util.cursor.execute(query)
    result: List[Tuple[str]] = expression_data_util.cursor.fetchall()
    handler_names: List[str] = [tpl[0] for tpl in result]
    return handler_names
