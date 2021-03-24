"""Implementation of VariableNameInterface class.
"""


class VariableNameInterface:

    _variable_name: str

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
        self._variable_name = variable_name
