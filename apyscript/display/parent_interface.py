"""Class implementation for parent related interface.
"""

from typing import Any, Optional


class ParentInterface:

    _parent: Optional[Any] = None

    @property
    def parent(self) -> Optional[Any]:
        """
        Get parent instance that has a add_child and remove_child
        interfaces.

        Returns
        -------
        parent : any parent instance or None
            Parent instance that has a add_child and remove_child
            interfaces. If this instance not have parent instance (not
            added child), None will be returned.
        """
        return self._parent

    @parent.setter
    def parent(self, value: Optional[Any]) -> None:
        """
        Set parent instance.

        Notes
        -----
        Only use this setter method at add_child or that's related
        interface.

        Parameters
        ----------
        value : *
            Parent instance to be set.

        Raises
        ------
        ValueError
            If specified instance is not None and hasn't `ChildInterface`
            interfaces.
        """
        self._parent = value
