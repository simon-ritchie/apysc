"""Class implementation for copy interface.
"""

from copy import deepcopy
from typing import Any

from apysc._type.type_name_interface import TypeNameInterface
from apysc._type.variable_name_interface import VariableNameInterface


class CopyInterface(TypeNameInterface, VariableNameInterface):

    def _copy(self) -> Any:
        """
        Make a deep copy of this instance.

        Returns
        -------
        result : *
            Copied instance.
        """
        from apysc._expression import expression_variables_util
        from apysc._expression.event_handler_scope import \
            TemporaryNotHandlerScope
        with TemporaryNotHandlerScope():
            result: CopyInterface = deepcopy(self)
            result.variable_name = \
                expression_variables_util.get_next_variable_name(
                    type_name=self.type_name)
            self._append_copy_expression(
                result_variable_name=result.variable_name)
        self._append_value_updating_cpy_exp_to_handler_scope(
            result_variable_name=result.variable_name)
        return result

    def _append_value_updating_cpy_exp_to_handler_scope(
            self, result_variable_name: str) -> None:
        """
        Append a value updating copy expression to the file
        if the current scope is an event handler's one.

        Parameters
        ----------
        result_variable_name : str
            Copied value's variable name.
        """
        from apysc import append_js_expression
        from apysc._expression import event_handler_scope
        evt_handler_scope_count: int = event_handler_scope.\
            get_current_event_handler_scope_count()
        if evt_handler_scope_count == 0:
            return
        expression: str = (
            f'{result_variable_name} = '
            f'cpy({self.variable_name});'
        )
        append_js_expression(expression=expression)

    def _append_copy_expression(self, result_variable_name: str) -> None:
        """
        Append copy expression to file.

        Parameters
        ----------
        result_variable_name : str
            Copied value's variable name.
        """
        from apysc import append_js_expression
        expression: str = (
            f'var {result_variable_name} = '
            f'cpy({self.variable_name});'
        )
        append_js_expression(expression=expression)
