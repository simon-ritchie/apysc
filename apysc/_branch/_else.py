"""Else branch instruction implementation.
"""

from typing import Any
from typing import Dict
from typing import Optional

from apysc._branch.if_base import IfBase


class Else(IfBase):
    """
    A class to append else branch instruction expression.

    References
    ----------
    - Else document
        - https://simon-ritchie.github.io/apysc/else.html
    - Each branch instruction class scope variables reverting setting
        - https://bit.ly/3rkAuaT
    """

    def __init__(
            self,
            locals_: Optional[Dict[str, Any]] = None,
            globals_: Optional[Dict[str, Any]] = None) -> None:
        """
        A class to append else branch instruction expression.

        Parameters
        ----------
        locals_ : dict or None, default None
            Current scope's local variables. Set locals() value to
            this argument.
        globals_ : dict or None, default None
            Current scope's golobal variables. Set golobals() value
            to this argument.

        References
        ----------
        - Else document
            - https://simon-ritchie.github.io/apysc/else.html
        - Each branch instruction class scope variables reverting setting
            - https://bit.ly/3rkAuaT
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=Else):
            super().__init__(
                condition=None,
                locals_=locals_,
                globals_=globals_)

    def _append_enter_expression(self) -> None:
        """
        Append else branch instruction start expression.

        Raises
        ------
        ValueError
            If the last scope is not If or Elif.
        """
        import apysc as ap
        if not self._last_scope_is_if_or_elif():
            raise ValueError(
                'Else interface can only use right after If or Elif '
                'interfaces.')
        expression: str = (
            'else {'
        )
        ap.append_js_expression(expression=expression)

    def _set_last_scope(self) -> None:
        """
        Set expression last scope value.
        """
        from apysc._expression import last_scope
        from apysc._expression.last_scope import LastScope
        last_scope.set_last_scope(value=LastScope.ELSE)
