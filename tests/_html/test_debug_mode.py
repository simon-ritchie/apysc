import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._expression import expression_file_util
from apysc._file import file_util
from apysc._html import debug_mode
from tests.testing_helper import assert_attrs


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_set_debug_mode() -> None:
    stage: ap.Stage = ap.Stage()
    ap.set_debug_mode(stage=stage)
    assert debug_mode.is_debug_mode()


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_debug_mode() -> None:
    stage: ap.Stage = ap.Stage()
    result: bool = ap.is_debug_mode()
    assert not result

    ap.set_debug_mode(stage=stage)
    result = ap.is_debug_mode()
    assert result

    ap.unset_debug_mode()
    result = ap.is_debug_mode()
    assert not result


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
        import os
        os_var = os  # noqa
        stage: ap.Stage = ap.Stage()
        with ap.DebugInfo(
                callable_=self.test___init__, locals_=locals(),
                module_name=__name__, class_=TestDebugInfo):
            pass
        expression: str = expression_file_util.get_current_expression()
        assert f'\n// [{self.test___init__.__name__}' not in expression

        ap.set_debug_mode(stage=stage)
        __any_val__: str = 'Hello'
        blank_str: str = ''  # noqa
        with_break_str: str = 'a\nb'  # noqa
        int_val: ap.Int = ap.Int(10)
        with ap.DebugInfo(
                callable_=self.test___init__, locals_=locals(),
                module_name=__name__, class_=TestDebugInfo):
            pass
        expression = expression_file_util.get_current_expression()
        assert f'\n// [{self.test___init__.__name__}' in expression
        assert f'\n// module name: {__name__}' in expression
        assert f'\n// class: {TestDebugInfo.__name__}' in expression
        assert '\n// arguments and variables:' in expression
        assert '\n//    self ='
        assert "\n//    blank_str = ''"
        assert '\n//    a\nb'
        assert f"\n//    int_val = 10({int_val.variable_name})"

        expression_file_util.empty_expression()
        ap.set_debug_mode(stage=stage)
        with ap.DebugInfo(
                callable_=self.test___init__, locals_={},
                module_name=__name__, class_=TestDebugInfo):
            pass
        expression = expression_file_util.get_current_expression()
        assert '\n// arguments and variables:' not in expression

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
        stage: ap.Stage = ap.Stage()
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

        ap.set_debug_mode(stage=stage)
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
def test__get_callable_count() -> None:
    expression_file_util.empty_expression()
    callable_count: int = debug_mode._get_callable_count(
        callable_=TestDebugInfo.test___init__,
        module_name=__name__,
        class_=TestDebugInfo)
    assert callable_count == 0

    for _ in range(2):
        debug_mode._increment_callable_count(
            callable_=TestDebugInfo.test___init__,
            module_name=__name__,
            class_=TestDebugInfo)
    callable_count = debug_mode._get_callable_count(
        callable_=TestDebugInfo.test___init__,
        module_name=__name__,
        class_=TestDebugInfo)
    assert callable_count == 2


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__increment_callable_count() -> None:
    expression_file_util.empty_expression()
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


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_unset_debug_mode() -> None:
    stage: ap.Stage = ap.Stage()
    ap.set_debug_mode(stage=stage)
    assert ap.is_debug_mode()
    ap.unset_debug_mode()
    assert not ap.is_debug_mode()


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_callable_path_name() -> None:
    path_name: str = debug_mode._get_callable_path_name(
        callable_=TestDebugInfo.test___init__,
        module_name=__name__,
        class_=TestDebugInfo)
    assert path_name == \
        'tests__html_test_debug_mode_TestDebugInfo_test___init__'

    path_name: str = debug_mode._get_callable_path_name(
        callable_=TestDebugInfo.test___init__,
        module_name=__name__)
    assert path_name == \
        'tests__html_test_debug_mode_test___init__'
