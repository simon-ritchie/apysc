"""Interface class implementation for the control x path data.
"""

from apysc._type.int import Int


class PathControlXInterface:

    _control_x: Int

    @property
    def control_x(self) -> Int:
        """
        Get a X-coordinate of the point.

        Returns
        -------
        control_x : Int
            X-coordinate of the control point.
        """
        return self._control_x._copy()

    @control_x.setter
    def control_x(self, value: Int) -> None:
        """
        Set a X-coordinate of the control point.

        Parameters
        ----------
        value : Int
            X-coordinate of the control point.
        """
        self._control_x.value = value
