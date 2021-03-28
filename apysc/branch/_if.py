"""If condition implementations.
"""

from typing import Any
from typing import Dict
from typing import Type

from apysc.expression import indent_num
from apysc.type import Boolean


class If:

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

    def __enter__(self) -> None:
        """
        Method to be called when begining of with statement.
        """
        from apysc.type import revert_interface
        self._snapshot_name = \
            revert_interface.make_snapshots_of_each_scope_vars(
                locals_=self._locals, globals_=self._globals)
        self._append_enter_expression()
        indent_num.increment()

    def _append_enter_expression(self) -> None:
        """
        Append if branch instruction start expression to file.
        """
        from apysc.expression import expression_file_util
        expression: str = (
            f'if ({self._condition.variable_name}) {{'
        )
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)

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
        indent_num.decrement()
        self._append_exit_expression()

    def _append_exit_expression(self) -> None:
        """
        Append if branch instruction end expression to file.
        """
        from apysc.expression import expression_file_util
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression='}')
