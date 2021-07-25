"""Class implementation for parent related interface.
"""

from typing import Any
from typing import Dict
from typing import Optional

from apysc._type.revert_interface import RevertInterface


class ParentInterface(RevertInterface):

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

        References
        ----------
        - Display object parent interfaces document
            - https://bit.ly/3wQX782
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

        References
        ----------
        - Display object parent interfaces document
            - https://bit.ly/3wQX782
        """
        from apysc._validation import parent_validation
        parent_validation.validate_parent_instance(parent=value)
        parent_validation.validate_parent_contains_child(
            parent=value, child=self)
        self._parent = value

    def remove_from_parent(self) -> None:
        """
        Remove this instance from parent.

        Raises
        ------
        ValueError
            If this instance is not added to any parent.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.remove_from_parent, locals_=locals(),
                module_name=__name__, class_=ParentInterface):
            from apysc._display.child_interface import ChildInterface
            from apysc._display.child_interface import \
                append_expression_of_remove_child
            from apysc._display.display_object import DisplayObject
            parent: Optional[ChildInterface] = self._parent
            child: DisplayObject = self  # type: ignore
            if parent is not None:
                parent.remove_child(child=child)
            else:
                append_expression_of_remove_child(child=child)

    _parent_snapshots: Dict[str, Optional[Any]]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_parent_snapshots'):
            self._parent_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._parent_snapshots[snapshot_name] = self._parent

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._parent = self._parent_snapshots[snapshot_name]
