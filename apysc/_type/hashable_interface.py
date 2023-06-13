"""The interface implementation for the `__hash__` method.
"""

from abc import abstractmethod


class HashableInterface:

    @abstractmethod
    def __hash__(self) -> str:
        """
        Get a hashed string.
        """
