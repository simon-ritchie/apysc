"""Class implementation for copy interface.
"""

from copy import deepcopy
from typing import Any

from apysc.type.type_name_interface import TypeNameInterface
from apysc.type.variable_name_interface import VariableNameInterface


class CopyInterface(TypeNameInterface, VariableNameInterface):

    def _copy(self) -> Any:
        """
        Make a deep copy of this instance.

        Returns
        -------
        result : *
            Copied instance.
        """
        from apysc.expression import expression_variables_util
        result: CopyInterface = deepcopy(self)
        result.variable_name = \
            expression_variables_util.get_next_variable_name(
                type_name=self.type_name)
        self._append_copy_expression(
            result_variable_name=result.variable_name)
        return result

    def _append_copy_expression(self, result_variable_name: str) -> None:
        """
        Append copy expression to file.

        Parameters
        ----------
        result_variable_name : str
            Copied value's variable name.
        """
        from apysc.expression import expression_file_util
        expression: str = (
            f'var {result_variable_name} = '
            f'cpy({self.variable_name});'
        )
        expression_file_util.append_js_expression(expression=expression)
