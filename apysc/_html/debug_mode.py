"""Debugging mode setting interface implementations for the HTML
and JavaScript.
"""

import os
from typing import Any, Callable, Dict


def set_debug_mode() -> None:
    """
    Set the debug mode for the HTML and JavaScript debugging.
    If this functions is called, the following setting will be applied:
    - HTML minify setting will be disabled.
    - Per each interface JavaScript divider string will be appended.
    """
    from apysc._expression import expression_file_util
    file_path: str = expression_file_util.DEBUG_MODE_SETTING_FILE_PATH
    with open(file_path, 'w') as f:
        f.write('1')


def is_debug_mode() -> bool:
    """
    Get a boolean value whether the current debug mode is enabled or not.

    Returns
    -------
    result : bool
        If the current debug mode is enabled, True will be returned.
    """
    from apysc._expression import expression_file_util
    file_path: str = expression_file_util.DEBUG_MODE_SETTING_FILE_PATH
    if not os.path.isfile(file_path):
        return False
    with open(file_path) as f:
        txt: str = f.read()
    if txt == '1':
        return True
    return False


class DebugInfo:

    _callable: Callable
    _locals: Dict[str, Any]

    def __init__(
            self, callable_: Callable, locals_: Dict[str, Any]) -> None:
        """
        Save a debug information (append callable interface name
        comment and arguments information) to the JavaScript
        expression file.

        Notes
        -----
        If the debug mode setting is not enabled, saving will
        be skipped.

        Parameters
        ----------
        callable_ : Callable
            Target function or method.
        locals_ : dict
            Local variables. This value will be set by the `locals()`
            function.
        """
        self._callable = callable_
        self._locals = locals_
