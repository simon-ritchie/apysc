"""Class implementation for ellipse width interface.
"""

from typing import Dict
from apysc import Int
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface


class EllipseWidthInterface(VariableNameInterface, RevertInterface):

    _ellipse_width: Int

    def _initialize_ellipse_width_if_not_initialized(self) -> None:
        """
        Initialize _ellipse_width attribute if it is not initialized yet.
        """
        if hasattr(self, '_ellipse_width'):
            return
        self._ellipse_width = Int(0)

    @property
    def ellipse_width(self) -> Int:
        """
        Get ellipse size value.

        Returns
        -------
        ellipse_width : Int
            Ellipse width value.
        """
        from apysc.type import value_util
        self._initialize_ellipse_width_if_not_initialized()
        return value_util.get_copy(value=self._ellipse_width)

    @ellipse_width.setter
    def ellipse_width(self, value: Int) -> None:
        """
        Update ellipse width value.

        Parameters
        ----------
        value : int or Int
            Ellipse width value.
        """
        from apysc.validation import number_validation
        if not isinstance(value, Int):
            number_validation.validate_integer(integer=value)
            value = Int(value)
        self._ellipse_width = value

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        pass

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        pass
