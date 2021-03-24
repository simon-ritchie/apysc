"""If condition implementations.
"""


from typing import Any, Dict, Type
from apysc.type import Boolean


class If:

    def __init__(
            self,
            condition: Boolean,
            locals_: Dict[str, Any],
            globals_: Dict[str, Any]) -> None:
        """
        A class to append if branch instruction expression.

        Parameters
        ----------
        condition : Boolean
            Boolean value to be used for judgment.
        locals_ : dict
            Current scope's local variables. Set locals() value to
            this argument.
        globals_ : dict
            Current scope's golobal variables. Set golobals() value
            to this argument.
        """
        pass

    def __enter__(self) -> None:
        pass

    def __exit__(
            self, exc_type: Type,
            exc_value: Any,
            traceback: Any) -> None:
        pass
