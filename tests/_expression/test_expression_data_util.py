from random import randint
from typing import List
from typing import Optional
from typing import Tuple

from retrying import retry

import apysc as ap
from apysc._expression import event_handler_scope
from apysc._expression import expression_data_util
from apysc._expression import indent_num
from apysc._expression.indent_num import Indent


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_current_expression() -> None:
    expression_data_util.empty_expression()
    ap.append_js_expression(
        'console.log("Hello!");'
    )
    expression: str = expression_data_util.get_current_expression()
    assert expression == 'console.log("Hello!");'
    expression_data_util.empty_expression()

    expression = expression_data_util.get_current_expression()
    assert expression == ''


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_append_js_expression() -> None:
    indent_num.reset()
    expression_data_util.empty_expression()
    ap.append_js_expression(
        expression='var num = 100;\nvar str = "test";')
    select_query: str = (
        'SELECT txt FROM '
        f'{expression_data_util.TableName.EXPRESSION_NORMAL.value};'
    )
    expression_data_util.cursor.execute(select_query)
    result_1: Optional[Tuple[str]] = expression_data_util.cursor.fetchone()
    expression_data_util.connection.commit()
    if result_1 is None:
        raise AssertionError('result value is None.')
    expected: str = 'var num = 100;\nvar str = "test";'
    assert expected in result_1[0]

    expression_data_util.empty_expression()
    with Indent():
        ap.append_js_expression(
            expression=('var num_1 = 10;\nvar str_1 = "test";'))
    expression_data_util.cursor.execute(select_query)
    result_2: Optional[Tuple[str]] = expression_data_util.cursor.fetchone()
    expression_data_util.connection.commit()
    if result_2 is None:
        raise AssertionError('result value is None.')
    expected = (
        '  var num_1 = 10;'
        '\n  var str_1 = "test";'
    )
    assert expected in result_2[0]

    ap.append_js_expression(expression='var num_2 = 20;')
    expression_data_util.cursor.execute(select_query)
    result_3: List[Tuple[str]] = expression_data_util.cursor.fetchall()
    assert len(result_3) == 2
    assert result_3[-1][0] == 'var num_2 = 20;'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_current_expression() -> None:
    expression_data_util.empty_expression()
    current_expression: str = expression_data_util._get_current_expression(
        table_name=expression_data_util.TableName.EXPRESSION_NORMAL)
    assert current_expression == ''

    ap.append_js_expression(
        expression='console.log("Hello!");')
    current_expression = expression_data_util._get_current_expression(
        table_name=expression_data_util.TableName.EXPRESSION_NORMAL)
    assert current_expression == 'console.log("Hello!");'

    ap.append_js_expression(
        expression='console.log("World!");')
    current_expression = expression_data_util._get_current_expression(
        table_name=expression_data_util.TableName.EXPRESSION_NORMAL)
    assert current_expression == \
        'console.log("Hello!");\nconsole.log("World!");'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_current_event_handler_scope_expression() -> None:
    expression_data_util.empty_expression()
    with event_handler_scope.HandlerScope():
        expression_data_util.append_js_expression(
            expression='console.log("Hello!");')
    current_expression: str = expression_data_util.\
        get_current_event_handler_scope_expression()
    assert current_expression == 'console.log("Hello!");'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__create_expression_normal_table() -> None:
    expression_data_util._create_expression_normal_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.EXPRESSION_NORMAL)
    assert result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__table_exists() -> None:
    expression_data_util._create_expression_normal_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.EXPRESSION_NORMAL)
    assert result

    result = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.NOT_EXISTING)
    assert not result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_initialize_sqlite_tables_if_not_initialized() -> None:
    expression_data_util.initialize_sqlite_tables_if_not_initialized()
    query: str = (
        'DROP TABLE IF EXISTS '
        f'{expression_data_util.TableName.EXPRESSION_NORMAL.value};')
    expression_data_util.cursor.execute(query)
    expression_data_util.connection.commit()

    initialized: bool = expression_data_util.\
        initialize_sqlite_tables_if_not_initialized()
    assert initialized
    table_exists: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.EXPRESSION_NORMAL)
    assert table_exists

    initialized = expression_data_util.\
        initialize_sqlite_tables_if_not_initialized()
    assert not initialized


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__make_create_table_query() -> None:
    query: str = expression_data_util._make_create_table_query(
        table_name=expression_data_util.TableName.EXPRESSION_HANDLER,
        column_ddl='  id INTEGER,\n  name TEXT')
    expected: str = (
        'CREATE TABLE IF NOT EXISTS '
        f'{expression_data_util.TableName.EXPRESSION_HANDLER.value} ('
        '\n  id INTEGER,'
        '\n  name TEXT'
        '\n);'
    )
    assert query == expected


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__create_expression_handler_table() -> None:
    expression_data_util._create_expression_handler_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.EXPRESSION_HANDLER)
    assert result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__create_indent_num_normal_table() -> None:
    expression_data_util._create_indent_num_normal_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.INDENT_NUM_NORMAL)
    assert result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__create_indent_num_handler_table() -> None:
    expression_data_util._create_indent_num_handler_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.INDENT_NUM_HANDLER)
    assert result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__create_last_scope_table() -> None:
    expression_data_util._create_last_scope_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.LAST_SCOPE)
    assert result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__create_event_handler_scope_count_table() -> None:
    expression_data_util._create_event_handler_scope_count_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.EVENT_HANDLER_SCOPE_COUNT)
    assert result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__create_loop_count_table() -> None:
    expression_data_util._create_loop_count_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.LOOP_COUNT)
    assert result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__create_debug_mode_setting_table() -> None:
    expression_data_util._create_debug_mode_setting_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.DEBUG_MODE_SETTING)
    assert result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_empty_expression() -> None:
    expression_data_util._create_expression_normal_table()
    expression_data_util.cursor.execute(
        'INSERT INTO '
        f'{expression_data_util.TableName.EXPRESSION_NORMAL.value}'
        '(txt) VALUES ("test_text");')
    expression_data_util.empty_expression()
    expression_data_util.cursor.execute(
        'SELECT * FROM '
        f'{expression_data_util.TableName.EXPRESSION_NORMAL.value} '
        'LIMIT 1;')
    result: Optional[Tuple] = expression_data_util.cursor.fetchone()
    assert result is None


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_expression_table_name() -> None:
    with event_handler_scope.HandlerScope():
        table_name: expression_data_util.TableName = expression_data_util.\
            _get_expression_table_name()
    assert table_name == expression_data_util.TableName.EXPRESSION_HANDLER

    table_name = expression_data_util._get_expression_table_name()
    assert table_name == expression_data_util.TableName.EXPRESSION_NORMAL


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__create_debug_mode_callable_count_table() -> None:
    expression_data_util._create_debug_mode_setting_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.DEBUG_MODE_CALLABLE_COUNT)
    assert result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__create_stage_elem_id_table() -> None:
    expression_data_util._create_stage_elem_id_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.STAGE_ELEM_ID)
    assert result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__create_variable_name_count_table() -> None:
    expression_data_util._create_variable_name_count_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.VARIABLE_NAME_COUNT)
    assert result
