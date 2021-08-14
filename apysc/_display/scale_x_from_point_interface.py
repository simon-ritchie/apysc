"""Class implementation for the scale_x_from_point interface.
"""


from typing import Union
import apysc as ap
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class ScaleXFromPointInterface(VariableNameInterface, RevertInterface):

    _scale_x_from_points: ap.Dictionary

    def _initialize_scale_x_from_points_if_not_initialized(self) -> None:
        """
        Initialize the `_scale_x_from_points` attribute if it hasn't been
        initialized_yet.
        """
        if hasattr(self, '_scale_x_from_points'):
            return
        self._scale_x_from_points = ap.Dictionary({})

    def get_scale_x_from_points(
            self,
            x: Union[int, ap.Int],
            y: Union[int, ap.Int]) -> ap.Number:
        """
        Get a scale-x value from the given point.

        Parameters
        ----------
        x : int or Int
            X-coordinate.
        y : int or Int
            Y-coordinate.

        Returns
        -------
        scale_x : ap.Number
            Scale-x value from the given point.
        """
        self._initialize_scale_x_from_points_if_not_initialized()
        default_val: ap.Number = ap.Number(1.0)
        # scale_x: ap.Number = self._scale_x_from_points
        pass

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert a value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
