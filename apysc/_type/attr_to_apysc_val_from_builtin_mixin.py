"""This module is for the attribute conversion interface from
built-in value to apysc value.
"""

from typing import Union

from typing_extensions import final

from apysc._type.boolean import Boolean
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)


class AttrToApyscValFromBuiltinMixIn:
    @final
    def _get_copied_int_from_builtin_val(
        self, *, integer: Union[int, Int], attr_identifier: str
    ) -> Int:
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
        from apysc._converter.to_apysc_val_from_builtin import (
            get_copied_int_from_builtin_val,
        )

        suffix: str = _get_variable_name_suffix(
            instance=self, attr_identifier=attr_identifier
        )
        copied: Int = get_copied_int_from_builtin_val(
            integer=integer, variable_name_suffix=suffix
        )
        return copied

    @final
    def _get_copied_number_from_builtin_val(
        self, *, float_or_num: Union[float, Number], attr_identifier: str
    ) -> Number:
        """
        Get a copied number value from a Python built-in float
        and set an attribute's variable name suffix.

        Parameters
        ----------
        float_or_num : Union[float, Number]
            Target float (or Number) value.
        attr_identifier : str
            Attribute identifier string (e.g., `fill_alpha`).

        Returns
        -------
        copied : Number
            Copied Number value.
        """
        from apysc._converter.to_apysc_val_from_builtin import (
            get_copied_number_from_builtin_val,
        )

        suffix: str = _get_variable_name_suffix(
            instance=self, attr_identifier=attr_identifier
        )
        copied: Number = get_copied_number_from_builtin_val(
            float_or_num=float_or_num, variable_name_suffix=suffix
        )
        return copied

    @final
    def _get_copied_string_from_builtin_val(
        self, *, string: Union[str, String], attr_identifier: str
    ) -> String:
        """
        Get a copied String value from a Python built-in str
        and set an attribute's variable name suffix.

        Parameters
        ----------
        string : Union[str, String]
            Target string value.
        attr_identifier : str
            Attribute identifier string (e.g., `fill_color`).

        Returns
        -------
        copied : String
            Copied String value.
        """
        from apysc._converter.to_apysc_val_from_builtin import (
            get_copied_string_from_builtin_val,
        )

        suffix: str = _get_variable_name_suffix(
            instance=self, attr_identifier=attr_identifier
        )
        copied: String = get_copied_string_from_builtin_val(
            string=string, variable_name_suffix=suffix
        )
        return copied

    @final
    def _get_copied_boolean_from_builtin_val(
        self, *, bool_val: Union[bool, Boolean], attr_identifier: str
    ) -> Boolean:
        """
        Get a copied Boolean value from a Python built-in bool
        and set an attribute's variable name suffix.

        Parameters
        ----------
        bool_val : Union[bool, Boolean]
            Target bool value.
        attr_identifier : str
            Attribute identifier string (e.g., `fill_color`).

        Returns
        -------
        copied : Boolean
            Copied Boolean value.
        """
        from apysc._converter.to_apysc_val_from_builtin import (
            get_copied_boolean_from_builtin_val,
        )

        suffix: str = _get_variable_name_suffix(
            instance=self, attr_identifier=attr_identifier
        )
        copied: Boolean = get_copied_boolean_from_builtin_val(
            bool_val=bool_val, variable_name_suffix=suffix
        )
        return copied


def _get_variable_name_suffix(
    *, instance: AttrToApyscValFromBuiltinMixIn, attr_identifier: str
) -> str:
    """
    Get a target instance's variable name suffix.

    Parameters
    ----------
    instance : AttrToApyscValFromBuiltinMixIn
        A target instance.
    attr_identifier : str
        Attribute identifier string (e.g., `x`).

    Returns
    -------
    suffix : str
        A target instance's variable name suffix.
        This value becomes a blank string if a specified
        instance type is not the `VariableNameSuffixAttrOrVarMixIn`.
    """
    if isinstance(instance, VariableNameSuffixAttrOrVarMixIn):
        suffix: str = instance._get_attr_or_variable_name_suffix(
            value_identifier=attr_identifier
        )
        return suffix

    return ""
