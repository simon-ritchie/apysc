"""This module is for the variable name's suffix setting mix-in
class.
"""


class VariableNameSuffixMixIn:
    __variable_name_suffix: str = ""

    @property
    def _variable_name_suffix(self) -> str:
        """
        Get a variable name suffix string.

        Returns
        -------
        variable_name_suffix : str
            A variable name suffix string.
        """
        return self.__variable_name_suffix

    @_variable_name_suffix.setter
    def _variable_name_suffix(self, value: str) -> None:
        """
        Set a variable name suffix string.

        Parameters
        ----------
        value : str
            A string to set.
        """
        self.__variable_name_suffix = value
