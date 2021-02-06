from apyscript.expression import expression_scope
from apyscript.expression import expression_file_util
from apyscript.file import file_util


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
