"""The implementation of manipulating HTL and js expression files.

Mainly following interfaces are defined:

- empty_expression : Empty the current js expression data.
- append_js_expression : Append js expression to the file.
- get_current_expression : Get current expression string.
- get_current_event_handler_scope_expression : Get a current
    event handler scope's expression string from a file.
"""

import os
import sqlite3
from enum import Enum
from typing import Any, Callable, Optional, Tuple
from typing import TypeVar

EXPRESSION_ROOT_DIR: str = '../.apysc_expression/'
EXPRESSION_FILE_PATH: str = os.path.join(
    EXPRESSION_ROOT_DIR, 'expression.txt')
EVENT_HANDLER_EXPRESSION_FILE_PATH: str = os.path.join(
    EXPRESSION_ROOT_DIR, 'event_handler_expression.txt')
INDENT_NUM_FILE_PATH: str = os.path.join(
    EXPRESSION_ROOT_DIR, 'indent_num.txt')
EVENT_HANDLER_INDENT_NUM_FILE_PATH: str = os.path.join(
    EXPRESSION_ROOT_DIR, 'event_handler_indent_num.txt')
LAST_SCOPE_FILE_PATH: str = os.path.join(
    EXPRESSION_ROOT_DIR, 'last_scope.txt')
EVENT_HANDLER_SCOPE_COUNT_FILE_PATH: str = os.path.join(
    EXPRESSION_ROOT_DIR, 'event_handler_scope_count.txt')
LOOP_COUNT_FILE_PATH: str = os.path.join(
    EXPRESSION_ROOT_DIR, 'loop_count.txt')
DEBUG_MODE_SETTING_FILE_PATH: str = os.path.join(
    EXPRESSION_ROOT_DIR, 'debug_mode_setting.txt')


class TableName(Enum):
    NOT_EXISTING = 'not_existing'
    EXPRESSION_NORMAL = 'expression_normal'
    EXPRESSION_HANDLER = 'expression_handler'
    INDENT_NUM_NORMAL = 'indent_num_normal'
    INDENT_NUM_HANDLER = 'indent_num_handler'
    LAST_SCOPE = 'last_scope'
    EVENT_HANDLER_SCOPE_COUNT = 'event_handler_scope_count'
    LOOP_COUNT = 'loop_count'
    DEBUG_MODE_SETTING = 'debug_mode_setting'

_SQLITE_IN_MEMORY_SETTING: str = 'file::memory:?cache=shared'
connection = sqlite3.connect(_SQLITE_IN_MEMORY_SETTING, uri=True)
cursor = connection.cursor()

_C = TypeVar('_C', bound=Callable)


def _check_connection(func: _C) -> _C:
    """
    The decorator function to check a SQLite connection when a
    specified function calling, and if failed, create a new
    connection and recall a function.

    Parameters
    ----------
    func : Callable
        Target function to decorate.

    Returns
    -------
    new_func : Callable
        Decorated function.
    """

    def new_func(*args: Any, **kwargs: Any) -> Any:
        """
        Function for the decoration.

        Parameters
        ----------
        *args : list
            Any positional arguments.
        **kwargs : dict
            Any keyword arguments.

        Returns
        -------
        result : Any
            Any returned value.
        """
        global connection, cursor
        try:
            result: Any = func(*args, **kwargs)
        except Exception:
            connection = sqlite3.connect(_SQLITE_IN_MEMORY_SETTING, uri=True)
            cursor = connection.cursor()
            result = func(*args, **kwargs)
        return result

    return new_func  # type: ignore


@_check_connection
def _table_exists(table_name: TableName) -> bool:
    """
    Get a boolean value whether a specified table exists or not.

    Parameters
    ----------
    table_name : TableName
        Target table name.

    Returns
    -------
    result : bool
        If exists, returns True.
    """
    query: str = (
        'SELECT name FROM sqlite_master WHERE type = "table" '
        f'AND name = "{table_name.value}" LIMIT 1;'
    )
    cursor.execute(query)
    result: Optional[Tuple] = cursor.fetchone()
    connection.commit()
    if result:
        return True
    return False


def _make_create_table_query(
        table_name: TableName,
        column_ddl: str) -> str:
    """
    Make a create table sql query.

    Parameters
    ----------
    table_name : str
        Target table name.
    column_ddl : str
        Target table columns DDL string.
        e.g., '  id INTEGER, ...'

    Returns
    -------
    query : str
        A create table sql query.
    """
    query: str = (
        'CREATE TABLE IF NOT EXISTS '
        f'{table_name.value} ('
        f'\n{column_ddl}'
        '\n);'
    )
    return query


_EXPRESSION_TABLE_COLUMN_DDL: str = (
    '  id INTEGER PRIMARY KEY AUTOINCREMENT,'
    '\n  txt TEXT NOT NULL'
)


@_check_connection
def _create_expression_normal_table() -> None:
    """
    Create the normal expression data SQLite table.
    """
    query: str = _make_create_table_query(
        table_name=TableName.EXPRESSION_NORMAL,
        column_ddl=_EXPRESSION_TABLE_COLUMN_DDL)
    cursor.execute(query)


@_check_connection
def _create_expression_handler_table() -> None:
    """
    Create the handler expression data SQLite table.
    """
    query: str = _make_create_table_query(
        table_name=TableName.EXPRESSION_HANDLER,
        column_ddl=_EXPRESSION_TABLE_COLUMN_DDL)
    cursor.execute(query)


_INDENT_NUM_TABLE_COLUMN_DDL: str = '  num INTEGER NOT NULL'


@_check_connection
def _create_indent_num_normal_table() -> None:
    """
    Create the normal indentation number data SQLite table.
    """
    query: str = _make_create_table_query(
        table_name=TableName.INDENT_NUM_NORMAL,
        column_ddl=_INDENT_NUM_TABLE_COLUMN_DDL)
    cursor.execute(query)


@_check_connection
def _create_indent_num_handler_table() -> None:
    """
    Create the handler indentation number data SQLite table.
    """
    query: str = _make_create_table_query(
        table_name=TableName.INDENT_NUM_HANDLER,
        column_ddl=_INDENT_NUM_TABLE_COLUMN_DDL)
    cursor.execute(query)


@_check_connection
def _create_last_scope_table() -> None:
    """
    Create the last scope data SQLite table.
    """
    query: str = _make_create_table_query(
        table_name=TableName.LAST_SCOPE,
        column_ddl=(
            '  last_scope INTEGER NOT NULL'
        ))
    cursor.execute(query)


@_check_connection
def _create_event_handler_scope_count_table() -> None:
    """
    Create the event handler scope count value SQLite table.
    """
    query: str = _make_create_table_query(
        table_name=TableName.EVENT_HANDLER_SCOPE_COUNT,
        column_ddl=(
            '  count INTEGER NOT NULL'
        ))
    cursor.execute(query)


@_check_connection
def _create_loop_count_table() -> None:
    """
    Create the loop count value SQLite table.
    """
    query: str = _make_create_table_query(
        table_name=TableName.LOOP_COUNT,
        column_ddl=(
            '  count INTEGER NOT NULL'
        ))
    cursor.execute(query)


@_check_connection
def _create_debug_mode_setting_table() -> None:
    """
    Create the debug mode setting SQLite table.
    """
    query: str = _make_create_table_query(
        table_name=TableName.DEBUG_MODE_SETTING,
        column_ddl=(
            '  is_debug_mode INTEGER NOT NULL'
        ))
    cursor.execute(query)


def initialize_sqlite_tables_if_not_initialized() -> bool:
    """
    Initialize the sqlite tables if they have not been
    initialized yet.

    Returns
    -------
    initialized : bool
        If initialized, returns True.
    """
    table_exists: bool = _table_exists(
        table_name=TableName.EXPRESSION_NORMAL)
    if table_exists:
        return False
    _create_expression_normal_table()
    _create_expression_handler_table()
    _create_indent_num_normal_table()
    _create_indent_num_handler_table()
    _create_last_scope_table()
    _create_event_handler_scope_count_table()
    _create_loop_count_table()
    _create_debug_mode_setting_table()
    return True


def empty_expression() -> None:
    """
    Empty the current js expression data.
    """
    initialize_sqlite_tables_if_not_initialized()
    for table_name in TableName:
        if table_name == TableName.NOT_EXISTING:
            continue
        query: str = f'DELETE FROM {table_name.value};'
        cursor.execute(query)
    connection.commit()


def append_js_expression(expression: str) -> None:
    """
    Append js expression to the file.

    Parameters
    ----------
    expression : str
        JavaScript Expression string.
    """
    from apysc._expression import indent_num
    from apysc._expression import last_scope
    from apysc._string import indent_util
    initialize_sqlite_tables_if_not_initialized()
    current_indent_num: int = indent_num.get_current_indent_num()
    expression = indent_util.append_spaces_to_expression(
        expression=expression, indent_num=current_indent_num)
    expression = expression.replace('"', '""')
    table_name: TableName = _get_expression_table_name()
    query: str = (
        f'INSERT INTO {table_name.value}(txt) '
        f'VALUES ("{expression}");'
    )
    cursor.execute(query)
    connection.commit()
    last_scope.set_last_scope(value=last_scope.LastScope.NORMAL)


def _get_expression_table_name() -> TableName:
    """
    Get a expression table name. This value will be switched whether
    current scope is event handler's one or not.

    Returns
    -------
    table_name : str
        Target expression table name.
    """
    from apysc._expression import event_handler_scope
    event_handler_scope_count: int = \
        event_handler_scope.get_current_event_handler_scope_count()
    if event_handler_scope_count == 0:
        return TableName.EXPRESSION_NORMAL
    return TableName.EXPRESSION_HANDLER


def get_current_expression() -> str:
    """
    Get a current expression's string from a file.

    Notes
    -----
    If it is necessary to get event handler scope's expression,
    then use get_current_event_handler_scope_expression function
    instead.

    Returns
    -------
    current_expression : str
        Current expression's string.
    """
    current_expression: str = _get_current_expression(
        file_path=EXPRESSION_FILE_PATH)
    return current_expression


def get_current_event_handler_scope_expression() -> str:
    """
    Get a current event handler scope's expression string from a file.

    Notes
    -----
    If it is necessary to get normal scope's expression, then use
    get_current_expression function instead.

    Returns
    -------
    current_expression : str
        Current expression's string.
    """
    current_expression: str = _get_current_expression(
        file_path=EVENT_HANDLER_EXPRESSION_FILE_PATH)
    return current_expression


def _get_current_expression(file_path: str) -> str:
    """
    Get a current expression's string from specified file path.

    Parameters
    ----------
    file_path : str
        Target file path.

    Returns
    -------
    current_expression : str
        Current expression's string.
    """
    from apysc._file import file_util
    if not os.path.isfile(file_path):
        return ''
    current_expression: str = file_util.read_txt(
        file_path=file_path)
    current_expression = current_expression.strip()
    return current_expression
