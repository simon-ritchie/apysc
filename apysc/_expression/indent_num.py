"""Implementations of expression's indent number related interfaces.

Mainly following interfaces are defined:

- get_current_indent_num: Get a current indent number.
- Indent: Class implementation for increment and decrement
    indentation number. Basically use this class at with statement.
- reset: Reset current indent number.
"""

from typing import Any
from typing import List
from typing import Optional
from typing import Tuple


def get_current_indent_num() -> int:
    """
    Get a current indent number.

    Returns
    -------
    current_indent_num : int
        Current indent number.
    """
    from apysc._expression import expression_data_util
    table_name: str = _get_indent_num_table_name()
    query: str = (
        f'SELECT num FROM {table_name} LIMIT 1;'
    )
    expression_data_util.exec_query(sql=query)
    result: Optional[Tuple[int]] = expression_data_util.cursor.fetchone()
    if result is None:
        return 0
    current_indent_num: int = result[0]
    return current_indent_num


def _save_current_indent_num(*, indent_num: int) -> None:
    """
    Save the current indentation number.

    Parameters
    ----------
    indent_num : int
        Current indentation number.
    """
    from apysc._expression import expression_data_util
    table_name: str = _get_indent_num_table_name()
    query: str = f'DELETE FROM {table_name};'
    expression_data_util.exec_query(sql=query, commit=False)
    query = (
        f'INSERT INTO {table_name}(num) VALUES ({indent_num});'
    )
    expression_data_util.exec_query(sql=query)


def _get_indent_num_table_name() -> str:
    """
    Get a indentation number table name. This value will switch
    by scope condition (e.g., event handler's scope or not).

    Returns
    -------
    table_name : str
        Target table name.
    """
    from apysc._expression import event_handler_scope
    from apysc._expression import expression_data_util
    event_handler_scope_count: int = \
        event_handler_scope.get_current_event_handler_scope_count()
    if event_handler_scope_count == 0:
        return expression_data_util.TableName.INDENT_NUM_NORMAL.value
    return expression_data_util.TableName.INDENT_NUM_HANDLER.value


class Indent:
    """Class implementation for increment and decrement
    indentation number. Basically use this class at with statement.
    """

    def __enter__(self) -> None:
        """
        Method to be used by with statement.
        This method will increment indentation number.
        """
        current_indent_num: int = get_current_indent_num()
        current_indent_num += 1
        _save_current_indent_num(indent_num=current_indent_num)

    def __exit__(self, *args: Any) -> None:
        """
        Method to be used by with statement.
        This method will decrement indentation number.

        Parameters
        ----------
        *args : list
            Any positional arguments.
        """
        current_indent_num: int = get_current_indent_num()
        current_indent_num -= 1
        if current_indent_num < 0:
            current_indent_num = 0
        _save_current_indent_num(indent_num=current_indent_num)


def reset() -> None:
    """
    Reset current indent number.
    """
    from apysc._expression import expression_data_util
    table_names: List[str] = [
        expression_data_util.TableName.INDENT_NUM_NORMAL.value,
        expression_data_util.TableName.INDENT_NUM_HANDLER.value,
    ]
    for table_name in table_names:
        query: str = f'DELETE FROM {table_name};'
        expression_data_util.exec_query(sql=query, commit=False)
    expression_data_util.connection.commit()
