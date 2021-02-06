import sys
from types import ModuleType

from apyscript.decorator import \
    update_current_scope as update_current_scope_mod
from apyscript.decorator.update_current_scope import update_current_scope
from apyscript.expression import expression_scope


def test__make_scope_name_from_module_and_func_name() -> None:
    scope_name: str = update_current_scope_mod.\
        _make_scope_name_from_module_and_func_name(
            module_name='any.module.package',
            func_name='get_any_value')
    assert scope_name == 'any___module___package___get_any_value'


this_module: ModuleType = sys.modules[__name__]


@update_current_scope(module=this_module)
def any_func(x: int) -> int:
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


def test_update_current_scope() -> None:
    y: int = any_func(x=100)
    assert y == 200

    current_scope: str = expression_scope.get_current_scope()
    assert current_scope == (
        'tests___decorator___test_update_current_scope'
        '___any_func'
    )
