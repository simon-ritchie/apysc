"""Abstract base class implementation for if, elif, and else.
"""

from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Dict
from typing import Optional
from typing import Type

from apysc import Boolean
from apysc.expression.indent_num import Indent


class IfBase(ABC):

    _condition: Optional[Boolean]
    _locals: Dict[str, Any]
    _globals: Dict[str, Any]
    _snapshot_name: str
    _indent: Indent

    def __init__(
            self,
            condition: Optional[Boolean],
            locals_: Dict[str, Any],
            globals_: Dict[str, Any]) -> None:
        """
        A class to append if (else if and else) branch instruction
        expression.

        Parameters
        ----------
        condition : Boolean or None
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
        self._indent = Indent()

    def __enter__(self) -> Any:
        """
        Method to be called when begining of with statement.

        Returns
        -------
        self : IfBase
            This instance.
        """
        from apysc.type import revert_interface
        self._snapshot_name = \
            revert_interface.make_snapshots_of_each_scope_vars(
                locals_=self._locals, globals_=self._globals)
        self._append_enter_expression()
        self._indent.__enter__()
        return self

    @abstractmethod
    def _append_enter_expression(self) -> None:
        """
        Append branch instruction start expression to file.
        """

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
        from apysc.type import revert_interface
        revert_interface.revert_each_scope_vars(
            snapshot_name=self._snapshot_name,
            locals_=self._locals, globals_=self._globals)
        self._indent.__exit__()
        self._append_exit_expression()
        self._set_last_scope()

    def _append_exit_expression(self) -> None:
        """
        Append if branch instruction end expression to file.
        """
        from apysc.expression import expression_file_util
        expression_file_util.append_js_expression(expression='}')

    @abstractmethod
    def _set_last_scope(self) -> None:
        """
        Set expression last scope value.
        """

    def _last_scope_is_if_or_elif(self) -> bool:
        """
        Get a boolean value whether the last scope is If or Elif.

        Returns
        -------
        result : bool
            If last scope is If or Else, then True will be returned.
        """
        from apysc.expression import last_scope
        from apysc.expression.last_scope import LastScope
        last_scope_: LastScope = last_scope.get_last_scope()
        if last_scope_ != LastScope.IF and last_scope_ != LastScope.ELIF:
            return False
        return True
