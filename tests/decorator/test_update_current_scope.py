from random import randint
import sys
from types import ModuleType
from typing import List

from retrying import retry

from apyscript.decorator import \
    update_current_scope as update_current_scope_mod
from apyscript.decorator.update_current_scope import _ScopeReverter
from apyscript.decorator.update_current_scope import update_current_scope
from apyscript.expression import expression_scope
from apyscript.expression import expression_file_util
from apyscript.display.stage import Stage
from apyscript.file import file_util
from tests import testing_helper


def test__make_scope_name_from_module_and_func_name() -> None:
    scope_name: str = update_current_scope_mod.\
        _make_scope_name_from_module_and_func_name(
            module_name='any.module.package',
            func_name='get_any_value')
    assert scope_name == 'any___module___package___get_any_value'


this_module: ModuleType = sys.modules[__name__]


@update_current_scope(module=this_module)
def any_func_1(stage: Stage) -> Stage:
    """
    Test function for decorator implementation.

    Parameters
    ----------
    stage : Stage
        Stage instance.

    Returns
    -------
    stage : Stage
        Stage instance.
    """
    return stage



@update_current_scope(module=this_module)
def any_func_2(x: int) -> int:
    """
    Test function for decorator implementation.

    Parameters
    ----------
    x : int
        Any integer value.

    Returns
    -------
    y : int
        Result value.
    """
    return x * 2


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test_update_current_scope() -> None:
    stage: Stage = Stage()
    file_util.remove_file_if_exists(
        file_path=expression_file_util.SCOPE_HISTORY_FILE_PATH)
    expression_scope.update_current_scope(scope_name='test_scope_1')
    stage = any_func_1(stage=stage)
    assert isinstance(stage, Stage)
    scope_history: List[str] = expression_scope.get_scope_history()
    expected: List[str] = [
        'test_scope_1',
        'tests___decorator___test_update_current_scope___any_func_1',
        'test_scope_1',
    ]
    assert scope_history == expected

    current_scope: str = expression_scope.get_current_scope()
    assert current_scope == 'test_scope_1'

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=any_func_2,
        kwargs={'x': 100})


class Test_ScopeReverter:

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test___init__(self) -> None:
        expression_scope.update_current_scope(scope_name='test_scope')
        scope_reverter: _ScopeReverter = _ScopeReverter()
        testing_helper.assert_attrs(
            expected_attrs={
                '_pre_scope': 'test_scope',
            },
            any_obj=scope_reverter)

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_revert(self) -> None:
        expression_scope.update_current_scope(scope_name='test_scope_1')
        scope_reverter: _ScopeReverter = _ScopeReverter()
        expression_scope.update_current_scope(scope_name='test_scope_2')
        scope_reverter.revert()
        current_scope: str = expression_scope.get_current_scope()
        assert current_scope == 'test_scope_1'
