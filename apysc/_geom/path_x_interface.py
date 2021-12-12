"""Interface class implementation for the x path data.
"""

from apysc._type.int import Int


class PathXInterface:

    _x: Int

    @property
    def x(self) -> Int:
        """
        Get a x-coordinate of the destination point.

        Returns
        -------
        x : Int
            A x-coordinate of the destination point.
        """
        return self._x._copy()

    @x.setter
    def x(self, value: Int) -> None:
        """
        Set a x-coordinate of the destination point.

        Parameters
        ----------
        value : Int
            X-coordinate of the destination point.
        """
        self._x.value = value
