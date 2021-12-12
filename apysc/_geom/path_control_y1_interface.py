"""Interface class implementation for the first control y path data.
"""

from apysc._type.int import Int


class PathControlY1Interface:

    _control_y1: Int

    @property
    def control_y1(self) -> Int:
        """
        Get a first y-coordinate of the control point.

        Returns
        -------
        control_y1 : Int
            First y-coordinate of the control point.
        """
        return self._control_y1._copy()

    @control_y1.setter
    def control_y1(self, value: Int) -> None:
        """
        Set a first y-coordinate of the control point.

        Parameters
        ----------
        value : Int
            First y-coordinate of the control point.
        """
        self._control_y1.value = value
