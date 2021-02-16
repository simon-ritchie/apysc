"""Decorator implementation to update current expression's scope.
"""

from functools import wraps
from types import ModuleType
from typing import Any
from typing import Callable

from apyscript.expression import expression_scope
from apyscript.validation import expression_arg_validation


class _ScopeReverter:

    _pre_scope: str = ''

    def __init__(self) -> None:
        """
        Class to revert scope when function's call ended.
        """
        self._pre_scope = expression_scope.get_current_scope()

    def revert(self) -> None:
        """
        Revert current scope to pre-scope.
        """
        expression_scope.update_current_scope(
            scope_name=self._pre_scope)


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
        """
        Decorator function to return wrapped callable.

        Parameters
        ----------
        func : Callable
            Function to wrap.

        Returns
        -------
        result : Callable
            Wrapped callable.
        """

        @wraps(func)
        def inner_decorator_func(*args: list, **kwargs: dict) -> Any:
            """
            Decorator function to handle specified function's call.

            Parameters
            ----------
            *args : list
                Any arguments.
            **kwargs : dict
                Any keyword arguments.

            Returns
            -------
            result : *
                Any returned value to be got from function's call.
            """
            expression_arg_validation.validate_acceptable_arg_types(
                args=args,  # type: ignore
                kwargs=kwargs)
            scope_reverter: _ScopeReverter = _ScopeReverter()
            scope_name: str = _make_scope_name_from_module_and_func_name(
                module_name=module.__name__,
                func_name=func.__name__)
            expression_scope.update_current_scope(scope_name=scope_name)
            result: Any = func(*args, **kwargs)
            scope_reverter.revert()
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
        Scope name that module name's comma replaced by triple underscore
        and also concatenated function name.
        e.g., 'any___module___name___function_name'.
    """
    module_name = module_name.replace('.', '___')
    scope_name: str = f'{module_name}___{func_name}'
    return scope_name
