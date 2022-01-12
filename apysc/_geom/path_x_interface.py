"""Interface class implementation for the x path data.
"""

from typing import Dict

from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface


class PathXInterface(RevertInterface, AttrLinkingInterface):

    _x: Int

    def _initialize_x_if_not_initialized(self) -> None:
        """
        Initialize the _x attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_x'):
            return
        self._x = Int(0)

        self._append_x_linking_setting()

    def _append_x_linking_setting(self) -> None:
        """
        Append a x attribute linking setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_x_linking_setting,
                locals_=locals(),
                module_name=__name__, class_=PathXInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._x, attr_name='x')
            self._append_attr_to_linking_stack(
                attr=self._x, attr_name='x')

    @property
    def x(self) -> Int:
        """
        Get a x-coordinate of the destination point.

        Returns
        -------
        x : Int
            A x-coordinate of the destination point.

        Examples
        --------
        >>> import apysc as ap
        >>> line_to: ap.PathLineTo = ap.PathLineTo(x=50, y=50)
        >>> line_to.x = ap.Int(100)
        >>> line_to.x
        Int(100)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='x', locals_=locals(),
                module_name=__name__, class_=PathXInterface):
            self._initialize_x_if_not_initialized()
            return self._x._copy()

    @x.setter
    def x(self, value: Int) -> None:
        """
        Set a x-coordinate of the destination point.

        Parameters
        ----------
        value : Int
            X-coordinate of the destination point.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='x', locals_=locals(),
                module_name=__name__, class_=PathXInterface):
            self._initialize_x_if_not_initialized()
            self._x.value = value

            self._append_x_linking_setting()

    _x_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_x_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_x_snapshots',
            value=int(self._x._value), snapshot_name=snapshot_name)

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
        self._initialize_x_if_not_initialized()
        self._x._value = self._x_snapshots[snapshot_name]
