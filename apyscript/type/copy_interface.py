"""Class implementation for copy interface.
"""

from copy import deepcopy
from typing import Any

from apyscript.expression import expression_variables_util
from apyscript.type.type_name_interface import TypeNameInterface
from apyscript.type.variable_name_interface import VariableNameInterface


class CopyInterface(TypeNameInterface, VariableNameInterface):

    def _copy(self) -> Any:
        """
        Make a deep copy of this instance.

        Returns
        -------
        result : *
            Copied instance.
        """
        result: CopyInterface = deepcopy(self)
        result.variable_name = \
            expression_variables_util.get_next_variable_name(
                type_name=self.type_name)
        return result
