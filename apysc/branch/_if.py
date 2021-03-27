"""If condition implementations.
"""

from typing import Any, List
from typing import Dict
from typing import Type

from apysc.type import Boolean
from apysc.type.revert_interface import RevertInterface


class If:

    _condition: Boolean
    _locals: Dict[str, Any]
    _globals: Dict[str, Any]

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
        self._make_snapshots_of_each_scope_vars()
        pass

    def _make_snapshots_of_each_scope_vars(self) -> str:
        """
        Make snapshots of each scope's variables (_locals and _globals).

        Returns
        -------
        snapshot_name : str
            Used snapshot name.
        """
        ended: Dict[int, bool] = {}
        snapshot_name: str = ''
        variables: List[Any] = [*self._locals.values(), *self._globals.values()]
        for variable in variables:
            if not isinstance(variable, RevertInterface):
                continue
            var_id: int = id(variable)
            if var_id in ended:
                continue
            if snapshot_name == '':
                snapshot_name = variable._get_next_snapshot_name()
            variable._run_all_make_snapshot_methods(
                snapshot_name=snapshot_name)
            ended[var_id] = True
        return snapshot_name

    def __exit__(
            self, exc_type: Type,
            exc_value: Any,
            traceback: Any) -> None:
        pass
