"""Class implementation of the width and height Interfaces
for the ellipse.

Notes
-----
Subclass that inherit the normal WidthInterface and HeightInterface
can't use this interface.
"""

from typing import Dict

from apysc import Int
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface


class WidthAndHeightInterfacesForEllipse(
        VariableNameInterface, RevertInterface):

    _width: Int
    _height: Int

    def _initialize_width_and_height_if_not_initialized(self) -> None:
        """
        Initialize _width and _height attributes if these are not
        initialized yet.
        """
        if not hasattr(self, '_width'):
            self._width = Int(0)
        if not hasattr(self, '_height'):
            self._height = Int(0)

    @property
    def width(self) -> Int:
        """
        Get a ellipse width value.

        Returns
        -------
        width : Int
            Ellipse width.
        """
        from apysc.type import value_util
        self._initialize_width_and_height_if_not_initialized()
        return value_util.get_copy(value=self._width)

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make the values' snapshots.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert the values if the snapshots exist.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
