import os
from random import randint
import re
from typing import Match, Optional

from retrying import retry

from apysc.expression import expression_file_util
from apysc.expression import indent_num
from apysc.html import html_const
from apysc.html import html_util


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
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


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_remove_expression_file() -> None:
    expression_file_util.append_js_expression(
        expression='console.log("Hello!");')
    assert os.path.isfile(expression_file_util.EXPRESSION_FILE_PATH)
    expression_file_util.remove_expression_file()
    assert not os.path.exists(expression_file_util.EXPRESSION_FILE_PATH)


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_get_current_expression() -> None:
    expression_file_util.remove_expression_file()
    expression_file_util.append_js_expression(
        'console.log("Hello!");'
    )
    expression: str = expression_file_util.get_current_expression()
    assert expression == 'console.log("Hello!");'
    expression_file_util.remove_expression_file()

    expression = expression_file_util.get_current_expression()
    assert expression == ''


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_wrap_by_script_tag_and_append_expression() -> None:
    indent_num.reset()
    expression_file_util.remove_expression_file()
    expression_file_util.append_js_expression(expression='var num = 100;')
    expression: str = expression_file_util.get_current_expression()
    expected: str = 'var num = 100;'
    assert expected in expression
    assert html_const.SCRIPT_START_TAG in expression
    assert html_const.SCRIPT_END_TAG in expression


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_append_js_expression() -> None:
    indent_num.reset()
    expression_file_util.remove_expression_file()
    expression_file_util.append_js_expression(expression='var num = 100;')
    expression: str = expression_file_util.get_current_expression()
    match: Optional[Match] = re.search(
        pattern=r'^var num = 100;',
        string=expression,
        flags=re.MULTILINE)
    assert match is not None

    expression_file_util.remove_expression_file()
    indent_num.increment()
    expression_file_util.append_js_expression(
        expression='var num_1 = 100;\nvar num_2 = 200;\nvar num_3 = 300;')
    expression = expression_file_util.get_current_expression()
    match: Optional[Match] = re.search(
        pattern=r'^  var num_2 = 200;',
        string=expression,
        flags=re.MULTILINE)
