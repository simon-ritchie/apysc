"""Interface class implementation for the first control x path data.
"""

from typing import Dict

from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface


class PathControlX1Interface(RevertInterface, AttrLinkingInterface):

    _control_x1: Int

    def _initialize_control_x1_if_not_initialized(self) -> None:
        """
        Initialize the _control_x1 attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_control_x1'):
            return
        self._control_x1 = Int(0)

        self._append_control_x1_linking_setting()

    def _append_control_x1_linking_setting(self) -> None:
        """
        Append a control_x1 attribute to the linking setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='control_x1', locals_=locals(),
                module_name=__name__, class_=PathControlX1Interface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._control_x1, attr_name='control_x1')
            self._append_attr_to_linking_stack(
                attr=self._control_x1, attr_name='control_x1')

    @property
    def control_x1(self) -> Int:
        """
        Get a first x-coordinate of the control point.

        Returns
        -------
        control_x1 : Int
            First x-coordinate of the control point.

        Examples
        --------
        >>> import apysc as ap
        >>> bezier_3d: ap.PathBezier3D = ap.PathBezier3D(
        ...     control_x1=50, control_y1=0,
        ...     control_x2=100, control_y2=0,
        ...     dest_x=150, dest_y=50)
        >>> bezier_3d.control_x1 = ap.Int(75)
        >>> bezier_3d.control_x1
        Int(75)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='control_x1', locals_=locals(),
                module_name=__name__, class_=PathControlX1Interface):
            self._initialize_control_x1_if_not_initialized()
            return self._control_x1._copy()

    @control_x1.setter
    def control_x1(self, value: Int) -> None:
        """
        Set a first x-coordinate of the control point.

        Parameters
        ----------
        value : Int
            First x-coordinate of the control point.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='control_x1', locals_=locals(),
                module_name=__name__, class_=PathControlX1Interface):
            self._initialize_control_x1_if_not_initialized()
            self._control_x1.value = value

            self._append_control_x1_linking_setting()

    _control_x1_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_control_x1_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_control_x1_snapshots',
            value=int(self._control_x1._value), snapshot_name=snapshot_name)

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
        self._initialize_control_x1_if_not_initialized()
        self._control_x1._value = self._control_x1_snapshots[snapshot_name]
