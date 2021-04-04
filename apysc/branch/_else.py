"""Else branch instruction implementation.
"""

from typing import Any
from typing import Dict

from apysc.branch.if_base import IfBase


class Else(IfBase):

    def __init__(
            self,
            locals_: Dict[str, Any],
            globals_: Dict[str, Any]) -> None:
        """
        A class to append else branch instruction expression.

        Parameters
        ----------
        locals_ : dict
            Current scope's local variables. Set locals() value to
            this argument.
        globals_ : dict
            Current scope's golobal variables. Set golobals() value
            to this argument.
        """
        super().__init__(
            condition=None,
            locals_=locals_,
            globals_=globals_)

    def _append_enter_expression(self) -> None:
        """
        Append else branch instruction start expression to file.

        Raises
        ------
        ValueError
            If the last scope is not If or Elif.
        """
        from apysc.expression import expression_file_util
        if not self._last_scope_is_if_or_elif():
            raise ValueError(
                'Else interface can only use right after If or Elif '
                'interfaces.')
        expression: str = (
            'else {'
        )
        expression_file_util.append_js_expression(expression=expression)

    def _set_last_scope(self) -> None:
        """
        Set expression last scope value.
        """
        from apysc.expression import last_scope
        from apysc.expression.last_scope import LastScope
        last_scope.set_last_scope(value=LastScope.ELSE)
