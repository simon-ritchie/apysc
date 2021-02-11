from random import randint
from apyscript.file import file_util
import os
from typing import Dict, List

from retrying import retry

from apyscript.expression import expression_file_util
from apyscript.display.stage import Stage
from apyscript.expression import expression_scope
from tests import testing_helper


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
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


@retry(stop_max_attempt_number=5, wait_fixed=300)
def test_append_expression_to_current_scope() -> None:
    expression_scope.update_current_scope(
        scope_name='test___scope')
    expression_file_util.append_expression_to_current_scope(
        expression='<body></body>')
    scope_file_path: str = expression_file_util.\
        get_scope_file_path_from_scope(scope='test___scope')
    expression: str = file_util.read_txt(file_path=scope_file_path)
    assert expression.strip() == '<body></body>'


def test__get_maintaining_files_txt() -> None:
    CURRENT_SCOPE_FILE_PATH: str = \
        expression_file_util.CURRENT_SCOPE_FILE_PATH
    expected: str = 'To be, or not to be, that is the question.'
    file_util.save_plain_txt(
        txt=expected,
        file_path=CURRENT_SCOPE_FILE_PATH)
    maintaining_files_txt: Dict[str, str] = expression_file_util.\
        _get_maintaining_files_txt()
    assert maintaining_files_txt[CURRENT_SCOPE_FILE_PATH] == expected

    os.remove(CURRENT_SCOPE_FILE_PATH)
    maintaining_files_txt = expression_file_util._get_maintaining_files_txt()
    assert CURRENT_SCOPE_FILE_PATH not in maintaining_files_txt


def test__restore_maintaining_files() -> None:
    test_file_path: str = '../.tmp_test_expression_file_util.txt'
    file_util.remove_file_if_exists(file_path=test_file_path)
    expression_file_util._restore_maintaining_files(
        maintaining_files_txt={
            test_file_path: 'To be, or not to be, that is the question.'
        })
    text: str = file_util.read_txt(file_path=test_file_path)
    assert text == 'To be, or not to be, that is the question.'


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test_remove_current_scope_expression_file() -> None:
    expression_scope.update_current_scope(
        scope_name='test_expression_file_util')
    file_path: str = expression_file_util.\
        get_current_scope_expression_file_path()
    expression_file_util.append_expression_to_current_scope(
        expression='<body></body>')
    assert os.path.isfile(file_path)
    expression_file_util.remove_current_scope_expression_file()
    assert not os.path.exists(file_path)


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test_get_current_scope_expression_file_path() -> None:
    expression_scope.update_current_scope(
        scope_name='test_expression_file_util')
    file_path: str = expression_file_util.\
        get_current_scope_expression_file_path()
    expected: str = os.path.join(
        expression_file_util.EXPRESSION_ROOT_DIR,
        'test_expression_file_util.html'
    )
    assert file_path == expected


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test_get_current_scope_expression() -> None:
    expression_scope.update_current_scope(
        scope_name='test_expression_file_util')
    expression_file_util.remove_current_scope_expression_file()
    expression_file_util.append_expression_to_current_scope(
        '<body></body>'
    )
    expression: str = expression_file_util.get_current_scope_expression()
    assert expression == '<body></body>'
    expression_file_util.remove_current_scope_expression_file()
