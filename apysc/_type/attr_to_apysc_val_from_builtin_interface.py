"""This module is for the attribute conversion interface from
built-in value to apysc value.
"""

from typing import Union

from apysc._type.int import Int
from apysc._type.variable_name_suffix_attr_interface import \
    VariableNameSuffixAttrInterface


class AttrToApyscValFromBuiltinInterface:

    def _get_copied_int_from_builtin_val(
            self, *,
            integer: Union[int, Int],
            attr_identifier: str) -> Int:
        """
        Get a copied Int value from a Python built-in int
        and set an attribute's variable name suffix.

        Parameters
        ----------
        integer : Union[int, Int]
            Target integer value.
        attr_identifier : str
            Attribute identifier string (e.g., `x`).

        Returns
        -------
        copied : Int
            Copied Int value.
        """
        from apysc._converter.to_apysc_val_from_builtin import \
            get_copied_int_from_builtin_val
        if isinstance(self, VariableNameSuffixAttrInterface):
            suffix: str = self._get_attr_variable_name_suffix(
                attr_identifier=attr_identifier)
        else:
            suffix = ''
        copied: Int = get_copied_int_from_builtin_val(
            integer=integer, variable_name_suffix=suffix)
        return copied
