"""Implementation of the VariableNameMixIn class.
"""

from typing import List

from typing_extensions import final

from apysc._type.deleted_object_mixin import DeletedObjectMixIn
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos


class VariableNameMixIn(DeletedObjectMixIn):

    _variable_name: str
    _variable_name_history: List[str]

    @property
    def variable_name(self) -> str:
        """
        Get a js variable name of this instance.

        Returns
        -------
        variable_name : str
            A js variable name of this instance.
        """
        if not hasattr(self, "_variable_name"):
            return ""
        variable_name: str = self._variable_name
        if isinstance(self, VariableNameSuffixMixIn):
            suffix: str = self._variable_name_suffix
            if suffix != "" and not variable_name.endswith(f"__{suffix}"):
                variable_name += f"__{suffix}"
        return variable_name

    @variable_name.setter
    @arg_validation_decos.is_builtin_string(arg_position_index=1, optional=False)
    @arg_validation_decos.not_empty_string(arg_position_index=1)
    def variable_name(self, variable_name: str) -> None:
        """
        Set a js variable name of this instance.

        Parameters
        ----------
        variable_name : str
            Variable name to set.
        """
        if not hasattr(self, "_variable_name_history"):
            self._variable_name_history = []
        self._variable_name = variable_name
        self._variable_name_history.append(variable_name)

    @final
    def _get_previous_variable_name(self) -> str:
        """
        Get a previous variable name.

        Returns
        -------
        previous_variable_name : str
            A previous-variable name of this instance.
            If that value is not existing, this interface
            returns a blank string.
        """
        if not hasattr(self, "_variable_name_history"):
            return ""
        if len(self._variable_name_history) <= 1:
            return ""
        return self._variable_name_history[-2]
