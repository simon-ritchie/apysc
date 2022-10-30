"""`trace` (console.log expression) interface implementations
"""

import inspect
from inspect import FrameInfo
from types import FrameType
from typing import Any
from typing import List
from typing import Optional

from typing_extensions import final

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
    - Trace interface
        - https://simon-ritchie.github.io/apysc/en/trace.html

    Examples
    --------
    >>> import apysc as ap
    >>> int_val: ap.Int = ap.Int(10)
    >>> ap.trace("Int value is:", int_val)
    """
    import apysc as ap
    from apysc._string import string_util
    from apysc._type.variable_name_mixin import VariableNameMixIn

    expression: str = "console.log("
    arg_strs: List[str] = []
    for arg in args:
        if isinstance(arg, VariableNameMixIn):
            arg_strs.append(f"{arg.variable_name}")
            continue
        arg = string_util.escape_str(string=str(arg))
        arg_strs.append(f'"{arg}"')
    expression += ", ".join(arg_strs)

    func_caller_info: str = _get_func_callers_info()
    expression += f', "{func_caller_info}"'

    expression += ");"
    ap.append_js_expression(expression=expression)


_temporary_outer_frames_index_adjustments: Optional[int] = None


class TemporaryOuterFramesIndexAdjustment:

    _temporary_outer_frames_index_adjustments: int

    @final
    def __init__(self, *, temporary_outer_frames_index_adjustments: int) -> None:
        """
        The class for the trace's temporary outer frames index setting.

        Parameters
        ----------
        temporary_outer_frames_index_adjustments : int
            A temporary outer frames index setting to set.
        """
        self._temporary_outer_frames_index_adjustments = (
            temporary_outer_frames_index_adjustments
        )

    @final
    def __enter__(self) -> None:
        """
        Enter and set the temporary outer frames index setting.
        """
        global _temporary_outer_frames_index_adjustments
        _temporary_outer_frames_index_adjustments = (
            self._temporary_outer_frames_index_adjustments
        )

    @final
    def __exit__(self, *args: Any) -> None:
        """
        Exit and revert the temporary outer frames index setting.
        """
        global _temporary_outer_frames_index_adjustments
        _temporary_outer_frames_index_adjustments = None


# Index count: _get_func_callers_info's function + trace + decorator + caller = 3
DEFAULT_OUTER_FRAMES_INDEX: int = 3


def _get_outer_frames_index() -> int:
    """
    Get the trace's outer frames' index setting.

    Returns
    -------
    outer_frames_index : int
        The trace's outer frames' index setting.
    """
    global _temporary_outer_frames_index_adjustments
    if _temporary_outer_frames_index_adjustments is None:
        return DEFAULT_OUTER_FRAMES_INDEX
    return _temporary_outer_frames_index_adjustments


def _get_func_callers_info() -> str:
    """
    Get a function caller's information.

    Returns
    -------
    func_caller_info : str
        A function caller's information, such as the caller's name,
        module name, and line number.
    """
    outer_frames_index: int = _get_outer_frames_index()
    current_frame: Optional[FrameType] = inspect.currentframe()
    outer_frames: List[FrameInfo] = inspect.getouterframes(frame=current_frame)
    file_name: str = outer_frames[outer_frames_index].filename
    file_name = file_name.rsplit("/", maxsplit=1)[-1]
    lineno: int = outer_frames[outer_frames_index].lineno
    function: str = outer_frames[outer_frames_index].function
    if function != "<module>":
        func_caller_info: str = (
            f"\\nCalled from: {function}, file name: {file_name}, line number: {lineno}"
        )
    else:
        func_caller_info = f"\\nCalled from: {file_name}, line number: {lineno}"
    return func_caller_info
