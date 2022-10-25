"""Class implementation for the parent-related mix-in.
"""

from typing import TYPE_CHECKING
from typing import Dict
from typing import Optional

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.revert_mixin import RevertMixIn
from apysc._validation import arg_validation_decos

if TYPE_CHECKING:
    from apysc._display.child_mixin import ChildMixIn


class ParentMixIn(RevertMixIn):

    _parent: Optional["ChildMixIn"] = None

    @property
    def parent(self) -> Optional["ChildMixIn"]:
        """
        Get a parent instance that has an add_child and remove_child
        interfaces.

        Returns
        -------
        parent : any parent instance (ChildMixIn) or None
            Parent instance with `add_child` and `remove_child`
            interfaces. If this instance does not have a parent
            instance (not added child), this interface returns None.

        References
        ----------
        - Display object parent interfaces
            - https://simon-ritchie.github.io/apysc/en/display_object_parent.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite_1: ap.Sprite = ap.Sprite()
        >>> sprite_1.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite_1.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> sprite_2: ap.Sprite = ap.Sprite()
        >>> sprite_2.add_child(rectangle)
        >>> rectangle.parent == sprite_2
        True
        """
        return self._parent

    @parent.setter
    @arg_validation_decos.is_display_object_container(
        arg_position_index=1, optional=True
    )
    def parent(self, value: Optional["ChildMixIn"]) -> None:
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
            If specified instance is not None and hasn't `ChildMixIn`
            interfaces.

        References
        ----------
        - Display object parent interfaces
            - https://simon-ritchie.github.io/apysc/en/display_object_parent.html  # noqa
        """
        from apysc._validation import parent_validation

        parent_validation.validate_parent_contains_child(parent=value, child=self)
        self._parent = value

    @final
    @add_debug_info_setting(module_name=__name__)
    def remove_from_parent(self) -> None:
        """
        Remove this instance from a parent.

        Raises
        ------
        ValueError
            If a parent is None (there is no parent).
        """
        from apysc._display.child_mixin import ChildMixIn
        from apysc._display.child_mixin import append_expression_of_remove_child
        from apysc._display.display_object import DisplayObject

        parent: Optional[ChildMixIn] = self._parent
        child: DisplayObject = self  # type: ignore
        if parent is not None:
            parent.remove_child(child=child)
        else:
            append_expression_of_remove_child(child=child)

    _parent_snapshots: Dict[str, Optional["ChildMixIn"]]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._set_single_snapshot_val_to_dict(
            dict_name="_parent_snapshots",
            value=self._parent,
            snapshot_name=snapshot_name,
        )

    def _revert(self, *, snapshot_name: str) -> None:
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
