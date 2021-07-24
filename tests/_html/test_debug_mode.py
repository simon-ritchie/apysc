from random import randint
from typing import Match, Optional
import re

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

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
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

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___enter__(self) -> None:
        import os  # noqa
        expression_file_util.empty_expression_dir()
        with ap.DebugInfo(
                callable_=self.test___init__, locals_=locals(),
                module_name=__name__, class_=TestDebugInfo):
            pass
        expression: str = expression_file_util.get_current_expression()
        assert f'\n// [{self.test___init__.__name__}' not in expression

        ap.set_debug_mode()
        __any_val__: str = 'Hello'
        blank_str: str = ''  # noqa
        int_val: ap.Int = ap.Int(10)
        with ap.DebugInfo(
                callable_=self.test___init__, locals_=locals(),
                module_name=__name__, class_=TestDebugInfo):
            pass
        expression = expression_file_util.get_current_expression()
        assert f'\n// [{self.test___init__.__name__}' in expression
        assert f'\n// module name: {__name__}' in expression
        assert f'\n// class: {TestDebugInfo.__name__}' in expression
        assert f'\n// arguments and variables:' in expression
        assert f'\n//    self ='
        assert f"\n//    blank_str = ''"
        assert f"\n//    int_val = 10({int_val.variable_name})"

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_class_info(self) -> None:
        debug_info: ap.DebugInfo = ap.DebugInfo(
            callable_=self.test___init__,
            locals_=locals(),
            module_name=__name__,
            class_=TestDebugInfo)
        class_info: str = debug_info._get_class_info()
        assert class_info == f'\n// class: {TestDebugInfo.__name__}'

        debug_info = ap.DebugInfo(
            callable_=self.test___init__,
            locals_=locals(),
            module_name=__name__,
        )
        class_info = debug_info._get_class_info()
        assert class_info == ''

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___exit__(self) -> None:
        expression_file_util.empty_expression_dir()
        with ap.DebugInfo(
                callable_=self.test___init__, locals_=locals(),
                module_name=__name__, class_=TestDebugInfo):
            pass
        expression: str = expression_file_util.get_current_expression()
        callable_name: str = self.test___init__.__name__
        match: Optional[Match] = re.search(
            pattern=(
                rf'// \[{callable_name} .+?\] ended\.'
            ),
            string=expression, flags=re.MULTILINE | re.DOTALL)
        assert match is None

        ap.set_debug_mode()
        with ap.DebugInfo(
                callable_=self.test___init__, locals_=locals(),
                module_name=__name__, class_=TestDebugInfo):
            pass
        expression = expression_file_util.get_current_expression()
        match = re.search(
            pattern=(
                rf'// \[{callable_name} .+?\] ended\.'
            ),
            string=expression, flags=re.MULTILINE | re.DOTALL)
        assert match is not None


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_callable_count_file_path() -> None:
    file_path: str = debug_mode._get_callable_count_file_path(
        callable_=TestDebugInfo.test___init__,
        module_name=__name__,
        class_=TestDebugInfo)
    assert file_path.startswith(expression_file_util.EXPRESSION_ROOT_DIR)
    assert 'tests__html_test_debug_mode' in file_path
    assert 'TestDebugInfo' in file_path
    assert 'test___init__' in file_path

    _ = debug_mode._get_callable_count_file_path(
        callable_=TestDebugInfo.test___init__,
        module_name=__name__)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_callable_count() -> None:
    expression_file_util.empty_expression_dir()
    callable_count: int = debug_mode._get_callable_count(
        callable_=TestDebugInfo.test___init__,
        module_name=__name__,
        class_=TestDebugInfo)
    assert callable_count == 0

    file_path: str = debug_mode._get_callable_count_file_path(
        callable_=TestDebugInfo.test___init__,
        module_name=__name__,
        class_=TestDebugInfo)
    file_util.append_plain_txt(txt='', file_path=file_path)
    callable_count = debug_mode._get_callable_count(
        callable_=TestDebugInfo.test___init__,
        module_name=__name__,
        class_=TestDebugInfo)
    assert callable_count == 0

    file_util.append_plain_txt(txt='3', file_path=file_path)
    callable_count = debug_mode._get_callable_count(
        callable_=TestDebugInfo.test___init__,
        module_name=__name__,
        class_=TestDebugInfo)
    assert callable_count == 3


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__increment_callable_count() -> None:
    expression_file_util.empty_expression_dir()
    debug_mode._increment_callable_count(
        callable_=TestDebugInfo.test___init__,
        module_name=__name__,
        class_=TestDebugInfo)
    callable_count: int = debug_mode._get_callable_count(
        callable_=TestDebugInfo.test___init__,
        module_name=__name__,
        class_=TestDebugInfo)
    assert callable_count == 1


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_callable_str() -> None:
    callable_str: str = debug_mode._get_callable_str(
        callable_=test__get_callable_str)
    assert callable_str == 'test__get_callable_str'

    callable_str = debug_mode._get_callable_str(callable_='any_func')
    assert callable_str == 'any_func'
