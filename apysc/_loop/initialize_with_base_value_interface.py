"""The interface implementation for the `_initialize_with_base_value` method.
"""

from abc import abstractmethod
from typing import Any


class InitializeWithBaseValueInterface:
    @classmethod
    @abstractmethod
    def _initialize_with_base_value(cls) -> Any:
        """
        Initialize this class with a base value(s).
        """
        raise NotImplementedError(
            "The _initialize_with_base_value abstract method must be implemented."
        )
