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

    @width.setter
    def width(self, value: Int) -> None:
        """
        Update a ellipse width value.

        Parameters
        ----------
        value : int or Int
            Ellipse width value.
        """
        from apysc.validation import number_validation
        if not isinstance(value, Int):
            number_validation.validate_integer(integer=value)
            value = Int(value)
        self._width = value

    @property
    def height(self) -> Int:
        """
        Get a ellipse height value.

        Parameters
        ----------
        height : Int
            Ellipse height.
        """
        from apysc.type import value_util
        self._initialize_width_and_height_if_not_initialized()
        return value_util.get_copy(value=self._height)

    @height.setter
    def height(self, value: Int) -> None:
        """
        Update a ellipse height value.

        Parameters
        ----------
        value : int or Int
            Ellipse height value.
        """
        from apysc.validation import number_validation
        if not isinstance(value, Int):
            number_validation.validate_integer(integer=value)
            value = Int(value)
        self._height = value

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
