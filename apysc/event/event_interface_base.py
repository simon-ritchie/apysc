"""Class implementation for each event interfaces' base class.
"""

from typing_extensions import Final

from apysc.type.variable_name_interface import VariableNameInterface


class EventInterfaceBase:

    VARIABLE_NAME_INTERFACE_TYPE_ERR_MSG: Final[str] = (
        'This interface can only be used that inheriting '
        'VariableNameInterface.'
    )

    def validate_self_is_variable_name_interface(
            self) -> VariableNameInterface:
        """
        Validate whether this instance is a VariableNameInterface
        instance or not.

        Returns
        -------
        self_instance : VariableNameInterface
            This instance.

        Raises
        ------
        ValueError
            If this instance is not a VariableNameInterface.
        """
        if not isinstance(self, VariableNameInterface):
            raise ValueError(self.VARIABLE_NAME_INTERFACE_TYPE_ERR_MSG)
        return self
