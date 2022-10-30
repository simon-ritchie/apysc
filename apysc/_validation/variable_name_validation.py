"""Variable name-related Validation interfaces.
"""

from typing import Any

from apysc._type.variable_name_mixin import VariableNameMixIn


def validate_variable_name_interface_type(
    *, instance: Any, additional_err_msg: str = ""
) -> VariableNameMixIn:
    """
    Validate specified instance type is VariableNameMixIn.

    Parameters
    ----------
    instance : *
        Instance to be checked.
    additional_err_msg : str, optional
        An additional error message to display.

    Returns
    -------
    instance : VariableNameMixIn
        Checked instance.

    Raises
    ------
    TypeError
        If specified instance type isn't VariableNameMixIn.
    """
    if not isinstance(instance, VariableNameMixIn):
        if additional_err_msg != "":
            additional_err_msg = f"\n{additional_err_msg}"
        raise TypeError(
            "Specified instance type is not VariableNameMixIn : "
            f"{type(instance)}{additional_err_msg}"
        )
    return instance
