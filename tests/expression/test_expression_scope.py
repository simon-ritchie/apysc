import os
from apyscript.expression import expression_scope
from apyscript.expression import expression_file_util
from apyscript.file import file_util
from tests import testing_helper


def test_update_current_scope() -> None:
    expression_scope.update_current_scope(scope_name='main__main')
    current_scope: str = file_util.read_txt(
        file_path=expression_file_util.CURRENT_SCOPE_FILE_PATH)
    assert current_scope == 'main__main'


def test_get_current_scope() -> None:
    expression_scope.update_current_scope(' main__main')
    current_scope: str = expression_scope.get_current_scope()
    assert current_scope == 'main__main'

    file_util.remove_file_if_exists(
        file_path=expression_file_util.CURRENT_SCOPE_FILE_PATH)
    current_scope = expression_scope.get_current_scope()
    assert current_scope == expression_file_util.ROOT_SCOPE


def test_get_scope_name_from_file_path() -> None:
    scope_name: str = expression_scope.get_scope_name_from_file_path(
        expression_file_path='any__scope___name.html')
    assert scope_name == 'any__scope___name'


def test__get_scope_wrapper_function_head() -> None:
    scope_wrapper_function_head: str = \
        expression_scope._get_scope_wrapper_function_head(
            scope_name='any___scope___name')
    expected: str = 'function any___scope___name() {'
    assert scope_wrapper_function_head == expected


def test_append_scope_wrapper_func_to_expression() -> None:
    expression: str = (
        '<html>'
        '\n<script type="text/javascript" src="jquery.min.js"></script>'
        '\n<script type="text/javascript">'
        '\n  console.log("Hello apyscript!");'
        '\n</script>'
        '\n</html>'
    )
    result_expression: str = expression_scope.\
        append_scope_wrapper_func_to_expression(
            expression=expression, scope_name='any___scope___name')
    expected: str = (
        '<html>'
        '\n<script type="text/javascript" src="jquery.min.js"></script>'
        '\n<script type="text/javascript">'
        '\nfunction any___scope___name() {'
        '\n  console.log("Hello apyscript!");'
        '\n}'
        '\n</script>'
        '\n</html>'
    )
    assert result_expression == expected


def test__save_scope_history() -> None:
    file_util.remove_file_if_exists(
        file_path=expression_file_util.SCOPE_HISTORY_FILE_PATH)
    expression_scope._save_scope_history(
        scope_name='any___scope___name___1')
    expression_scope._save_scope_history(
        scope_name='any___scope___name___2')
    scope_history: str = file_util.read_txt(
        file_path=expression_file_util.SCOPE_HISTORY_FILE_PATH)
    expected: str = 'any___scope___name___1,any___scope___name___2,'
    assert scope_history == expected

    file_util.remove_file_if_exists(
        file_path=expression_file_util.SCOPE_HISTORY_FILE_PATH)


def test__reset_scope_history_if_scope_is_main_entry_point() -> None:
    testing_helper.make_blank_file(
        file_path=expression_file_util.SCOPE_HISTORY_FILE_PATH)
    expression_scope._reset_scope_history_if_scope_is_main_entry_point(
        scope_name='any___scope___name')
    assert os.path.exists(expression_file_util.SCOPE_HISTORY_FILE_PATH)

    expression_scope._reset_scope_history_if_scope_is_main_entry_point(
        scope_name='__main_____main')
    assert not os.path.exists(expression_file_util.SCOPE_HISTORY_FILE_PATH)
