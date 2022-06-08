"""Interface class implementation for the x path data.
"""

from typing import Dict

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface
from apysc._validation import arg_validation_decos


class PathXInterface(RevertInterface, AttrLinkingInterface):

    _x: Int

    def _initialize_x_if_not_initialized(self) -> None:
        """
        Initialize the _x attribute if this instance does not
        initialize it yet.
        """
        if hasattr(self, '_x'):
            return
        self._x = Int(0)

        self._append_x_linking_setting()

    @add_debug_info_setting(
        module_name=__name__, class_name='PathXInterface')
    def _append_x_linking_setting(self) -> None:
        """
        Append an x attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._x, attr_name='x')
        self._append_attr_to_linking_stack(
            attr=self._x, attr_name='x')

    @property
    @add_debug_info_setting(
        module_name=__name__, class_name='PathXInterface')
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
        self._initialize_x_if_not_initialized()
        return self._x._copy()

    @x.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @add_debug_info_setting(
        module_name=__name__, class_name='PathXInterface')
    def x(self, value: Int) -> None:
        """
        Set a x-coordinate of the destination point.

        Parameters
        ----------
        value : Int
            X-coordinate of the destination point.
        """
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
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_x_if_not_initialized()
        self._x._value = self._x_snapshots[snapshot_name]
