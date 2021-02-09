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
