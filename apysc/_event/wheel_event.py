"""Class implementation for mouse wheel event.
"""


import apysc as ap
from apysc._event.event import Event
from apysc._type.variable_name_interface import VariableNameInterface


class WheelEvent(Event):
    """
    Mouse wheel event class.
    """

    def __init__(self, this: VariableNameInterface) -> None:
        """
        Mouse wheel event class.

        Parameters
        ----------
        this : VariableNameInterface
            Instance will be binded this event.

        Notes
        -----
        Not supported each SVG elements' mouse wheel event currently, only
        supported document (overall screen) mouse wheel.
        """
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=WheelEvent):
            from apysc._expression import var_names
            super(WheelEvent, self).__init__(
                this=this,
                type_name=var_names.WHEEL_EVENT)

    def prevent_default(self) -> None:
        """
        WheelEvent instance isn't supported this interface.
        """
        raise Exception(
            'WheelEvent instance isn\'t supported this interface.')

    @property
    def delta_x(self) -> ap.Int:
        """
        Horizontal mouse wheel value.

        Returns
        -------
        delta_x : Int
            Delta x value.
        """
        with ap.DebugInfo(
                callable_='delta_x', locals_=locals(),
                module_name=__name__, class_=WheelEvent):
            delta_x: ap.Int = ap.Int(0)
            self._append_delta_x_getter_expression(delta_x=delta_x)
            return delta_x

    def _append_delta_x_getter_expression(self, delta_x: ap.Int) -> None:
        """
        Append delta_x getter property's expression.

        Parameters
        ----------
        delta_x : Int
            Target delta x value.
        """
        with ap.DebugInfo(
                callable_=self._append_delta_x_getter_expression,
                locals_=locals(),
                module_name=__name__, class_=WheelEvent):
            expression: str = (
                f'{delta_x.variable_name} = '
                f'{self.variable_name}.deltaX;'
            )
            ap.append_js_expression(expression=expression)

    @property
    def delta_y(self) -> ap.Int:
        """
        Vertical mouse wheel value.

        Returns
        -------
        delta_y : Int
            Delta y value.
        """
        with ap.DebugInfo(
                callable_='delta_y', locals_=locals(),
                module_name=__name__, class_=WheelEvent):
            delta_y: ap.Int = ap.Int(0)
            self._append_delta_y_getter_expression(delta_y=delta_y)
            return delta_y

    def _append_delta_y_getter_expression(self, delta_y: ap.Int) -> None:
        """
        Append delta_y getter property's expression.

        Parameters
        ----------
        delta_y : Int
            Target delta y value.
        """
        expression: str = (
            f'{delta_y.variable_name} = '
            f'{self.variable_name}.deltaY;'
        )
        ap.append_js_expression(expression=expression)
