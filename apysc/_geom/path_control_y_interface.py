"""Interface class implementation for the control y path data.
"""

from typing import Dict

from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface


class PathControlYInterface(RevertInterface, AttrLinkingInterface):

    _control_y: Int

    def _initialize_control_y_if_not_initialized(self) -> None:
        """
        Initialize the _control_y attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_control_y'):
            return
        self._control_y = Int(0)

        self._append_control_y_linking_setting()

    def _append_control_y_linking_setting(self) -> None:
        """
        Append a control_y attribute linking setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_control_y_linking_setting,
                locals_=locals(),
                module_name=__name__, class_=PathControlYInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._control_y, attr_name='control_y')
            self._append_attr_to_linking_stack(
                attr=self._control_y, attr_name='control_y')

    @property
    def control_y(self) -> Int:
        """
        Get a Y-coordinate of the control point.

        Returns
        -------
        control_y : Int
            Y-coordinate of the control point.

        Examples
        --------
        >>> import apysc as ap
        >>> bezier_2d: ap.PathBezier2D = ap.PathBezier2D(
        ...     control_x=0, control_y=0, dest_x=50, dest_y=50)
        >>> bezier_2d.control_y = ap.Int(25)
        >>> bezier_2d.control_y
        Int(25)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='control_y', locals_=locals(),
                module_name=__name__, class_=PathControlYInterface):
            self._initialize_control_y_if_not_initialized()
            return self._control_y._copy()

    @control_y.setter
    def control_y(self, value: Int) -> None:
        """
        Set a Y-coordinate of the control point.

        Parameters
        ----------
        value : Int
            Y-coordinate of the control point.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='control_y', locals_=locals(),
                module_name=__name__, class_=PathControlYInterface):
            self._initialize_control_y_if_not_initialized()
            self._control_y.value = value

            self._append_control_y_linking_setting()

    _control_y_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_control_y_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_control_y_snapshots',
            value=int(self._control_y._value), snapshot_name=snapshot_name)

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
        self._initialize_control_y_if_not_initialized()
        self._control_y._value = self._control_y_snapshots[snapshot_name]
