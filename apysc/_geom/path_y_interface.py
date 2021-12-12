"""Interface class implementation for the path data y.
"""

from apysc._type.int import Int


class PathYInterface:

    _y: Int

    @property
    def y(self) -> Int:
        """
        Get a y-coordinate of the destination point.

        Returns
        -------
        y : Int
            A y-coordinate of the destination point.
        """
        return self._y

    @y.setter
    def y(self, value: Int) -> None:
        """
        Set a y-coordinate of the destination point.

        Parameters
        ----------
        value : Int
            Y-coordinate of the destination point.
        """
        self._y.value = value
