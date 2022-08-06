"""`trace` (console.log expression) interface implementations
"""

import inspect
from inspect import FrameInfo
from types import FrameType
from typing import Any
from typing import List
from typing import Optional

from apysc._html.debug_mode import add_debug_info_setting


@add_debug_info_setting(module_name=__name__)
def trace(*args: Any) -> None:
    """
    Display arguments information to console.
    This function saves a JavaScript `console.log` expression.

    Parameters
    ----------
    *args : list
        Any arguments to display to console.

    References
    ----------
    - Trace interface document
        - https://simon-ritchie.github.io/apysc/en/trace.html

    Examples
    --------
    >>> import apysc as ap
    >>> int_val: ap.Int = ap.Int(10)
    >>> ap.trace("Int value is:", int_val)
    """
    import apysc as ap
    from apysc._string import string_util
    from apysc._type.variable_name_interface import VariableNameInterface

    expression: str = "console.log("
    arg_strs: List[str] = []
    for arg in args:
        if isinstance(arg, VariableNameInterface):
            arg_strs.append(f"{arg.variable_name}")
            continue
        arg = string_util.escape_str(string=str(arg))
        arg_strs.append(f'"{arg}"')
    expression += ", ".join(arg_strs)

    func_caller_info: str = _get_func_callers_info()
    expression += f', "{func_caller_info}"'

    expression += ");"
    ap.append_js_expression(expression=expression)


def _get_func_callers_info() -> str:
    """
    Get a function caller's information.

    Returns
    -------
    func_caller_info : str
        A function caller's information, such as the caller's name,
        module name, and line number.
    """
    # Index count: this function + trace + decorator + caller = 3
    OUTER_FRAMES_INDEX: int = 3

    current_frame: Optional[FrameType] = inspect.currentframe()
    outer_frames: List[FrameInfo] = inspect.getouterframes(frame=current_frame)
    file_name: str = outer_frames[OUTER_FRAMES_INDEX].filename
    file_name = file_name.rsplit("/", maxsplit=1)[-1]
    lineno: int = outer_frames[OUTER_FRAMES_INDEX].lineno
    function: str = outer_frames[OUTER_FRAMES_INDEX].function
    if function != "<module>":
        func_caller_info: str = (
            f"\\nCalled from: {function}, file name: {file_name}, line number: {lineno}"
        )
    else:
        func_caller_info = f"\\nCalled from: {file_name}, line number: {lineno}"
    return func_caller_info
