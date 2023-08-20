"""The interface class implementation for the `_copy` method.
"""

from abc import abstractmethod
from typing import Generic
from typing import TypeVar

_SelfType = TypeVar("_SelfType", bound="CopyInterface")


class CopyInterface(Generic[_SelfType]):
    @abstractmethod
    def _copy(self) -> _SelfType:
        """
        Make a deep copy of this instance.
        """
