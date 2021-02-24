"""Class implementation for type name interface.
"""


class TypeNameInterface:

    _type_name: str

    @property
    def type_name(self) -> str:
        """
        This instance expression's type name.
        """
        return self._type_name
