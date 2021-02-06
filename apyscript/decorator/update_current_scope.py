"""Decorator implementation to update current expression's scope.
"""

from typing import Any, Callable
from types import ModuleType
from functools import wraps

from apyscript.expression import expression_scope


def update_current_scope(module: ModuleType) -> Callable:
    """
    Decorator function to update current expression's scope name.

    Parameters
    ----------
    module : ModuleType
        The module that using this decorator.

    Returns
    -------
    decorator_func : Callable
        A function to be used as decorator.
    """

    def decorator_func(func: Callable) -> Callable:

        @wraps(func)
        def inner_decorator_func(*args, **kwargs) -> Any:
            scope_name: str = _make_scope_name_from_module_and_func_name(
                module_name=module.__name__,
                func_name=func.__name__)
            result: Any = func(*args, **kwargs)
            return result

        return inner_decorator_func

    return decorator_func


def _make_scope_name_from_module_and_func_name(
        module_name: str, func_name: str) -> str:
    """
    Make scope name from specified module and function's name.

    Parameters
    ----------
    module_name : str
        Module name that concatenated package path by comma.
        e.g., 'any.module.name'
    func_name : str
        Function name.

    Returns
    -------
    scope_name : str
        Scope name that module name's comma replaced by double underscore
        and also concatenated function name.
        e.g., 'any__module__name__function_name'.
    """
    module_name = module_name.replace('.', '__')
    scope_name: str = f'{module_name}__{func_name}'
    return scope_name
