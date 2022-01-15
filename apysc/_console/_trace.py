"""`trace` (console.log expression) interface implementations
"""

from typing import Any
from typing import List


def trace(*args: Any) -> None:
    """
    Display arguments information to console. This function will
    save js `console.log` expression.

    Parameters
    ----------
    *args : list
        Any arguments to display to console.

    References
    ----------
    - Trace interface document
        - https://simon-ritchie.github.io/apysc/trace.html

    Examples
    --------
    >>> import apysc as ap
    >>> int_val: ap.Int = ap.Int(10)
    >>> ap.trace('Int value is:', int_val)
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=trace, locals_=locals(),
            module_name=__name__):
        from apysc._string import string_util
        from apysc._type.variable_name_interface import VariableNameInterface

        expression: str = 'console.log('
        arg_strs: List[str] = []
        for arg in args:
            if isinstance(arg, VariableNameInterface):
                arg_strs.append(f'{arg.variable_name}')
                continue
            arg = string_util.escape_str(string=str(arg))
            arg_strs.append(f'"{arg}"')
        expression += ', '.join(arg_strs)
        expression += ');'
        ap.append_js_expression(expression=expression)
