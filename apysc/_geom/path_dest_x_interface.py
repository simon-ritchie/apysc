"""Interface class implementation for the destination x path data.
"""

from apysc._type.int import Int


class PathDestXInterface:

    _dest_x: Int

    @property
    def dest_x(self) -> Int:
        """
        Get a x-coordinate of the destination point.

        Returns
        -------
        dest_x : Int
            X-coordinate of the destination point.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='dest_x', locals_=locals(),
                module_name=__name__, class_=PathDestXInterface):
            return self._dest_x._copy()

    @dest_x.setter
    def dest_x(self, value: Int) -> None:
        """
        Set a x-coordinate of the destination point.

        Parameters
        ----------
        value : Int
            X-coordinate of the destination point.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='dest_x', locals_=locals(),
                module_name=__name__, class_=PathDestXInterface):
            self._dest_x.value = value
