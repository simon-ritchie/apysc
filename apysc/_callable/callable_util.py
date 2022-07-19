"""Typical callable utility implementations.
"""

import inspect
from inspect import Parameter
from inspect import Signature
from typing import Any
from typing import Callable
from typing import Dict

from apysc._html.debug_mode import add_debug_info_setting

empty = inspect.Signature.empty


@add_debug_info_setting(module_name=__name__)
def get_func_default_vals(*, func: Callable) -> Dict[str, Any]:
    """
    Get specified function's arguments default values.

    Parameters
    ----------
    func : Callable
        Target function (or method).

    Returns
    -------
    default_vals : dict
        Dictionary with an argument name at key and
        default value at value. This interface sets the
        `empty` object if an argument has no default value.
    """
    signature: Signature = inspect.signature(func)
    default_vals: Dict[str, Any] = {}
    parameter: Parameter
    for arg_name, parameter in signature.parameters.items():
        default_vals[arg_name] = parameter.default
    return default_vals


@add_debug_info_setting(module_name=__name__)
def get_arg_name_at(*, func: Callable, index: int) -> str:
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
    signature: Signature = inspect.signature(func)
    arg_name: str = ""
    for i, target_idx_arg_name in enumerate(signature.parameters.keys()):
        if i != index:
            continue
        arg_name = target_idx_arg_name
        break
    return arg_name


@add_debug_info_setting(module_name=__name__)
def get_name_and_arg_value_dict_from_args(
    *, func: Callable, args: list, kwargs: dict
) -> Dict[str, Any]:
    """
    Get a dictionary with an argument name at key and
    specified argument values at value.

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
    name_and_arg_value_dict: Dict[str, Any] = {}
    for i, arg_value in enumerate(args):
        arg_name: str = get_arg_name_at(func=func, index=i)
        name_and_arg_value_dict[arg_name] = arg_value
    name_and_arg_value_dict.update(kwargs)
    return name_and_arg_value_dict


@add_debug_info_setting(module_name=__name__)
def get_method_class_name(*, method: Callable) -> str:
    """
    Get a specified method's class name.

    Parameters
    ----------
    method : Callable
        Target method.

    Returns
    -------
    class_name : str
        Target method's class name. This interface
        returns a blank string if a specified argument
        is not a method (e.g., function).
    """
    if not inspect.ismethod(method):
        return ""
    class_name: str = ""
    for class_ in inspect.getmro(type(method.__self__)):  # type: ignore
        if method.__name__ not in class_.__dict__:
            continue
        class_name = class_.__name__
    return class_name
