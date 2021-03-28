"""Abstract base class implementation for if, elif, and else.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Type
from apysc.type import Boolean


class IfBase(ABC):

    _condition: Boolean
    _locals: Dict[str, Any]
    _globals: Dict[str, Any]
    _snapshot_name: str

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
        self._condition = condition
        self._locals = locals_
        self._globals = globals_

    @abstractmethod
    def __enter__(self) -> None:
        """
        Method to be called when begining of with statement.
        """

    @abstractmethod
    def __exit__(
            self, exc_type: Type,
            exc_value: Any,
            traceback: Any) -> None:
        """
        Method to be called when end of with statement.

        Parameters
        ----------
        exc_type : Type
            Exception type.
        exc_value : *
            Exception value.
        traceback : *
            Traceback value.
        """
