"""Class implementation for type name interface.
"""


class TypeNameInterface:

    _type_name: str

    @property
    def type_name(self) -> str:
        """
        Get this instance expression's type name.

        Returns
        -------
        type_name : str
            This instance expression's type name.
        """
        return self._type_name
