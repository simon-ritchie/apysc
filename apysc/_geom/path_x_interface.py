"""Interface class implementation for the path data x.
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
