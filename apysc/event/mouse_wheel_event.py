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
        return delta_y
