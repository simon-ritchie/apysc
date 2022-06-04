"""Variable name-related Validation interfaces.
"""

from typing import Any

from apysc._type.variable_name_interface import VariableNameInterface


def validate_variable_name_interface_type(
        *, instance: Any,
        additional_err_msg: str = '') -> VariableNameInterface:
    """
    Validate specified instance type is VariableNameInterface.

    Parameters
    ----------
    instance : *
        Instance to be checked.
    additional_err_msg : str, optional
        An additional error message to display.

    Returns
    -------
    instance : VariableNameInterface
        Checked instance.

    Raises
    ------
    TypeError
        If specified instance type isn't VariableNameInterface.
    """
    if not isinstance(instance, VariableNameInterface):
        if additional_err_msg != '':
            additional_err_msg = f'\n{additional_err_msg}'
        raise TypeError(
            'Specified instance type is not VariableNameInterface : '
            f'{type(instance)}{additional_err_msg}')
    return instance
