"""Interface class implementation for the first control x path data.
"""

from apysc._type.int import Int


class PathControlX1Interface:

    _control_x1: Int

    @property
    def control_x1(self) -> Int:
        """
        Get a first x-coordinate of the control point.

        Returns
        -------
        control_x1 : Int
            First x-coordinate of the control point.
        """
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
        self._control_x1.value = value
