"""Else branch instruction implementation.
"""

from typing import Any
from typing import Dict
from typing import Optional

from typing_extensions import final

from apysc._branch.if_base import IfBase
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos


class Else(IfBase):
    """
    A class to append else branch instruction expression.

    Notes
    -----
    - You can only use this class immediately after the
        `If` or `Elif` statement.

    References
    ----------
    - Else
        - https://simon-ritchie.github.io/apysc/en/else.html
    - Each branch instruction class's scope variables reverting setting
        - https://simon-ritchie.github.io/apysc/en/branch_instruction_variables_reverting_setting.html  # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> int_val: ap.Int = ap.Int(10)
    >>> with ap.If(int_val >= 11):
    ...     ap.trace("Value is greater than equal 11.")
    ...
    >>> with ap.Else():
    ...     ap.trace("Value is less than 11.")
    ...
    """

    @final
    @arg_validation_decos.is_vars_dict(arg_position_index=1)
    @arg_validation_decos.is_vars_dict(arg_position_index=2)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        *,
        locals_: Optional[Dict[str, Any]] = None,
        globals_: Optional[Dict[str, Any]] = None
    ) -> None:
        """
        A class to append else branch instruction expression.

        Notes
        -----
        - You can only use this class immediately after the
            `If` or `Elif` statement.

        Parameters
        ----------
        locals_ : dict or None, default None
            Current scope's local variables. Set locals()
            value to this argument. If specified, this interface
            reverts all local scope VariableNameMixIn
            variables (like Int, Sprite) at the end of an `Else`
            scope. This setting is useful when you don't want to
            update each variable by implementing the `Else` scope.
        globals_ : dict or None, default None
            Current scope's global variables. Set globals()
            value to this argument. This setting works
            the same way as the locals_ argument.

        References
        ----------
        - Else
            - https://simon-ritchie.github.io/apysc/en/else.html
        - Each branch instruction class's scope variables reverting setting
            - https://simon-ritchie.github.io/apysc/en/branch_instruction_variables_reverting_setting.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> int_val: ap.Int = ap.Int(10)
        >>> with ap.If(int_val >= 11):
        ...     ap.trace("Value is greater than equal 11.")
        ...
        >>> with ap.Else():
        ...     ap.trace("Value is less than 11.")
        ...
        """
        super().__init__(condition=None, locals_=locals_, globals_=globals_)

    @final
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
                "Else interface can only use right after If or Elif " "interfaces."
            )
        expression: str = "else {"
        ap.append_js_expression(expression=expression)

    @final
    def _set_last_scope(self) -> None:
        """
        Set expression last scope value.
        """
        from apysc._expression import last_scope
        from apysc._expression.last_scope import LastScope

        last_scope.set_last_scope(value=LastScope.ELSE)
