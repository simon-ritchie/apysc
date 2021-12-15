"""Interface class implementation for the destination y path data.
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
        import apysc as ap
        with ap.DebugInfo(
                callable_='dest_y', locals_=locals(),
                module_name=__name__, class_=PathDestYInterface):
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
        import apysc as ap
        with ap.DebugInfo(
                callable_='dest_y', locals_=locals(),
                module_name=__name__, class_=PathDestYInterface):
            self._dest_y.value = value
