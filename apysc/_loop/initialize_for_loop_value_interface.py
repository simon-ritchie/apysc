"""The interface implementation for the `_initialize_for_loop_value` method.
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

_T = TypeVar('_T')


class InitializeForLoopValueInterface(ABC, Generic[_T]):
    @abstractmethod
    def _initialize_for_loop_value(self) -> _T:
        """
        Initialize this instance for a loop value.
        """
