"""Elif (else if) branch instruction implementations.
"""

from apysc.branch.if_base import IfBase


class Elif(IfBase):

    def _append_enter_expression(self) -> None:
        """
        Append if branch instruction start expression to file.

        Raises
        ------
        ValueError
            If the last scope is not If or Elif.
        """
        from apysc.expression import expression_file_util
        from apysc.expression import last_scope
        from apysc.expression.last_scope import LastScope
        last_scope_: LastScope = last_scope.get_last_scope()
        if last_scope_ != LastScope.IF and last_scope_ != LastScope.ELIF:
            raise ValueError(
                'Elif interface can only use right after If or Elif '
                'interfaces.')
        expression: str = (
            f'else if ({self._condition.variable_name}) {{'
        )
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)

    def _set_last_scope(self) -> None:
        """
        Set expression last scope value.
        """
        from apysc.expression import last_scope
        from apysc.expression.last_scope import LastScope
        last_scope.set_last_scope(value=LastScope.ELIF)
