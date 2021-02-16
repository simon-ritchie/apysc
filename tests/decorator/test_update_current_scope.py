import sys
from types import ModuleType

from retrying import retry

from apyscript.decorator import \
    update_current_scope as update_current_scope_mod
from apyscript.decorator.update_current_scope import update_current_scope
from apyscript.expression import expression_scope
from apyscript.display.stage import Stage
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


@retry(stop_max_attempt_number=5, wait_fixed=300)
def test_update_current_scope() -> None:
    stage: Stage = Stage()
    stage = any_func_1(stage=stage)
    assert isinstance(stage, Stage)

    current_scope: str = expression_scope.get_current_scope()
    assert current_scope == (
        'tests___decorator___test_update_current_scope'
        '___any_func_1'
    )

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=any_func_2,
        kwargs={'x': 100})
