"""If branch instruction implementations.
"""

from typing import Any
from typing import Dict
from typing import Optional

import apysc as ap
from apysc._branch.if_base import IfBase


class If(IfBase):
    """
    A class to append if branch instruction expression.

    References
    ----------
    - If document
        - https://simon-ritchie.github.io/apysc/if.html
    - Each branch instruction class scope variables reverting setting
        - https://bit.ly/3rkAuaT
    """

    def __init__(
            self,
            condition: Optional[ap.Boolean],
            locals_: Optional[Dict[str, Any]] = None,
            globals_: Optional[Dict[str, Any]] = None) -> None:
        """
        A class to append if branch instruction expression.

        Parameters
        ----------
        condition : Boolean or None
            Boolean value to be used for judgment.
        locals_ : dict or None, default None
            Current scope's local variables. Set locals() value to
            this argument. If specified, all local scope
            VariableNameInterface variables (like Int, Sprite) will be
            reverted ad the end of If scope. This setting is useful
            when you don't want to update each variable by the
            implementation of the If scope.
        globals_ : dict or None, default None
            Current scope's global variables. Set golobals() value
            to this argument. This works the same way as the locals_
            argument.

        References
        ----------
        - If document
            - https://simon-ritchie.github.io/apysc/if.html
        - Each branch instruction class scope variables reverting setting
            - https://bit.ly/3rkAuaT
        """
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=If):
            super(If, self).__init__(
                condition=condition, locals_=locals_, globals_=globals_)

    def _append_enter_expression(self) -> None:
        """
        Append if branch instruction start expression.
        """
        import apysc as ap
        if self._condition is None:
            raise ValueError(
                'If expression\'s condition argument can\'t be set None.')
        expression: str = (
            f'if ({self._condition.variable_name}) {{'
        )
        ap.append_js_expression(expression=expression)

    def _set_last_scope(self) -> None:
        """
        Set expression last scope value.
        """
        from apysc._expression import last_scope
        from apysc._expression.last_scope import LastScope
        last_scope.set_last_scope(value=LastScope.IF)
