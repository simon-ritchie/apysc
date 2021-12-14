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
        import apysc as ap
        with ap.DebugInfo(
                callable_='control_x', locals_=locals(),
                module_name=__name__, class_=PathControlXInterface):
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
        import apysc as ap
        with ap.DebugInfo(
                callable_='control_x', locals_=locals(),
                module_name=__name__, class_=PathControlXInterface):
            self._control_x.value = value
