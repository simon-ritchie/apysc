"""If branch instruction implementations.
"""

from typing import Any
from typing import Dict
from typing import Optional

from typing_extensions import final

from apysc._branch.if_base import IfBase
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.boolean import Boolean
from apysc._validation import arg_validation_decos


class If(IfBase):
    """
    A class to append if branch instruction expression.

    References
    ----------
    - If
        - https://simon-ritchie.github.io/apysc/en/if.html
    - Each branch instruction class's scope variables reverting setting
        - https://simon-ritchie.github.io/apysc/en/branch_instruction_variables_reverting_setting.html  # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> int_val: ap.Int = ap.Int(10)
    >>> condition: ap.Boolean = int_val >= 10
    >>> with ap.If(condition):
    ...     ap.trace("Int value is greater than equal 10!")
    ...
    """

    @final
    @arg_validation_decos.is_apysc_boolean(arg_position_index=1)
    @arg_validation_decos.is_vars_dict(arg_position_index=2)
    @arg_validation_decos.is_vars_dict(arg_position_index=3)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        condition: Optional[Boolean],
        *,
        locals_: Optional[Dict[str, Any]] = None,
        globals_: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        A class to append if branch instruction expression.

        Parameters
        ----------
        condition : Boolean or None
            Boolean value to be used for judgment.
        locals_ : dict or None, default None
            Current scope's local variables. Set locals()
            value to this argument. If specified, this interface
            reverts all local scope VariableNameMixIn
            variables (like Int, Sprite) at the end of an `If`
            scope. This setting is useful when you don't want to
            update each variable by implementing the `If` scope.
        globals_ : dict or None, default None
            Current scope's global variables. Set globals()
            value to this argument. This setting works
            the same way as the locals_ argument.

        References
        ----------
        - If
            - https://simon-ritchie.github.io/apysc/en/if.html
        - Each branch instruction class's scope variables reverting setting
            - https://simon-ritchie.github.io/apysc/en/branch_instruction_variables_reverting_setting.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> int_val: ap.Int = ap.Int(10)
        >>> condition: ap.Boolean = int_val >= 10
        >>> with ap.If(condition):
        ...     ap.trace("Int value is greater than equal 10!")
        ...
        """
        super(If, self).__init__(
            condition=condition, locals_=locals_, globals_=globals_
        )

    @final
    def _append_enter_expression(self) -> None:
        """
        Append if branch instruction starting expression.
        """
        from apysc._expression import expression_data_util

        if self._condition is None:
            raise ValueError("If expression's condition argument can't be set None.")
        expression: str = f"if ({self._condition.variable_name}) {{"
        expression_data_util.append_js_expression(expression=expression)

    @final
    def _set_last_scope(self) -> None:
        """
        Set expression last scope value.
        """
        from apysc._expression import last_scope
        from apysc._expression.last_scope import LastScope

        last_scope.set_last_scope(value=LastScope.IF)
