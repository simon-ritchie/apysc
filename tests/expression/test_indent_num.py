import os
from random import randint

from retrying import retry

from apysc.expression import indent_num
from apysc.file import file_util
from apysc.expression.expression_file_util import INDENT_NUM_FILE_PATH


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_get_current_indent_num() -> None:
    file_util.remove_file_if_exists(file_path=INDENT_NUM_FILE_PATH)
    current_indent_num: int = indent_num.get_current_indent_num()
    assert current_indent_num == 0

    file_util.save_plain_txt(
        txt='', file_path=INDENT_NUM_FILE_PATH)
    current_indent_num = indent_num.get_current_indent_num()
    assert current_indent_num == 0

    file_util.save_plain_txt(txt=' 2 ', file_path=INDENT_NUM_FILE_PATH)
    current_indent_num = indent_num.get_current_indent_num()
    assert current_indent_num == 2
