"""Interface class implementation for the y path data.
"""

from typing import Dict

from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface


class PathYInterface(RevertInterface, AttrLinkingInterface):

    _y: Int

    def _initialize_y_if_not_initialized(self) -> None:
        """
        Initialize the _y attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_y'):
            return
        self._y = Int(0)

        self._append_y_linking_setting()

    def _append_y_linking_setting(self) -> None:
        """
        Append a y attribute linking setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_y_linking_setting,
                locals_=locals(),
                module_name=__name__, class_=PathYInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._y, attr_name='y')
            self._append_attr_to_linking_stack(
                attr=self._y, attr_name='y')

    @property
    def y(self) -> Int:
        """
        Get a y-coordinate of the destination point.

        Returns
        -------
        y : Int
            A y-coordinate of the destination point.

        Examples
        --------
        >>> import apysc as ap
        >>> line_to: ap.PathLineTo = ap.PathLineTo(x=50, y=50)
        >>> line_to.y = ap.Int(100)
        >>> line_to.y
        Int(100)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='y', locals_=locals(),
                module_name=__name__, class_=PathYInterface):
            self._initialize_y_if_not_initialized()
            return self._y._copy()

    @y.setter
    def y(self, value: Int) -> None:
        """
        Set a y-coordinate of the destination point.

        Parameters
        ----------
        value : Int
            Y-coordinate of the destination point.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='y', locals_=locals(),
                module_name=__name__, class_=PathYInterface):
            self._initialize_y_if_not_initialized()
            self._y.value = value

            self._append_y_linking_setting()

    _y_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_y_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_y_snapshots',
            value=int(self._y._value), snapshot_name=snapshot_name)

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
        self._initialize_y_if_not_initialized()
        self._y._value = self._y_snapshots[snapshot_name]
