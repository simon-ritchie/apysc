from typing import List
from apyscript.file import file_util
from retrying import retry

from apyscript.expression import scope_variables_util
from apyscript.expression import expression_file_util
from apyscript.expression import expression_scope


@retry(stop_max_attempt_number=5, wait_fixed=300)
def test_get_current_scope_variable_names_file_path() -> None:
    expression_scope.update_current_scope(
        scope_name='test_scope_variables_util')
    file_path: str = scope_variables_util.\
        get_current_scope_variable_names_file_path(type_name='sprite')
    assert file_path.startswith(expression_file_util.EXPRESSION_ROOT_DIR)
    assert '_test_scope_variables_util_' in file_path
    assert file_path.endswith('_sprite.txt')


def test__read_current_scope_variable_names() -> None:
    expression_scope.update_current_scope(
        scope_name='test_scope_variables_util')
    file_path: str = scope_variables_util.\
        get_current_scope_variable_names_file_path(type_name='sprite')
    file_util.save_plain_txt(
        txt='sprite_1,sprite_2,sprite_3,', file_path=file_path)
    variable_names: List[str] = scope_variables_util.\
        _read_current_scope_variable_names(type_name='sprite')
    assert variable_names == ['sprite_1', 'sprite_2', 'sprite_3']

    file_util.remove_file_if_exists(file_path=file_path)


def test__get_current_scope_next_variable_num() -> None:
    expression_scope.update_current_scope(
        scope_name='test_scope_variables_util')
    file_path: str = scope_variables_util.\
        get_current_scope_variable_names_file_path(type_name='sprite')
    file_util.remove_file_if_exists(file_path=file_path)
    next_variable_num: int = scope_variables_util.\
        _get_current_scope_next_variable_num(type_name='sprite')
    assert next_variable_num == 1

    file_util.save_plain_txt(
        txt='sprite_1,sprite_2,', file_path=file_path)
    next_variable_num = scope_variables_util.\
        _get_current_scope_next_variable_num(type_name='sprite')
    assert next_variable_num == 3

    file_util.remove_file_if_exists(file_path=file_path)
