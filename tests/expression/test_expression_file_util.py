import os
from random import randint
from typing import Dict
from typing import List

from retrying import retry

from apyscript.display.stage import Stage
from apyscript.expression import expression_file_util
from apyscript.file import file_util
from apyscript.html import html_const
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

    expected_expression_1: str = '<body>'
    expression_file_util.append_expression(expression=expected_expression_1)
    expected_expression_2: str = '<span>test</span>'
    expression_file_util.append_expression(
        expression=expected_expression_2)
    expected_expression_3: str = (
        f'{html_const.SCRIPT_START_TAG}'
        '\nconsole.log("Hello ");'
        f'\n{html_const.SCRIPT_END_TAG}'
        f'\n{html_const.SCRIPT_START_TAG}'
        '\nconsole.log("World!");'
        f'\n{html_const.SCRIPT_END_TAG}'
    )
    expression_file_util.append_expression(
        expression=expected_expression_3)
    with open(expression_file_util.EXPRESSION_FILE_PATH, 'r') as f:
        expression_txt: str = f.read()
    expected_str: str = (
        f'{expected_expression_1}\n{expected_expression_2}\n'
    )
    assert expression_txt.startswith(expected_str)
    expected_str = (
        '\nconsole.log("Hello ");'
        '\nconsole.log("World!");'
    )
    assert expected_str in expression_txt

    expression_file_util.empty_expression_dir()


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test_remove_expression_file() -> None:
    expression_file_util.append_expression(
        expression='<body></body>')
    assert os.path.isfile(expression_file_util.EXPRESSION_FILE_PATH)
    expression_file_util.remove_expression_file()
    assert not os.path.exists(expression_file_util.EXPRESSION_FILE_PATH)


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test_get_current_expression() -> None:
    expression_file_util.remove_expression_file()
    expression_file_util.append_expression(
        '<body></body>'
    )
    expression: str = expression_file_util.get_current_expression()
    assert expression == '<body></body>'
    expression_file_util.remove_expression_file()

    expression = expression_file_util.get_current_expression()
    assert expression == ''


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test__merge_script_section() -> None:
    expression_file_util.remove_expression_file()
    expression_file_util.append_expression(
        '<body>'
        f'\n{html_const.SCRIPT_START_TAG}'
        '\nconsole.log("Hello ");'
        '\n'
        '\n'
        f'{html_const.SCRIPT_END_TAG}'
        '\n</body>'
    )
    expression_file_util.append_expression(
        f'{html_const.SCRIPT_START_TAG}'
        '\nconsole.log("World!");'
        '\n'
        f'{html_const.SCRIPT_END_TAG}'
    )
    expression_file_util._merge_script_section()
    expression: str = expression_file_util.get_current_expression()
    expected: str = (
        '<body>'
        '\n</body>'
        f'\n{html_const.SCRIPT_START_TAG}'
        '\nconsole.log("Hello ");'
        '\nconsole.log("World!");'
        f'\n{html_const.SCRIPT_END_TAG}'
    )
    assert expression == expected

    expression_file_util.remove_expression_file()
