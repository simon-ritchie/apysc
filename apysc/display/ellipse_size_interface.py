"""Class implementation for ellipse size interface.
"""

from apysc import Int
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface


class EllipseSizeInterface(VariableNameInterface, RevertInterface):

    _ellipse_size: Int

    def _initialize_ellipse_size_if_not_initialized(self) -> None:
        """
        Initialize _ellipse_size attribute if it is not initialized yet.
        """
        if hasattr(self, '_ellipse_size'):
            return
        self._ellipse_size = Int(0)

    @property
    def ellipse_size(self) -> Int:
        """
        Get a ellipse size value.

        Returns
        -------
        ellipse_size : Int
            Ellipse size value.
        """
        from apysc.type import value_util
        self._initialize_ellipse_size_if_not_initialized()
        return value_util.get_copy(value=self._ellipse_size)

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
