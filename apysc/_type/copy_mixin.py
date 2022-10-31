"""Class implementation for copy interface.
"""

from copy import deepcopy
from typing import Any

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.type_name_mixin import TypeNameMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn


class CopyMixIn(TypeNameMixIn, VariableNameMixIn):
    @final
    @add_debug_info_setting(module_name=__name__)
    def _copy(self) -> Any:
        """
        Make a deep copy of this instance.

        Returns
        -------
        result : *
            Copied instance.
        """
        from apysc._expression import expression_variables_util
        from apysc._expression.event_handler_scope import TemporaryNotHandlerScope

        with TemporaryNotHandlerScope():
            result: CopyMixIn = deepcopy(self)
            result.variable_name = expression_variables_util.get_next_variable_name(
                type_name=self.type_name
            )
            self._append_copy_expression(result_variable_name=result.variable_name)
        self._append_value_updating_cpy_exp_to_handler_scope(
            result_variable_name=result.variable_name
        )
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_value_updating_cpy_exp_to_handler_scope(
        self, *, result_variable_name: str
    ) -> None:
        """
        Append a value updating copy expression
        if the current scope is an event handler's one.

        Parameters
        ----------
        result_variable_name : str
            Copied value's variable name.
        """
        import apysc as ap
        from apysc._expression import event_handler_scope
        from apysc._type.type_util import is_immutable_type

        if not event_handler_scope.current_scope_is_in_event_handler():
            return
        if is_immutable_type(value=self):
            expression: str = f"{result_variable_name} = {self.variable_name};"
        else:
            expression = f"{result_variable_name} = " f"cpy({self.variable_name});"
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_copy_expression(self, *, result_variable_name: str) -> None:
        """
        Append copy expression.

        Parameters
        ----------
        result_variable_name : str
            Copied value's variable name.
        """
        import apysc as ap
        from apysc._type.type_util import is_immutable_type

        if is_immutable_type(value=self):
            expression: str = f"var {result_variable_name} = " f"{self.variable_name};"
        else:
            expression = f"var {result_variable_name} = " f"cpy({self.variable_name});"
        ap.append_js_expression(expression=expression)
