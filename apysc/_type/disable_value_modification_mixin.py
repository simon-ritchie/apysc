"""The mix-in class implementation to disable a value modification.
"""


class DisableValueModificationMixIn:
    _disabled_value_modification: bool = False

    def disable_value_modification(self) -> None:
        """
        Disable a value modification. This method is useful when you want to
        prevent the value modification (e.g., the value updating with the
        `value` property).

        Calling this method after the instantiation is recommended.
        """
        self._disabled_value_modification = True

    def raise_if_value_modification_is_disabled(self) -> None:
        """
        Raise an error if the value modification is disabled.

        Raises
        ------
        ValueError
            If the value modification is disabled.
        """
        if self._disabled_value_modification:
            raise ValueError(
                "The value modification of this instance is disabled. "
                "Please created a new value instance or copy this instance."
            )
