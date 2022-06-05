"""Interface class implementation for the second control y path data.
"""

from typing import Dict

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface
from apysc._validation import arg_validation_decos


class PathControlY2Interface(RevertInterface, AttrLinkingInterface):

    _control_y2: Int

    def _initialize_control_y2_if_not_initialized(self) -> None:
        """
        Initialize the _control_y2 attribute if this instance
        does not initialize it yet.
        """
        if hasattr(self, '_control_y2'):
            return
        self._control_y2 = Int(0)

        self._append_control_y2_linking_setting()

    @add_debug_info_setting(
        module_name=__name__, class_name='PathControlY2Interface')
    def _append_control_y2_linking_setting(self) -> None:
        """
        Append a control_y2 attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._control_y2, attr_name='control_y2')
        self._append_attr_to_linking_stack(
            attr=self._control_y2, attr_name='control_y2')

    @property
    @add_debug_info_setting(
        module_name=__name__, class_name='PathControlY2Interface')
    def control_y2(self) -> Int:
        """
        Get a second y-coordinate of the control point.

        Returns
        -------
        control_y2 : Int
            Second y-coordinate of the control point.

        Examples
        --------
        >>> import apysc as ap
        >>> bezier_3d: ap.PathBezier3D = ap.PathBezier3D(
        ...     control_x1=0, control_y1=0,
        ...     control_x2=50, control_y2=0,
        ...     dest_x=50, dest_y=50)
        >>> bezier_3d.control_y2 = ap.Int(25)
        >>> bezier_3d.control_y2
        Int(25)
        """
        self._initialize_control_y2_if_not_initialized()
        return self._control_y2._copy()

    @control_y2.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    def control_y2(self, value: Int) -> None:
        """
        Set a second y-coordinate of the control point.

        Parameters
        ----------
        value : Int
            Second y-coordinate of the control point.
        """
        from apysc._html.debug_mode import DebugInfo
        with DebugInfo(
                callable_='control_y2', args=[value], kwargs={},
                module_name=__name__,
                class_name=PathControlY2Interface.__name__):
            self._initialize_control_y2_if_not_initialized()
            self._control_y2.value = value

            self._append_control_y2_linking_setting()

    _control_y2_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_control_y2_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_control_y2_snapshots',
            value=int(self._control_y2._value), snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_control_y2_if_not_initialized()
        self._control_y2._value = self._control_y2_snapshots[snapshot_name]
