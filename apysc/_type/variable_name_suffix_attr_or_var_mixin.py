"""This module is for the attribute or variable name's suffix-related
mix-in class.
"""

from typing_extensions import final

from apysc._validation import arg_validation_decos


class VariableNameSuffixAttrOrVarMixIn:
    @final
    @arg_validation_decos.not_empty_string(arg_position_index=1)
    def _get_attr_or_variable_name_suffix(self, *, value_identifier: str) -> str:
        """
        Get an attribute or variable name's suffix if its value
        is not blank.

        Parameters
        ----------
        value_identifier : str
            Value identifier string (e.g., `x`).

        Returns
        -------
        attr_or_variable_name_suffix : str
            An attribute or variable's name suffix.
            In the following cases, this value becomes a blank string.
            - If this instance is not the `VariableNameSuffixMixIn`
                instance.
            - If a suffix is a blank string.
        """
        from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn

        if not isinstance(self, VariableNameSuffixMixIn):
            return ""
        if self._variable_name_suffix == "":
            return ""

        attr_or_variable_name_suffix: str = (
            f"{self._variable_name_suffix}__{value_identifier}"
        )
        return attr_or_variable_name_suffix
