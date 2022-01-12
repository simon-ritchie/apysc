"""Interface class implementation for the relative value.
"""

from typing import Dict

from apysc._type.boolean import Boolean
from apysc._type.revert_interface import RevertInterface


class RelativeInterface(RevertInterface):

    _relative: Boolean

    def _initialize_relative_if_not_initialized(self) -> None:
        """
        Initialize the _relative attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_relative'):
            return
        self._relative = Boolean(False)

    @property
    def relative(self) -> Boolean:
        """
        Get a boolean value indicating whether a path data
        is relative or not.

        Returns
        -------
        relative : Boolean
            A boolean value indicating whether path data
            is relative or not.

        Examples
        --------
        >>> import apysc as ap
        >>> line_to: ap.PathLineTo = ap.PathLineTo(
        ...     x=50, y=50, relative=False)
        >>> line_to.relative = ap.Boolean(True)
        >>> line_to.relative
        Boolean(True)
        """
        self._initialize_relative_if_not_initialized()
        return self._relative._copy()

    @relative.setter
    def relative(self, value: Boolean) -> None:
        """
        Set a boolean value indicating whether path a path data
        is relative or not.

        Parameters
        ----------
        value : Boolean
            A boolean value indicating whether path data
            is relative or not.
        """
        self._initialize_relative_if_not_initialized()
        self._relative.value = value

    _relative_snapshots: Dict[str, bool]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_relative_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_relative_snapshots',
            value=self._relative._value, snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert a value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_relative_if_not_initialized()
        self._relative._value = self._relative_snapshots[snapshot_name]
