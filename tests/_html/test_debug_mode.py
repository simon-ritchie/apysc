from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import expression_file_util
from apysc._file import file_util
from tests.testing_helper import assert_attrs
from apysc._html import debug_mode
from apysc._expression import expression_file_util


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


class TestDebugInfo:

    def test___init__(self) -> None:
        debug_info: ap.DebugInfo = ap.DebugInfo(
            callable_=self.test___init__,
            locals_=locals(),
            module_name=__name__,
            class_=TestDebugInfo)
        assert_attrs(
            expected_attrs={
                '_callable': self.test___init__,
                '_locals': {'self': self},
                '_module_name': __name__,
                '_class': TestDebugInfo,
            },
            any_obj=debug_info,
        )


def test__get_callable_count_file_path() -> None:
    file_path: str = debug_mode._get_callable_count_file_path(
        callable_=TestDebugInfo.test___init__,
        module_name=__name__,
        class_=TestDebugInfo)
    assert file_path.startswith(expression_file_util.EXPRESSION_ROOT_DIR)
    assert 'tests__html_test_debug_mode' in file_path
    assert 'TestDebugInfo' in file_path
    assert 'test___init__' in file_path
