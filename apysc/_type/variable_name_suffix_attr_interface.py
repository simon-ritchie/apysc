"""This module is for the attribute's variable name suffix-related
interface class.
"""

from apysc._type.variable_name_suffix_interface import \
    VariableNameSuffixInterface


class VariableNameSuffixAttrInterface:

    def _get_attr_variable_name_suffix(
            self, *, attr_identifier: str) -> str:
        """
        Get an attribute's variable name suffix if its value
        is not blank.

        Parameters
        ----------
        attr_identifier : str
            Attribute identifier string (e.g., `x`).

        Returns
        -------
        attr_variable_name_suffix : str
            An attribute's variable name suffix.
            In the following cases, this value becomes a blank string.
            - If this instance is not the `VariableNameSuffixInterface`
                instance.
            - If a suffix is a blank string.
        """
        if not isinstance(self, VariableNameSuffixInterface):
            return ''
        if self._variable_name_suffix == '':
            return ''

        attr_variable_name_suffix: str = (
            f'{self._variable_name_suffix}__{attr_identifier}'
        )
        return attr_variable_name_suffix
