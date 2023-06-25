"""Variable name-related Validation interfaces.
"""

from typing import Any

from apysc._type.variable_name_mixin import VariableNameMixIn


def validate_variable_name_mixin_type(
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
    from apysc._validation import validation_common_utils

    if not isinstance(instance, VariableNameMixIn):
        err_msg: str = (
            "Specified instance type is not VariableNameMixIn : " f"{type(instance)}"
        )
        err_msg = validation_common_utils.append_additional_err_msg(
            err_msg=err_msg, additional_err_msg=additional_err_msg
        )
        raise TypeError(err_msg)
    return instance
