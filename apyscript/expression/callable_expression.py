"""Function or method expression (switch of scope) utility
implementations.
"""

from typing import Any, Callable, Dict, Tuple

from apyscript.validation import expression_arg_validation
from apyscript.callable import callable_util
from apyscript.display.variable_name_interface import VariableNameInterface
from apyscript.expression import expression_variables_util
from apyscript.html import html_util


def get_function_call_expression(
        scope_name: str, func: Callable, args: list, kwargs: dict,
        returned_val: Any) -> str:
    """
    Get a function call js expression.

    Parameters
    ----------
    scope_name : str
        Target function (or method)'s scope name.
    func : Callable
        Target function or method.
    args : list
        Positional arguments to be specified target function.
    kwargs : dict
        Keyword arguments to be specified target function.
    returned_val : *
        Returned value(s).

    Returns
    -------
    expression : str
        Created expression's string.
    """
    expression_arg_validation.validate_acceptable_arg_types(
        args=args, kwargs=kwargs)
    expression_arg_validation.validate_default_values_not_exist(func=func)
    expression_arg_validation.validate_acceptable_return_types(
        returned_val=returned_val)
    args_dict: Dict[str, VariableNameInterface] = callable_util.\
        get_name_and_arg_value_dict_from_args(
            func=func, args=args, kwargs=kwargs)
    expression: str = ''
    arg_var_name: str
    return_var_name: str
    expression, arg_var_name = _append_args_expression_to_str(
        expression=expression, args_dict=args_dict)
    expression, return_var_name = _append_func_call_expression_to_str(
        scope_name=scope_name, expression=expression,
        arg_var_name=arg_var_name)
    expression = html_util.wrap_expression_by_script_tag(
        expression=expression)
    return expression


ARG_VAR_TYPE_NAME: str = 'arg_dict'
RETURN_VAR_TYPE_NAME: str = 'return_dict'


def _append_func_call_expression_to_str(
        scope_name: str, expression: str,
        arg_var_name: str) -> Tuple[str, str]:
    """
    Append function call js expression to string.

    Parameters
    ----------
    scope_name : str
        Target function (or method)'s scope name.
    expression : str
        String to be appended expression.
    arg_var_name : str
        Dict (js Object) argument variable name.

    Returns
    -------
    expression : str
        After appending expression string.
    return_var_name : str
        Return variable (js Object) name to be used in expression.
    """
    return_var_name: str = expression_variables_util.get_next_variable_name(
        type_name=RETURN_VAR_TYPE_NAME)
    expression += (
        f'var {return_var_name} = {scope_name}({arg_var_name});\n'
    )
    return expression, return_var_name


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
        Argument variable (js Object) name to be used in expression.
    """
    arg_var_name: str = expression_variables_util.get_next_variable_name(
        type_name=ARG_VAR_TYPE_NAME)
    expression += f'var {arg_var_name} = {{'
    for arg_name, arg_value in args_dict.items():
        expression += f'\n  "{arg_name}": {arg_value.variable_name},'
    expression += '\n};\n'
    return expression, arg_var_name
