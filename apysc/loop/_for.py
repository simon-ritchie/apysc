"""For loop class implementation.
"""

from typing import Any, Dict
from apysc import Array


class For:

    _arr: Array
    _locals: Dict[str, Any]
    _globals: Dict[str, Any]

    def __init__(
            self, arr: Array, locals_: Dict[str, Any],
            globals_: Dict[str, Any]) -> None:
        """
        A class to append for (loop) expression.

        Parameters
        ----------
        arr : Array
            Array instance to iterate.
        locals_ : dict
            Current scope's local variables. Set locals() value to
            this argument.
        globals_ : dict
            Current scope's golobal variables. Set golobals() value
            to this argument.
        """
        self._arr = arr
        self._locals = locals_
        self._globals = globals_
