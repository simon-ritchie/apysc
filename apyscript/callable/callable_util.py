"""Common callable utility implementations.
"""

import inspect
from inspect import Signature, Parameter
from typing import Any, Callable, Dict

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
    signature: Signature = inspect.signature(func)
    default_vals: Dict[str, Any] = {}
    parameter: Parameter
    for arg_name, parameter in signature.parameters.items():
        default_vals[arg_name] = parameter.default
    return default_vals
