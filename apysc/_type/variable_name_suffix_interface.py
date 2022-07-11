"""This module is for the variable name's suffix setting interface
class.
"""


class VariableNameSuffixInterface:

    _variable_name_suffix: str = ''

    @property
    def variable_name_suffix(self) -> str:
        """
        Get a variable name suffix string.

        Returns
        -------
        variable_name_suffix : str
            A variable name suffix string.
        """
        return self._variable_name_suffix

    @variable_name_suffix.setter
    def variable_name_suffix(self, value: str) -> None:
        """
        Set a variable name suffix string.

        Parameters
        ----------
        value : str
            A string to set.
        """
        self._variable_name_suffix = value
