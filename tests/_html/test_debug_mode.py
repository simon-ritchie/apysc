from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import expression_file_util
from apysc._file import file_util


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_set_debug_mode() -> None:
    expression_file_util.empty_expression_dir()
    ap.set_debug_mode()
    with open(expression_file_util.DEBUG_MODE_SETTING_FILE_PATH) as f:
        txt: str = f.read()
    assert txt == '1'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_debug_mode() -> None:
    expression_file_util.empty_expression_dir()
    result: bool = ap.is_debug_mode()
    assert not result

    file_util.append_plain_txt(
        txt='',
        file_path=expression_file_util.DEBUG_MODE_SETTING_FILE_PATH)
    result = ap.is_debug_mode()
    assert not result

    ap.set_debug_mode()
    result = ap.is_debug_mode()
    assert result
