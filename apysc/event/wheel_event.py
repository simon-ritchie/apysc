"""Class implementation for mouse wheel event.
"""

from typing import Generic
from typing import TypeVar

from apysc import Int
from apysc.event.event import Event
from apysc.type.variable_name_interface import VariableNameInterface


class WheelEvent(Event):

    def __init__(self) -> None:
        """
        Mouse wheel event class.

        Notes
        -----
        Not supported each SVG elements' mouse wheel event currently, only
        supported document (overall screen) mouse wheel.
        """
        from apysc.expression import var_names
        super(WheelEvent, self).__init__(
            this=None,
            type_name=var_names.MOUSE_WHEEL_EVENT)

    @property
    def this(self) -> None:
        """
        WheelEvent instance isn't supported this property.
        """
        raise Exception(
            'WheelEvent instance isn\'t supported this property.')

    @property
    def delta_y(self) -> Int:
        """
        Vertical mouse wheel value. If down direction, this value will
        be positive, inversely up one will be negative.

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
        from apysc.expression import expression_file_util
        expression: str = (
            f'{delta_y.variable_name} = '
            f'{self.variable_name}.deltaY;'
        )
        expression_file_util.append_js_expression(expression=expression)
