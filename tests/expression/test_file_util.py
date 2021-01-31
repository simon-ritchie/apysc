import os

from retrying import retry

from apyscript.expression import file_util


def test_empty_expression_dir() -> None:
    os.makedirs(file_util.EXPRESSION_ROOT_DIR, exist_ok=True)
    test_file_path: str = os.path.join(
        file_util.EXPRESSION_ROOT_DIR,
        'test_file.txt',
    )
    with open(test_file_path, 'w') as f:
        f.write('\n')
    file_util.empty_expression_dir()
    assert not os.path.exists(test_file_path)
    assert os.path.exists(file_util.EXPRESSION_ROOT_DIR)


@retry(stop_max_attempt_number=5, wait_fixed=300)
def test_append_expression() -> None:
    file_util.empty_expression_dir()

    expected_expression_1: str = (
        '<script>console.log("test")</script>'
    )
    expected_expression_2: str = '<span>test</span>'
    file_util.append_expression(expression=expected_expression_1)
    file_util.append_expression(
        expression=expected_expression_2,
        scope=file_util.ROOT_SCOPE)
    root_scope_file_path:str = file_util.get_scope_file_path_from_scope()
    with open(root_scope_file_path, 'r') as f:
        scope_txt: str = f.read()
    expected_str: str = (
        f'{expected_expression_1}\n{expected_expression_2}\n'
    )
    assert scope_txt == expected_str

    file_util.empty_expression_dir()


def test_get_scope_file_path_from_scope() -> None:
    scope_file_path: str = file_util.get_scope_file_path_from_scope(
        scope=None)
    expected_file_path: str = os.path.join(
        file_util.EXPRESSION_ROOT_DIR,
        f'{file_util.ROOT_SCOPE}.html',
    )
    assert scope_file_path == expected_file_path

    scope_file_path = file_util.get_scope_file_path_from_scope(
        scope='test_scope.html')
    expected_file_path = os.path.join(
        file_util.EXPRESSION_ROOT_DIR,
        'test_scope.html',
    )
    assert scope_file_path == expected_file_path

