"""If branch instruction implementations.
"""

from apysc._branch.if_base import IfBase


class If(IfBase):

    def _append_enter_expression(self) -> None:
        """
        Append if branch instruction start expression to file.
        """
        from apysc import append_js_expression
        if self._condition is None:
            raise ValueError(
                'If expression\'s condition argument can\'t be set None.')
        expression: str = (
            f'if ({self._condition.variable_name}) {{'
        )
        append_js_expression(expression=expression)

    def _set_last_scope(self) -> None:
        """
        Set expression last scope value.
        """
        from apysc._expression import last_scope
        from apysc._expression.last_scope import LastScope
        last_scope.set_last_scope(value=LastScope.IF)
