from typing import List
from typing import Optional
from typing import Tuple

import apysc as ap
from apysc._display import stage
from apysc._expression import event_handler_scope
from apysc._expression import expression_data_util
from apysc._expression.expression_data_util import _LimitClauseCantUseError
from apysc._expression.indent_num import Indent
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
from apysc._type.variable_name_mixin import VariableNameMixIn


@apply_test_settings()
def test_get_current_expression() -> None:
    ap.append_js_expression(expression='console.log("Hello!");')
    expression: str = expression_data_util.get_current_expression()
    assert 'console.log("Hello!");' in expression
    expression_data_util.empty_expression(
        skip_before_stage_instantiation_expression=False
    )


@apply_test_settings(retrying_max_attempts_num=0)
def test_append_js_expression() -> None:
    ap.append_js_expression(expression='var num = 100;\nvar str = "test";')
    select_query: str = (
        f"SELECT txt FROM {expression_data_util.TableName.EXPRESSION_NORMAL.value};"
    )
    expression_data_util.exec_query(sql=select_query)
    result_1: List[Tuple[str]] = expression_data_util.cursor.fetchall()
    if not result_1:
        raise AssertionError("result value is empty.")
    expected: str = 'var num = 100;\nvar str = "test";'
    expected_expression_exists: bool = False
    for tuple_val in result_1:
        if expected in tuple_val[0]:
            expected_expression_exists = True
            break
    assert expected_expression_exists

    ap.Stage()
    with Indent():
        ap.append_js_expression(expression=('var num_1 = 10;\nvar str_1 = "test";'))
    expression_data_util.exec_query(sql=select_query)
    result_2: List[Tuple[str]] = expression_data_util.cursor.fetchall()
    if not result_2:
        raise AssertionError("result value is empty.")
    expected = "  var num_1 = 10;" '\n  var str_1 = "test";'
    expected_expression_exists = False
    for tuple_val in result_2:
        if expected in tuple_val[0]:
            expected_expression_exists = True
            break
    assert expected_expression_exists


@apply_test_settings()
def test__get_current_expression() -> None:
    current_expression: str = expression_data_util._get_current_expression(
        table_name=expression_data_util.TableName.EXPRESSION_NORMAL
    )
    assert 'console.log("Hello!");' not in current_expression

    ap.append_js_expression(expression='console.log("Hello!");')
    current_expression = expression_data_util._get_current_expression(
        table_name=expression_data_util.TableName.EXPRESSION_NORMAL
    )
    assert 'console.log("Hello!");' in current_expression

    ap.append_js_expression(expression='console.log("World!");')
    current_expression = expression_data_util._get_current_expression(
        table_name=expression_data_util.TableName.EXPRESSION_NORMAL
    )
    assert 'console.log("Hello!");\nconsole.log("World!");' in current_expression

    expression_data_util.empty_expression(
        skip_before_stage_instantiation_expression=False
    )
    current_expression = expression_data_util._get_current_expression(
        table_name=expression_data_util.TableName.EXPRESSION_NORMAL
    )
    assert current_expression == ""


@apply_test_settings()
def test_get_current_event_handler_scope_expression() -> None:
    instance: VariableNameMixIn = VariableNameMixIn()
    instance.variable_name = "test_instance"
    with event_handler_scope.HandlerScope(
        handler_name="test_handler_1", instance=instance
    ):
        expression_data_util.append_js_expression(expression='console.log("Hello!");')
    current_expression: str = (
        expression_data_util.get_current_event_handler_scope_expression()
    )
    assert current_expression == 'console.log("Hello!");'


@apply_test_settings()
def test__create_expression_normal_table() -> None:
    expression_data_util._create_expression_normal_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.EXPRESSION_NORMAL
    )
    assert result


@apply_test_settings()
def test__table_exists() -> None:
    expression_data_util._create_expression_normal_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.EXPRESSION_NORMAL
    )
    assert result

    result = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.NOT_EXISTING
    )
    assert not result


@apply_test_settings()
def test_initialize_sqlite_tables_if_not_initialized() -> None:
    expression_data_util.initialize_sqlite_tables_if_not_initialized()
    query: str = (
        "DROP TABLE IF EXISTS "
        f"{expression_data_util.TableName.EXPRESSION_NORMAL.value};"
    )
    expression_data_util.cursor.execute(query)
    expression_data_util.connection.commit()

    initialized: bool = (
        expression_data_util.initialize_sqlite_tables_if_not_initialized()
    )
    assert initialized
    table_exists: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.EXPRESSION_NORMAL
    )
    assert table_exists

    initialized = expression_data_util.initialize_sqlite_tables_if_not_initialized()
    assert not initialized


@apply_test_settings()
def test__make_create_table_query() -> None:
    query: str = expression_data_util._make_create_table_query(
        table_name=expression_data_util.TableName.EXPRESSION_HANDLER,
        column_ddl="  id INTEGER,\n  name TEXT",
    )
    expected: str = (
        "CREATE TABLE IF NOT EXISTS "
        f"{expression_data_util.TableName.EXPRESSION_HANDLER.value} ("
        "\n  id INTEGER,"
        "\n  name TEXT"
        "\n);"
    )
    assert query == expected


@apply_test_settings()
def test__create_expression_handler_table() -> None:
    expression_data_util._create_expression_handler_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.EXPRESSION_HANDLER
    )
    assert result


@apply_test_settings()
def test__create_expression_before_stage_instantiation_table() -> None:
    expression_data_util._create_expression_before_stage_instantiation_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.EXPRESSION_BEFORE_STAGE_INSTANTIATION
    )
    assert result


@apply_test_settings()
def test__create_indent_num_normal_table() -> None:
    expression_data_util._create_indent_num_normal_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.INDENT_NUM_NORMAL
    )
    assert result


@apply_test_settings()
def test__create_indent_num_handler_table() -> None:
    expression_data_util._create_indent_num_handler_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.INDENT_NUM_HANDLER
    )
    assert result


@apply_test_settings()
def test__create_last_scope_table() -> None:
    expression_data_util._create_last_scope_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.LAST_SCOPE
    )
    assert result


@apply_test_settings()
def test__create_event_handler_scope_count_table() -> None:
    expression_data_util._create_event_handler_scope_count_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.EVENT_HANDLER_SCOPE_COUNT
    )
    assert result


@apply_test_settings()
def test__create_loop_count_table() -> None:
    expression_data_util._create_loop_count_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.LOOP_COUNT
    )
    assert result


@apply_test_settings()
def test__create_debug_mode_setting_table() -> None:
    expression_data_util._create_debug_mode_setting_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.DEBUG_MODE_SETTING
    )
    assert result


@apply_test_settings()
def test_empty_expression() -> None:
    expression_data_util._create_expression_normal_table()
    expression_data_util.cursor.execute(
        "INSERT INTO "
        f"{expression_data_util.TableName.EXPRESSION_NORMAL.value}"
        '(txt) VALUES ("test_text");'
    )
    expression_data_util.cursor.execute(
        "INSERT INTO "
        f"{expression_data_util.TableName.EXPRESSION_BEFORE_STAGE_INSTANTIATION.value}"
        '(txt) VALUES ("test_text");'
    )
    expression_data_util.empty_expression()
    expression_data_util.exec_query(
        sql=(
            "SELECT * FROM "
            f"{expression_data_util.TableName.EXPRESSION_NORMAL.value} "
            "LIMIT 1;"
        )
    )
    result: Optional[Tuple] = expression_data_util.cursor.fetchone()
    assert result is None
    assert not stage._is_stage_created

    table_name: str = (
        expression_data_util.TableName.EXPRESSION_BEFORE_STAGE_INSTANTIATION.value
    )
    expression_data_util.exec_query(sql=f"SELECT * FROM {table_name} LIMIT 1;")
    result = expression_data_util.cursor.fetchone()
    assert result is not None

    expression_data_util.empty_expression(
        skip_before_stage_instantiation_expression=False
    )
    expression_data_util.exec_query(sql=f"SELECT * FROM {table_name} LIMIT 1;")
    result = expression_data_util.cursor.fetchone()
    assert result is None


@apply_test_settings()
def test__get_expression_table_name() -> None:
    expression_data_util.empty_expression(
        skip_before_stage_instantiation_expression=False
    )
    stage._is_stage_created = False
    table_name: expression_data_util.TableName = (
        expression_data_util._get_expression_table_name()
    )
    assert table_name == (
        expression_data_util.TableName.EXPRESSION_BEFORE_STAGE_INSTANTIATION
    )

    ap.Stage()
    instance: VariableNameMixIn = VariableNameMixIn()
    instance.variable_name = "test_instance"
    with event_handler_scope.HandlerScope(
        handler_name="test_handler_1", instance=instance
    ):
        table_name = expression_data_util._get_expression_table_name()
    assert table_name == expression_data_util.TableName.EXPRESSION_HANDLER

    table_name = expression_data_util._get_expression_table_name()
    assert table_name == expression_data_util.TableName.EXPRESSION_NORMAL


@apply_test_settings()
def test__create_debug_mode_callable_count_table() -> None:
    expression_data_util._create_debug_mode_setting_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.DEBUG_MODE_CALLABLE_COUNT
    )
    assert result


@apply_test_settings()
def test__create_stage_elem_id_table() -> None:
    expression_data_util._create_stage_elem_id_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.STAGE_ELEM_ID
    )
    assert result


@apply_test_settings()
def test__create_variable_name_count_table() -> None:
    expression_data_util._create_variable_name_count_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.VARIABLE_NAME_COUNT
    )
    assert result


@apply_test_settings()
def test__create_handler_calling_stack_table() -> None:
    expression_data_util._create_handler_calling_stack_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.HANDLER_CALLING_STACK
    )
    assert result


@apply_test_settings()
def test__create_circular_calling_handler_name_table() -> None:
    expression_data_util._create_circular_calling_handler_name_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.CIRCULAR_CALLING_HANDLER_NAME
    )
    assert result


@apply_test_settings()
def test__create_stage_id_table() -> None:
    expression_data_util._create_stage_id_table()
    result: bool = expression_data_util._table_exists(
        table_name=expression_data_util.TableName.STAGE_ID
    )
    assert result


@apply_test_settings()
def test__validate_limit_clause() -> None:
    sqls: List[str] = [
        "DELETE FROM test_table LIMIT 1;",
        "UPDATE test_table SET a = 10 LIMIT 1;",
    ]
    for sql in sqls:
        assert_raises(
            expected_error_class=_LimitClauseCantUseError,
            callable_=expression_data_util._validate_limit_clause,
            match="LIMIT clause cannot use in the UPDATE or DELETE sql",
            sql=sql,
        )

    expression_data_util._validate_limit_clause(sql="SELECT a FROM test_table LIMIT 1;")


@apply_test_settings()
def test_exec_query() -> None:
    expression_data_util.empty_expression(
        skip_before_stage_instantiation_expression=False
    )
    table_name: str = expression_data_util.TableName.DEBUG_MODE_CALLABLE_COUNT.value
    expression_data_util.exec_query(
        sql=f"INSERT INTO {table_name}(name, count) VALUES('a', 1);"
    )

    expression_data_util.exec_query(
        sql=f"SELECT count FROM {table_name} WHERE name = 'a' LIMIT 1;"
    )
    result: Optional[Tuple[int]] = expression_data_util.cursor.fetchone()
    assert result == (1,)


@apply_test_settings(retrying_max_attempts_num=0)
def test_get_current_before_stage_instantiation_expression() -> None:
    expression_data_util.empty_expression(
        skip_before_stage_instantiation_expression=False
    )
    stage._is_stage_created = False
    expression_data_util.append_js_expression(expression='console.log("Hello!");')
    expression: str = (
        expression_data_util.get_current_before_stage_instantiation_expression()
    )
    assert 'console.log("Hello!");' in expression


@apply_test_settings()
def test_copy_expression_before_stage_instantiation() -> None:
    expression_data_util.empty_expression(
        skip_before_stage_instantiation_expression=False
    )
    stage._is_stage_created = False
    assert_raises(
        expected_error_class=stage.StageNotCreatedError,
        callable_=expression_data_util.copy_expression_before_stage_instantiation,
    )

    expression_data_util.append_js_expression(expression='console.log("Hello!");')
    ap.Stage()
    expression_data_util.copy_expression_before_stage_instantiation()
    expression: str = expression_data_util.get_current_expression()
    assert 'console.log("Hello!");' in expression
