"""Interface class implementation for the second control y path data.
"""

from apysc._type.int import Int


class PathControlY2Interface:

    _control_y2: Int

    @property
    def control_y2(self) -> Int:
        """
        Get a second y-coordinate of the control point.

        Returns
        -------
        control_y2 : Int
            Second y-coordinate of the control point.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='control_y2', locals_=locals(),
                module_name=__name__, class_=PathControlY2Interface):
            return self._control_y2._copy()

    @control_y2.setter
    def control_y2(self, value: Int) -> None:
        """
        Set a second y-coordinate of the control point.

        Parameters
        ----------
        value : Int
            Second y-coordinate of the control point.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='control_y2', locals_=locals(),
                module_name=__name__, class_=PathControlY2Interface):
            self._control_y2.value = value
