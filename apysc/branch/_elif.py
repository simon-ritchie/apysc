"""Elif (else if) branch instruction implementations.
"""

from apysc.branch.if_base import IfBase


class Elif(IfBase):

    def _append_enter_expression(self) -> None:
        """
        Append else if branch instruction start expression to file.

        Raises
        ------
        ValueError
            If the last scope is not If or Elif.
        """
        from apysc.expression import expression_file_util
        if not self._last_scope_is_if_or_elif():
            raise ValueError(
                'Elif interface can only use right after If or Elif '
                'interfaces.'
                '\n\nMaybe you are using Int or String, or anything else'
                ' comparison expression at Elif constructor (e.g., '
                '`with Elif(any_value == 10, ...):`).'
                '\nCurrently that specifying expression directly is not '
                'supported so please'
                ' define condition seperately as follows:'
                '\ncondition: Boolean = any_value == 10'
                '\n...'
                '\nwith Elif(condition, ....):')
        if self._condition is None:
            raise ValueError(
                'Elif expression\'s condition argument can\'t be set None.')
        expression: str = (
            f'else if ({self._condition.variable_name}) {{'
        )
        expression_file_util.append_js_expression(expression=expression)

    def _set_last_scope(self) -> None:
        """
        Set expression last scope value.
        """
        from apysc.expression import last_scope
        from apysc.expression.last_scope import LastScope
        last_scope.set_last_scope(value=LastScope.ELIF)
