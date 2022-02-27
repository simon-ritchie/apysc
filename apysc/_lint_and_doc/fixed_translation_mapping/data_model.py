"""This module is for the data model of the fixed-translation
mapping setting.
"""


class Mapping:
    """The class of a single fixed-translation mapping setting.
    """

    _key: str
    _value: str

    def __init__(self, *, key: str, value: str) -> None:
        """
        A single fixed-translation mapping setting.

        Parameters
        ----------
        key : str
            A key value (this value needs to set a source
            english string).
        value : str
            A translated value.
        """
        self._key = key
        self._value = value

    @property
    def key(self) -> str:
        """
        Get a key value (a source english string).

        Returns
        -------
        key : str
            A key value (a source english string).
        """
        return self._key
