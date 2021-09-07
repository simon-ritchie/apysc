"""Class implementation for the attribute linking interface.

This interface is used for updating an old property value to
achieve consistency in the handler functions.
"""

from typing import Generic, TypeVar
from typing import List

import apysc as ap

_T = TypeVar('_T', ap.Int, ap.Number, ap.String)


class AttrLinkingInterface(Generic[_T]):

    _attr_linking_stack: List[_T]

    def _initialize_attr_linking_stack(self) -> None:
        """
        Initialize the _attr_linking_stack attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_attr_linking_stack'):
            return
        self._attr_linking_stack = []

    def _append_attr_to_linking_stack(self, attr: _T) -> None:
        """
        Append an attribute to the linking attribute stack.

        Parameters
        ----------
        attr : Int, Number, or String
            Target attribute to be appended.
        """
        pass
