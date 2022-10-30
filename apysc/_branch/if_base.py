"""This module is for the abstract base class implementation
for if, else if, and else.
"""

from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Dict
from typing import Optional
from typing import Type

from typing_extensions import final

from apysc._expression.indent_num import Indent
from apysc._type.boolean import Boolean


class IfBase(ABC):

    _condition: Optional[Boolean]
    _locals: Dict[str, Any]
    _globals: Dict[str, Any]
    _snapshot_name: str
    _indent: Indent

    def __init__(
        self,
        *,
        condition: Optional[Boolean],
        locals_: Optional[Dict[str, Any]] = None,
        globals_: Optional[Dict[str, Any]] = None
    ) -> None:
        """
        A class to append if (else if and else) branch instruction
        expression.

        Parameters
        ----------
        condition : Boolean or None
            Boolean value to be used for judgment.
        locals_ : dict or None, default None
            Current scope's local variables. Set locals() value
            to this argument. If specified, this interface
            reverts all local scope VariableNameMixIn
            variables (like Int, Sprite) at the end of the
            `If` or the other branch scope. This setting is
            useful when you don't want to update each variable
            by implementing the `If` or the other scope.
        globals_ : dict or None, default None
            Current scope's global variables. Set the globals()
            value to this argument. This setting works the same
            way as the `locals_` argument.

        References
        ----------
        - If
            - https://simon-ritchie.github.io/apysc/en/if.html
        - Elif
            - https://simon-ritchie.github.io/apysc/en/elif.html
        - Else
            - https://simon-ritchie.github.io/apysc/en/else.html
        - Each branch instruction class's scope variables reverting setting
            - https://simon-ritchie.github.io/apysc/en/branch_instruction_variables_reverting_setting.html  # noqa
        """
        if locals_ is None:
            locals_ = {}
        if globals_ is None:
            globals_ = {}
        self._condition = condition
        self._locals = locals_
        self._globals = globals_
        self._indent = Indent()

    @final
    def __enter__(self) -> Any:
        """
        Method to be called when beginning of the with statement.

        Returns
        -------
        self : IfBase
            This instance.
        """
        from apysc._type import revert_mixin

        self._snapshot_name = revert_mixin.make_snapshots_of_each_scope_vars(
            locals_=self._locals, globals_=self._globals
        )
        self._append_enter_expression()
        self._indent.__enter__()
        return self

    @abstractmethod
    def _append_enter_expression(self) -> None:
        """
        Append branch instruction start expression.
        """

    @final
    def __exit__(self, exc_type: Type, exc_value: Any, traceback: Any) -> None:
        """
        Method to be called when ending of the with statement.

        Parameters
        ----------
        exc_type : Type
            Exception type.
        exc_value : *
            Exception value.
        traceback : *
            Traceback value.
        """
        from apysc._type import revert_mixin

        revert_mixin.revert_each_scope_vars(
            snapshot_name=self._snapshot_name,
            locals_=self._locals,
            globals_=self._globals,
        )
        self._indent.__exit__()
        self._append_exit_expression()
        self._set_last_scope()

    @final
    def _append_exit_expression(self) -> None:
        """
        Append if branch instruction ending expression.
        """
        import apysc as ap

        ap.append_js_expression(expression="}")

    @abstractmethod
    def _set_last_scope(self) -> None:
        """
        Set expression last scope value.
        """

    @final
    def _last_scope_is_if_or_elif(self) -> bool:
        """
        Get a boolean value whether the last scope is If or Elif.

        Returns
        -------
        result : bool
            If the last scope is If or Else, this interface
            returns True.
        """
        from apysc._expression import last_scope
        from apysc._expression.last_scope import LastScope

        last_scope_: LastScope = last_scope.get_last_scope()
        if last_scope_ != LastScope.IF and last_scope_ != LastScope.ELIF:
            return False
        return True
