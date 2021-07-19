"""If branch instruction implementations.
"""

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

    def _append_enter_expression(self) -> None:
        """
        Append if branch instruction start expression to file.
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
