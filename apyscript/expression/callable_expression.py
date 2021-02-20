"""Function or method expression (switch of scope) utility
implementations.
"""

from typing import Any, Callable, Dict, Tuple

from apyscript.validation import expression_arg_validation
from apyscript.callable import callable_util
from apyscript.display.variable_name_interface import VariableNameInterface
from apyscript.expression import expression_variables_util


def get_function_call_expression(
        func: Callable, args: list, kwargs: dict) -> str:
    """
    Get a function call js expression.

    Parameters
    ----------
    func : Callable
        Target function or method.
    args : list
        Positional arguments to be specified target function.
    kwargs : dict
        Keyword arguments to be specified target function.

    Returns
    -------
    expression : str
        Created expression's string.
    """
    expression_arg_validation.validate_acceptable_arg_types(
        args=args, kwargs=kwargs)
    expression_arg_validation.validate_default_values_not_exist(func=func)
    args_dict: Dict[str, VariableNameInterface] = callable_util.\
        get_name_and_arg_value_dict_from_args(
            func=func, args=args, kwargs=kwargs)
    expression: str = ''
    arg_var_name: str
    expression, arg_var_name = _append_args_expression_to_str(
        expression=expression, args_dict=args_dict)
    pass


ARG_VAR_TYPE_NAME: str = 'arg_dict'


def _append_args_expression_to_str(
        expression: str,
        args_dict: Dict[str, VariableNameInterface]) -> Tuple[str, str]:
    """
    Append arguments defining expression to string.

    Parameters
    ----------
    expression : str
        String to be appended expression.
    args_dict : dict
        Dictionary that has argument names at key and specified values
        at value.

    Returns
    -------
    expression : str
        After appending expression string.
    arg_var_name : str
        Argument name (js Object) to be used in expression.
    """
    arg_var_name: str = expression_variables_util.get_next_variable_name(
        type_name=ARG_VAR_TYPE_NAME)
    expression += f'var {arg_var_name} = {{'
    for arg_name, arg_value in args_dict.items():
        expression += f'\n  "{arg_name}": {arg_value.variable_name}'
    expression += '\n};\n'
    return expression, arg_var_name
