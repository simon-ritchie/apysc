"""For loop class implementation.
"""

from typing import Any
from typing import Dict
from typing import Type

from apysc import Array
from apysc import Int
from apysc.expression.indent_num import Indent


class For:

    _arr: Array
    _locals: Dict[str, Any]
    _globals: Dict[str, Any]
    _snapshot_name: str
    _indent: Indent

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
        self._indent = Indent()

    def __enter__(self) -> Int:
        """
        Method to be called when begining of with statement.

        Returns
        -------
        i : Int
            Loop index.
        """
        from apysc.type import revert_interface
        self._snapshot_name = \
            revert_interface.make_snapshots_of_each_scope_vars(
                locals_=self._locals, globals_=self._globals)
        i: Int = Int(0)
        self._append_enter_expression(i=i)
        self._indent.__enter__()
        return i

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
        from apysc.expression import expression_file_util
        from apysc.expression import last_scope
        from apysc.expression.last_scope import LastScope
        from apysc.type import revert_interface
        revert_interface.revert_each_scope_vars(
            snapshot_name=self._snapshot_name,
            locals_=self._locals, globals_=self._globals)
        self._indent.__exit__()
        expression_file_util.append_js_expression(expression='}')
        last_scope.set_last_scope(value=LastScope.FOR)

    def _append_enter_expression(self, i: Int) -> None:
        """
        Append for loop start expression to file.

        Parameters
        ----------
        i : Int
            Loop index value.
        """
        from apysc.expression import expression_file_util
        i_name: str = i.variable_name
        expression: str = (
            f'var length = {self._arr.variable_name}.length;\n'
            f'for ({i_name} = 0; {i_name} < length; {i_name}++) {{'
        )
        expression_file_util.append_js_expression(expression=expression)
