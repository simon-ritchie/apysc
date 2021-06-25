"""Class implementation for mouse wheel event.
"""


from apysc import Int
from apysc._event.event import Event


class WheelEvent(Event):

    def __init__(self) -> None:
        """
        Mouse wheel event class.

        Notes
        -----
        Not supported each SVG elements' mouse wheel event currently, only
        supported document (overall screen) mouse wheel.
        """
        from apysc._expression import var_names
        super(WheelEvent, self).__init__(
            this=None,
            type_name=var_names.WHEEL_EVENT)

    @property
    def this(self) -> None:
        """
        WheelEvent instance isn't supported this property.
        """
        raise Exception(
            'WheelEvent instance isn\'t supported this property.')

    def prevent_default(self) -> None:
        """
        WheelEvent instance isn't supported this interface.
        """
        raise Exception(
            'WheelEvent instance isn\'t supported this interface.')

    @property
    def delta_x(self) -> Int:
        """
        Horizontal mouse wheel value.

        Returns
        -------
        delta_x : Int
            Delta x value.
        """
        delta_x: Int = Int(0)
        self._append_delta_x_getter_expression(delta_x=delta_x)
        return delta_x

    def _append_delta_x_getter_expression(self, delta_x: Int) -> None:
        """
        Append delta_x getter property's expression to file.

        Parameters
        ----------
        delta_x : Int
            Target delta x value.
        """
        from apysc import append_js_expression
        expression: str = (
            f'{delta_x.variable_name} = '
            f'{self.variable_name}.deltaX;'
        )
        append_js_expression(expression=expression)

    @property
    def delta_y(self) -> Int:
        """
        Vertical mouse wheel value.

        Returns
        -------
        delta_y : Int
            Delta y value.
        """
        delta_y: Int = Int(0)
        self._append_delta_y_getter_expression(delta_y=delta_y)
        return delta_y

    def _append_delta_y_getter_expression(self, delta_y: Int) -> None:
        """
        Append delta_y getter property's expression to file.

        Parameters
        ----------
        delta_y : Int
            Target delta y value.
        """
        from apysc import append_js_expression
        expression: str = (
            f'{delta_y.variable_name} = '
            f'{self.variable_name}.deltaY;'
        )
        append_js_expression(expression=expression)
