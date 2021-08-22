import os
import re
from random import randint
from typing import Match
from typing import Optional
import sqlite3

from retrying import retry

import apysc as ap
from apysc._expression import event_handler_scope
from apysc._expression import expression_file_util
from apysc._expression import indent_num
from apysc._expression.indent_num import Indent
from apysc._file import file_util


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_empty_expression_dir() -> None:
    os.makedirs(expression_file_util.EXPRESSION_ROOT_DIR, exist_ok=True)
    test_file_path: str = os.path.join(
        expression_file_util.EXPRESSION_ROOT_DIR,
        'test_file.txt',
    )
    with open(test_file_path, 'w') as f:
        f.write('\n')
    expression_file_util.empty_expression()
    assert not os.path.exists(test_file_path)
    assert os.path.exists(expression_file_util.EXPRESSION_ROOT_DIR)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_current_expression() -> None:
    expression_file_util.empty_expression()
    ap.append_js_expression(
        'console.log("Hello!");'
    )
    expression: str = expression_file_util.get_current_expression()
    assert expression == 'console.log("Hello!");'
    expression_file_util.empty_expression()

    expression = expression_file_util.get_current_expression()
    assert expression == ''


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_append_js_expression() -> None:
    indent_num.reset()
    expression_file_util.empty_expression()
    ap.append_js_expression(expression='var num = 100;')
    expression: str = expression_file_util.get_current_expression()
    match: Optional[Match] = re.search(
        pattern=r'^var num = 100;',
        string=expression,
        flags=re.MULTILINE)
    assert match is not None

    expression_file_util.empty_expression()
    with Indent():
        ap.append_js_expression(
            expression='var num_1 = 100;\nvar num_2 = 200;\nvar num_3 = 300;')
        expression = expression_file_util.get_current_expression()
        match = re.search(
            pattern=r'^  var num_2 = 200;',
            string=expression,
            flags=re.MULTILINE)

    event_handler_scope._increment_scope_count()
    ap.append_js_expression('console.log("Hello!");')
    expression = \
        expression_file_util.get_current_event_handler_scope_expression()
    assert 'console.log("Hello!");' in expression
    expression_file_util.empty_expression()


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_current_expression() -> None:
    expression_file_util.empty_expression()
    ap.append_js_expression(
        expression='console.log("Hello!");')
    current_expression: str = expression_file_util._get_current_expression(
        file_path=expression_file_util.EXPRESSION_FILE_PATH)
    assert current_expression == 'console.log("Hello!");'

    expression_file_util.empty_expression()
    current_expression = expression_file_util.get_current_expression()
    assert current_expression == ''


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_current_event_handler_scope_expression() -> None:
    expression_file_util.empty_expression()
    file_util.save_plain_txt(
        txt='console.log("Hello!");',
        file_path=expression_file_util.EVENT_HANDLER_EXPRESSION_FILE_PATH)
    current_expression: str = expression_file_util.\
        get_current_event_handler_scope_expression()
    assert current_expression == 'console.log("Hello!");'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_expression_file_path() -> None:
    expression_file_util.empty_expression()
    file_path: str = expression_file_util._get_expression_file_path()
    assert file_path == expression_file_util.EXPRESSION_FILE_PATH

    event_handler_scope._increment_scope_count()
    file_path = expression_file_util._get_expression_file_path()
    assert file_path == \
        expression_file_util.EVENT_HANDLER_EXPRESSION_FILE_PATH
    expression_file_util.empty_expression()


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__create_expression_normal_table() -> None:
    expression_file_util._create_expression_normal_table()
    result: bool = expression_file_util._table_exists(
        table_name=expression_file_util._TableName.EXPRESSION_NORMAL)
    assert result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__table_exists() -> None:
    expression_file_util._create_expression_normal_table()
    result: bool = expression_file_util._table_exists(
        table_name=expression_file_util._TableName.EXPRESSION_NORMAL)
    assert result

    result = expression_file_util._table_exists(
        table_name=expression_file_util._TableName.NOT_EXISTING)
    assert not result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__initialize_sqlite_tables_if_not_initialized() -> None:
    initialized: bool = expression_file_util.\
        _initialize_sqlite_tables_if_not_initialized()
    assert initialized
    table_exists: bool = expression_file_util._table_exists(
        table_name=expression_file_util._TableName.EXPRESSION_NORMAL)
    assert table_exists

    initialized = expression_file_util.\
        _initialize_sqlite_tables_if_not_initialized()
    assert not initialized


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__make_create_table_query() -> None:
    query: str = expression_file_util._make_create_table_query(
        table_name=expression_file_util._TableName.EXPRESSION_HANDLER,
        column_ddl='  id INTEGER,\n  name TEXT')
    expected: str = (
        'CREATE TABLE IF NOT EXISTS '
        f'{expression_file_util._TableName.EXPRESSION_HANDLER.value} ('
        '\n  id INTEGER,'
        '\n  name TEXT'
        '\n);'
    )
    assert query == expected


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__create_expression_handler_table() -> None:
    expression_file_util._create_expression_handler_table()
    result: bool = expression_file_util._table_exists(
        table_name=expression_file_util._TableName.EXPRESSION_HANDLER)
    assert result
