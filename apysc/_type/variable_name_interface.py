"""Implementation of VariableNameInterface class.
"""

from typing import List


class VariableNameInterface:

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
        return self._variable_name

    @variable_name.setter
    def variable_name(self, variable_name: str) -> None:
        """
        Set a js variable name of this instance.

        Parameters
        ----------
        variable_name : str
            Variable name to set.
        """
        from apysc.validation import string_validation
        string_validation.validate_not_empty_string(string=variable_name)
        if not hasattr(self, '_variable_name_history'):
            self._variable_name_history = []
        self._variable_name = variable_name
        self._variable_name_history.append(variable_name)

    def _get_previous_variable_name(self) -> str:
        """
        Get a previous variable name.

        Returns
        -------
        previous_variable_name : str
            A previous variable name of this instance. If that value
            is not existing, then a blank string will be returned.
        """
        if not hasattr(self, '_variable_name_history'):
            return ''
        if len(self._variable_name_history) <= 1:
            return ''
        return self._variable_name_history[-2]
