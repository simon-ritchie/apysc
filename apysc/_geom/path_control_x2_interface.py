"""Interface class implementation for the second control x path data.
"""

from apysc._type.int import Int


class PathControlX2Interface:

    _control_x2: Int

    @property
    def control_x2(self) -> Int:
        """
        Get a second x-coordinate of the control point.

        Returns
        -------
        control_x2 : Int
            Second x-coordinate of the control point.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='control_x2', locals_=locals(),
                module_name=__name__, class_=PathControlX2Interface):
            return self._control_x2._copy()

    @control_x2.setter
    def control_x2(self, value: Int) -> None:
        """
        Set a second x-coordinate of the control point.

        Parameters
        ----------
        value : Int
            Second x-coordinate of the control point.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='control_x2', locals_=locals(),
                module_name=__name__, class_=PathControlX2Interface):
            self._control_x2.value = value
