"""The implementation of manipulating HTL and js expression files.

Mainly following interfaces are defined:

- empty_expression : Empty the current js expression data.
- append_js_expression : Append js expression.
- get_current_expression : Get current expression string.
- get_current_event_handler_scope_expression : Get a current
    event handler scope's expression string.
- exec_query : Execute a SQLite sql query.
"""

import sqlite3
from enum import Enum
from typing import Any
from typing import Callable
from typing import List
from typing import Optional
from typing import Tuple
from typing import TypeVar

from apysc._validation import arg_validation_decos


class TableName(Enum):
    NOT_EXISTING = "not_existing"
    EXPRESSION_NORMAL = "expression_normal"
    EXPRESSION_HANDLER = "expression_handler"
    INDENT_NUM_NORMAL = "indent_num_normal"
    INDENT_NUM_HANDLER = "indent_num_handler"
    LAST_SCOPE = "last_scope"
    EVENT_HANDLER_SCOPE_COUNT = "event_handler_scope_count"
    LOOP_COUNT = "loop_count"
    DEBUG_MODE_SETTING = "debug_mode_setting"
    DEBUG_MODE_CALLABLE_COUNT = "debug_mode_callable_count"
    STAGE_ELEM_ID = "stage_elem_id"
    VARIABLE_NAME_COUNT = "variable_name_count"
    HANDLER_CALLING_STACK = "handler_calling_stack"
    CIRCULAR_CALLING_HANDLER_NAME = "circular_calling_handler_name"
    STAGE_ID = "stage_id"


_SQLITE_IN_MEMORY_SETTING: str = "file::memory:?cache=shared"
connection = sqlite3.connect(_SQLITE_IN_MEMORY_SETTING, uri=True)
cursor = connection.cursor()

_Callable = TypeVar("_Callable", bound=Callable)


def _check_connection(func: _Callable) -> _Callable:
    """
    The decorator function checks an SQLite connection
    when a specified function calls. If failed, create
    a new connection and recall a function.

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
def _table_exists(*, table_name: TableName) -> bool:
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


def _make_create_table_query(*, table_name: TableName, column_ddl: str) -> str:
    """
    Make a create table SQL query.

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
        A create table SQL query.
    """
    query: str = (
        "CREATE TABLE IF NOT EXISTS " f"{table_name.value} (" f"\n{column_ddl}" "\n);"
    )
    return query


_EXPRESSION_TABLE_COLUMN_DDL: str = (
    "  id INTEGER PRIMARY KEY AUTOINCREMENT," "\n  txt TEXT NOT NULL"
)


@_check_connection
def _create_expression_normal_table() -> None:
    """
    Create the normal expression data SQLite table.
    """
    query: str = _make_create_table_query(
        table_name=TableName.EXPRESSION_NORMAL, column_ddl=_EXPRESSION_TABLE_COLUMN_DDL
    )
    cursor.execute(query)


@_check_connection
def _create_expression_handler_table() -> None:
    """
    Create the handler expression data SQLite table.
    """
    query: str = _make_create_table_query(
        table_name=TableName.EXPRESSION_HANDLER, column_ddl=_EXPRESSION_TABLE_COLUMN_DDL
    )
    cursor.execute(query)


_INDENT_NUM_TABLE_COLUMN_DDL: str = "  num INTEGER NOT NULL"


@_check_connection
def _create_indent_num_normal_table() -> None:
    """
    Create the normal indentation number data SQLite table.
    """
    query: str = _make_create_table_query(
        table_name=TableName.INDENT_NUM_NORMAL, column_ddl=_INDENT_NUM_TABLE_COLUMN_DDL
    )
    cursor.execute(query)


@_check_connection
def _create_indent_num_handler_table() -> None:
    """
    Create the handler indentation number data SQLite table.
    """
    query: str = _make_create_table_query(
        table_name=TableName.INDENT_NUM_HANDLER, column_ddl=_INDENT_NUM_TABLE_COLUMN_DDL
    )
    cursor.execute(query)


@_check_connection
def _create_last_scope_table() -> None:
    """
    Create the last scope data SQLite table.
    """
    query: str = _make_create_table_query(
        table_name=TableName.LAST_SCOPE, column_ddl=("  last_scope INTEGER NOT NULL")
    )
    cursor.execute(query)


@_check_connection
def _create_event_handler_scope_count_table() -> None:
    """
    Create the event handler scope count value SQLite table.
    """
    query: str = _make_create_table_query(
        table_name=TableName.EVENT_HANDLER_SCOPE_COUNT,
        column_ddl=("  count INTEGER NOT NULL"),
    )
    cursor.execute(query)


@_check_connection
def _create_loop_count_table() -> None:
    """
    Create the loop count value SQLite table.
    """
    query: str = _make_create_table_query(
        table_name=TableName.LOOP_COUNT, column_ddl=("  count INTEGER NOT NULL")
    )
    cursor.execute(query)


@_check_connection
def _create_debug_mode_setting_table() -> None:
    """
    Create the debug mode setting SQLite table.
    """
    query: str = _make_create_table_query(
        table_name=TableName.DEBUG_MODE_SETTING,
        column_ddl=("  is_debug_mode INTEGER NOT NULL"),
    )
    cursor.execute(query)


@_check_connection
def _create_debug_mode_callable_count_table() -> None:
    """
    Create the debug mode callable count data SQLite table.
    """
    query: str = _make_create_table_query(
        table_name=TableName.DEBUG_MODE_CALLABLE_COUNT,
        column_ddl=(
            "  id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "\n  name TEXT NOT NULL,"
            "\n  count INTEGER NOT NULL"
        ),
    )
    cursor.execute(query)


@_check_connection
def _create_stage_elem_id_table() -> None:
    """
    Create the stage element id data SQLite table.
    """
    query: str = _make_create_table_query(
        table_name=TableName.STAGE_ELEM_ID, column_ddl="  elem_id TEXT NOT NULL"
    )
    cursor.execute(query)


@_check_connection
def _create_variable_name_count_table() -> None:
    """
    Create the variable name count data SQLite table.
    """
    query: str = _make_create_table_query(
        table_name=TableName.VARIABLE_NAME_COUNT,
        column_ddl=(
            "  id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "\n  type_name TEXT NOT NULL,"
            "\n  count INTEGER NOT NULL"
        ),
    )
    cursor.execute(query)


@_check_connection
def _create_handler_calling_stack_table() -> None:
    """
    Create the handler calling stack data SQLite table.
    """
    query: str = _make_create_table_query(
        table_name=TableName.HANDLER_CALLING_STACK,
        column_ddl=(
            "  id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "\n  handler_name TEXT NOT NULL,"
            "\n  scope_count INTEGER NOT NULL,"
            "\n  variable_name TEXT NOT NULL"
        ),
    )
    cursor.execute(query)


@_check_connection
def _create_circular_calling_handler_name_table() -> None:
    """
    Create the circular calling handler names data SQLite table.
    """
    query: str = _make_create_table_query(
        table_name=TableName.CIRCULAR_CALLING_HANDLER_NAME,
        column_ddl=(
            "  id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "\n  handler_name TEXT NOT NULL,"
            "\n  prev_handler_name TEXT NOT NULL,"
            "\n  prev_variable_name TEXT NOT NULL"
        ),
    )
    cursor.execute(query)


@_check_connection
def _create_stage_id_table() -> None:
    """
    Create the stage id data SQLite table.
    """
    query: str = _make_create_table_query(
        table_name=TableName.STAGE_ID, column_ddl="  stage_id INTEGER NOT NULL"
    )
    cursor.execute(query)


def initialize_sqlite_tables_if_not_initialized() -> bool:
    """
    Initialize the SQLite tables if the apysc does not
    initialize them yet.

    Returns
    -------
    initialized : bool
        If initialized, returns True.
    """
    table_exists: bool = _table_exists(table_name=TableName.EXPRESSION_NORMAL)
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
    _create_debug_mode_callable_count_table()
    _create_stage_elem_id_table()
    _create_variable_name_count_table()
    _create_handler_calling_stack_table()
    _create_circular_calling_handler_name_table()
    _create_stage_id_table()
    return True


def empty_expression() -> None:
    """
    Empty the current js expression data.
    """
    initialize_sqlite_tables_if_not_initialized()
    for table_name in TableName:
        if table_name == TableName.NOT_EXISTING:
            continue
        query: str = f"DELETE FROM {table_name.value};"
        cursor.execute(query)
    connection.commit()


@arg_validation_decos.is_builtin_string(arg_position_index=0, optional=False)
def append_js_expression(expression: str) -> None:
    """
    Append js expression.

    Parameters
    ----------
    expression : str
        JavaScript Expression string.

    References
    ----------
    - append_js_expression interface
        - https://simon-ritchie.github.io/apysc/en/append_js_expression.html

    Examples
    --------
    >>> import apysc as ap
    >>> ap.append_js_expression(expression='console.log("Hello!")')
    """
    from apysc._expression import indent_num
    from apysc._expression import last_scope
    from apysc._string import indent_util

    initialize_sqlite_tables_if_not_initialized()
    current_indent_num: int = indent_num.get_current_indent_num()
    expression = indent_util.append_spaces_to_expression(
        expression=expression, indent_num=current_indent_num
    )
    expression = expression.replace('"', '""')
    table_name: TableName = _get_expression_table_name()
    query: str = f"INSERT INTO {table_name.value}(txt) " f'VALUES ("{expression}");'
    cursor.execute(query)
    connection.commit()
    last_scope.set_last_scope(value=last_scope.LastScope.NORMAL)


def _get_expression_table_name() -> TableName:
    """
    Get an expression table name. This interface switches
    this value by the current scope is event handler's one
    or not.

    Returns
    -------
    table_name : str
        Target expression table name.
    """
    from apysc._expression import event_handler_scope

    if not event_handler_scope.current_scope_is_in_event_handler():
        return TableName.EXPRESSION_NORMAL
    return TableName.EXPRESSION_HANDLER


def get_current_expression() -> str:
    """
    Get a current expression string.

    Notes
    -----
    If it is necessary to get an event handler scope's
    expression, use the get_current_event_handler_scope_expression
    function instead.

    Returns
    -------
    current_expression : str
        Current expression's string.
    """
    current_expression: str = _get_current_expression(
        table_name=TableName.EXPRESSION_NORMAL
    )
    return current_expression


def get_current_event_handler_scope_expression() -> str:
    """
    Get a current event handler scope's expression string.

    Notes
    -----
    If it is necessary to get a normal scope's expression,
    use the get_current_expression function instead.

    Returns
    -------
    current_expression : str
        Current expression's string.
    """
    current_expression: str = _get_current_expression(
        table_name=TableName.EXPRESSION_HANDLER
    )
    return current_expression


def _get_current_expression(*, table_name: TableName) -> str:
    """
    Get a current expression string from a specified table.

    Parameters
    ----------
    table_name : TableName
        Target table name.

    Returns
    -------
    current_expression : str
        Current expression string.
    """
    initialize_sqlite_tables_if_not_initialized()
    query: str = f"SELECT txt FROM {table_name.value}"
    cursor.execute(query)
    result: List[Tuple[str]] = cursor.fetchall()
    if not result:
        return ""
    expressions: List[str] = [tpl[0] for tpl in result]
    current_expression = "\n".join(expressions)
    return current_expression


class _LimitClauseCantUseError(Exception):
    ...


def _validate_limit_clause(*, sql: str) -> None:
    """
    Validate whether a LIMIT clause is used in an UPDATE or
    DELETE SQL.

    Parameters
    ----------
    sql : str
        Target sql.

    Raises
    ------
    _LimitClauseCantUseError
        If the LIMIT clause used in a DELETE or UPDATE sql.
    """
    sql_: str = sql.lower()
    if "delete " not in sql_ and "update " not in sql_:
        return
    if "limit " not in sql_:
        return
    raise _LimitClauseCantUseError(
        f"LIMIT clause cannot use in the UPDATE or DELETE sql: {sql_}"
    )


def exec_query(*, sql: str, commit: bool = True) -> None:
    """
    Execute an SQLite SQL query.

    Parameters
    ----------
    sql : str
        Target SQL.
    commit : bool, default True
        A boolean value indicating whether commit the
        transaction after the SQL query or not.

    Raises
    ------
    _LimitClauseCantUseError
        If the LIMIT clause used in a DELETE or UPDATE sql.
    """
    _validate_limit_clause(sql=sql)
    initialize_sqlite_tables_if_not_initialized()
    cursor.execute(sql)
    if commit:
        connection.commit()
