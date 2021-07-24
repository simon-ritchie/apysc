"""Common callable utility implementations.
"""

import inspect
from inspect import Parameter
from inspect import Signature
from typing import Any
from typing import Callable
from typing import Dict

empty = inspect.Signature.empty


def get_func_default_vals(func: Callable) -> Dict[str, Any]:
    """
    Get specified function's arguments default values.

    Parameters
    ----------
    func : Callable
        Target function (or method).

    Returns
    -------
    default_vals : dict
        Dictionary that has a argument name at key and default value
        at value. If argument has no default value, then `empty` object
        will be set.
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=get_func_default_vals, locals_=locals(),
            module_name=__name__):
        signature: Signature = inspect.signature(func)
        default_vals: Dict[str, Any] = {}
        parameter: Parameter
        for arg_name, parameter in signature.parameters.items():
            default_vals[arg_name] = parameter.default
        return default_vals


def get_arg_name_at(func: Callable, index: int) -> str:
    """
    Get specified index argument name from function.

    Parameters
    ----------
    func : Callable
        Target function (or method).
    index : int
        Argument index (start from 0).

    Returns
    -------
    arg_name : str
        Target index's argument name.
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=get_arg_name_at, locals_=locals(),
            module_name=__name__):
        signature: Signature = inspect.signature(func)
        arg_name: str = ''
        for i, target_idx_arg_name in enumerate(signature.parameters.keys()):
            if i != index:
                continue
            arg_name = target_idx_arg_name
            break
        return arg_name


def get_name_and_arg_value_dict_from_args(
        func: Callable, args: list, kwargs: dict) -> Dict[str, Any]:
    """
    Get dictionary that has an argument name at key and specified
    argument values at value.

    Parameters
    ----------
    func : Callable
        Target function (or method).
    args : list
        Specified positional arguments.
    kwargs : dict
        Specified keyword arguments.

    Returns
    -------
    name_and_arg_value_dict : dict
        Dictionary that has an argument name at key and specified
        argument values at value.
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=get_name_and_arg_value_dict_from_args, locals_=locals(),
            module_name=__name__):
        name_and_arg_value_dict: Dict[str, Any] = {}
        for i, arg_value in enumerate(args):
            arg_name: str = get_arg_name_at(func=func, index=i)
            name_and_arg_value_dict[arg_name] = arg_value
        name_and_arg_value_dict.update(kwargs)
        return name_and_arg_value_dict


def get_method_class_name(method: Callable) -> str:
    """
    Get a specified method's class name.

    Parameters
    ----------
    method : Callable
        Target method.

    Returns
    -------
    class_name : str
        Target method's class name. If specified argument is
        not a method (e.g., function), then blank string will be
        returned.
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=get_method_class_name, locals_=locals(),
            module_name=__name__):
        if not inspect.ismethod(method):
            return ''
        class_name: str = ''
        for class_ in inspect.getmro(type(method.__self__)):  # type: ignore
            if method.__name__ not in class_.__dict__:
                continue
            class_name = class_.__name__
        return class_name
