from apyscript.expression import core
from apyscript.expression import expression_file_util
from apyscript.file import file_util


def test_update_current_scope() -> None:
    core.update_current_scope(scope_name='main__main')
    current_scope: str = file_util.read_txt(
        file_path=expression_file_util.CURRENT_SCOPE_FILE_PATH)
    assert current_scope == 'main__main'
