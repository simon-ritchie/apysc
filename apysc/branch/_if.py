"""If branch instruction implementations.
"""

from apysc.branch.if_base import IfBase


class If(IfBase):

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

    def _set_last_scope(self) -> None:
        """
        Set expression last scope value.
        """
        from apysc.expression import last_scope
        from apysc.expression.last_scope import LastScope
        last_scope.set_last_scope(value=LastScope.IF)
