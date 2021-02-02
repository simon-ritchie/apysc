import os
from typing import List

from retrying import retry

from apyscript.expression import expression_file_util
from apyscript.display.stage import Stage
from tests import testing_helper


def test_empty_expression_dir() -> None:
    os.makedirs(expression_file_util.EXPRESSION_ROOT_DIR, exist_ok=True)
    test_file_path: str = os.path.join(
        expression_file_util.EXPRESSION_ROOT_DIR,
        'test_file.txt',
    )
    with open(test_file_path, 'w') as f:
        f.write('\n')
    expression_file_util.empty_expression_dir()
    assert not os.path.exists(test_file_path)
    assert os.path.exists(expression_file_util.EXPRESSION_ROOT_DIR)


@retry(stop_max_attempt_number=5, wait_fixed=300)
def test_append_expression() -> None:
    expression_file_util.empty_expression_dir()

    expected_expression_1: str = (
        '<script>console.log("test")</script>'
    )
    expected_expression_2: str = '<span>test</span>'
    expression_file_util.append_expression(expression=expected_expression_1)
    expression_file_util.append_expression(
        expression=expected_expression_2,
        scope=expression_file_util.ROOT_SCOPE)
    root_scope_file_path: str = \
        expression_file_util.get_scope_file_path_from_scope()
    with open(root_scope_file_path, 'r') as f:
        scope_txt: str = f.read()
    expected_str: str = (
        f'{expected_expression_1}\n{expected_expression_2}\n'
    )
    assert scope_txt == expected_str

    expression_file_util.empty_expression_dir()


def test_get_scope_file_path_from_scope() -> None:
    scope_file_path: str = \
        expression_file_util.get_scope_file_path_from_scope(
            scope=None)
    expected_file_path: str = os.path.join(
        expression_file_util.EXPRESSION_ROOT_DIR,
        f'{expression_file_util.ROOT_SCOPE}.html',
    )
    assert scope_file_path == expected_file_path

    scope_file_path = expression_file_util.get_scope_file_path_from_scope(
        scope='test_scope.html')
    expected_file_path = os.path.join(
        expression_file_util.EXPRESSION_ROOT_DIR,
        'test_scope.html',
    )
    assert scope_file_path == expected_file_path


@retry(stop_max_attempt_number=5, wait_fixed=300)
def test_get_expression_file_paths() -> None:
    Stage()
    test_text_file_path: str =os.path.join(
        expression_file_util.EXPRESSION_ROOT_DIR,
        'test_expression_file_util.txt',
    )
    testing_helper.make_blank_file(
        file_path=test_text_file_path)
    expression_file_paths: List[str] = \
        expression_file_util.get_expression_file_paths()

    assert test_text_file_path not in expression_file_paths
    for expression_file_path in expression_file_paths:
        assert expression_file_path.endswith('.html')
