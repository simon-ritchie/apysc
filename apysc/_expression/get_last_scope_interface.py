"""The interface class implementation for the `_get_last_scope` method.
"""

from abc import ABC
from abc import abstractmethod

from apysc._expression.last_scope import LastScope


class GetLastScopeInterface(ABC):
    @abstractmethod
    def _get_last_scope(self) -> LastScope:
        """
        Get a target last scope value.
        """
