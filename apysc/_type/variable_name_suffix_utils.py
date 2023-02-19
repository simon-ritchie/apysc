"""The utilities implementations for the variable name suffix-related
functions.
"""

from typing import Any


def get_attr_or_variable_name_suffix(*, instance: Any, value_identifier: str) -> str:
    """
    Get an attribute or variable name's suffix if a specified instance's
    type is the `VariableNameSuffixAttrOrVarMixIn` and its suffix value
    is not blank.

    Parameters
    ----------
    instance : Any
        A target instance.
    value_identifier : str
        A value identifier string (e.g., `x`).

    Returns
    -------
    attr_or_variable_name_suffix : str
        An attribute or variable's name suffix.
        In the following cases, this value becomes a blank string.
        - If a specified instance is not the `VariableNameSuffixMixIn`
            and `VariableNameSuffixAttrOrVarMixIn` instance.
        - If a suffix is a blank string.
    """
    from apysc._type.variable_name_suffix_attr_or_var_mixin import (
        VariableNameSuffixAttrOrVarMixIn,
    )

    suffix: str = ""
    if isinstance(instance, VariableNameSuffixAttrOrVarMixIn):
        suffix = instance._get_attr_or_variable_name_suffix(
            value_identifier=value_identifier
        )
    return suffix
