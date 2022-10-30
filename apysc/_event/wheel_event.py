"""Class implementation for mouse wheel event.
"""

from typing_extensions import final

from apysc._event.event import Event
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.variable_name_mixin import VariableNameMixIn


class WheelEvent(Event):
    """
    Mouse wheel event class.
    """

    @final
    @add_debug_info_setting(module_name=__name__)
    def __init__(self, *, this: VariableNameMixIn) -> None:
        """
        Mouse wheel event class.

        Parameters
        ----------
        this : VariableNameMixIn
            Instance will be binded this event.

        Notes
        -----
        Not supported each SVG elements' mouse wheel event currently, only
        supported document (overall screen) mouse wheel.
        """
        from apysc._expression import var_names

        super(WheelEvent, self).__init__(this=this, type_name=var_names.WHEEL_EVENT)

    @property
    @add_debug_info_setting(module_name=__name__)
    def delta_x(self) -> Int:
        """
        Horizontal mouse wheel value.

        Returns
        -------
        delta_x : Int
            Delta x value.
        """
        import apysc as ap

        delta_x: ap.Int = ap.Int(0)
        self._append_delta_x_getter_expression(delta_x=delta_x)
        return delta_x

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_delta_x_getter_expression(self, *, delta_x: Int) -> None:
        """
        Append delta_x getter property's expression.

        Parameters
        ----------
        delta_x : Int
            Target delta x value.
        """
        import apysc as ap

        expression: str = f"{delta_x.variable_name} = " f"{self.variable_name}.deltaX;"
        ap.append_js_expression(expression=expression)

    @property
    @add_debug_info_setting(module_name=__name__)
    def delta_y(self) -> Int:
        """
        Vertical mouse wheel value.

        Returns
        -------
        delta_y : Int
            Delta y value.
        """
        import apysc as ap

        delta_y: ap.Int = ap.Int(0)
        self._append_delta_y_getter_expression(delta_y=delta_y)
        return delta_y

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_delta_y_getter_expression(self, *, delta_y: Int) -> None:
        """
        Append delta_y getter property's expression.

        Parameters
        ----------
        delta_y : Int
            Target delta y value.
        """
        import apysc as ap

        expression: str = f"{delta_y.variable_name} = " f"{self.variable_name}.deltaY;"
        ap.append_js_expression(expression=expression)
