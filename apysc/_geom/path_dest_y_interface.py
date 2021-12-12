"""Interface class implementation for the path destination y data.
"""

from apysc._type.int import Int


class PathDestYInterface:

    _dest_y: Int

    @property
    def dest_y(self) -> Int:
        """
        Get a y-coordinate of the destination point.

        Returns
        -------
        dest_y : Int
            Y-coordinate of the destination point
        """
        return self._dest_y._copy()

    @dest_y.setter
    def dest_y(self, value: Int) -> None:
        """
        Set a y-coordinate of the destination point.

        Parameters
        ----------
        value : Int
            Y-coordinate of the destination point
        """
        self._dest_y.value = value
