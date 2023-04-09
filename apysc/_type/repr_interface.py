"""Interface class implementation for the `__repr__` method.
"""

from abc import ABC
from abc import abstractmethod


class ReprInterface(ABC):
    @abstractmethod
    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).
        """
