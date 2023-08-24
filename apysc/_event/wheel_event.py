"""Class implementation for mouse wheel event.
"""

from typing_extensions import final

from apysc._event.event import Event
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number
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
    def delta_x(self) -> Number:
        """
        Horizontal mouse wheel value.

        Returns
        -------
        delta_x : Number
            Delta x value.
        """
        delta_x: Number = Number(0)
        self._append_delta_x_getter_expression(delta_x=delta_x)
        return delta_x

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_delta_x_getter_expression(self, *, delta_x: Number) -> None:
        """
        Append delta_x getter property's expression.

        Parameters
        ----------
        delta_x : Number
            Target delta x value.
        """
        from apysc._expression import expression_data_util

        expression: str = f"{delta_x.variable_name} = " f"{self.variable_name}.deltaX;"
        expression_data_util.append_js_expression(expression=expression)

    @property
    @add_debug_info_setting(module_name=__name__)
    def delta_y(self) -> Number:
        """
        Vertical mouse wheel value.

        Returns
        -------
        delta_y : Number
            Delta y value.
        """

        delta_y: Number = Number(0)
        self._append_delta_y_getter_expression(delta_y=delta_y)
        return delta_y

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_delta_y_getter_expression(self, *, delta_y: Number) -> None:
        """
        Append delta_y getter property's expression.

        Parameters
        ----------
        delta_y : Number
            Target delta y value.
        """
        from apysc._expression import expression_data_util

        expression: str = f"{delta_y.variable_name} = " f"{self.variable_name}.deltaY;"
        expression_data_util.append_js_expression(expression=expression)
